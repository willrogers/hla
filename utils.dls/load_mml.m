function load_mml(ringmode)

    fprintf('Loading data for ring mode %s\n', ringmode);
    dir = fileparts(mfilename('fullpath'));
    cd(dir);

    loaded_mode = getfamilydata('OperationalMode');

    if ~strcmp(loaded_mode, ringmode)
        fprintf('MML ring mode %s loaded, not %s\n', loaded_mode, ringmode);
        fprintf('Exiting.\n');
        return;
    end

    switch2sim;

    % load directly into the ap SQL database
    machine_dir = fullfile(dir, '..', 'aphla', 'machines', ringmode);

    % mksqlite library in this repository for now.
    addpath('./mksqlite');
    DB_FILE = fullfile(machine_dir, 'data.sqlite');

    mksqlite('open', DB_FILE);
    mksqlite('delete from elements');
    mksqlite('delete from pvs');

    global THERING;
    ao = getao();

    % The individual BPM PVs are not stored in middlelayer.
    global BPMS;
    BPMS = get_bpm_pvs(ao);

    % Map from AT types to types in the accelerator object (ao).
    global TYPE_MAP;
    keys = {'QUAD', 'SEXT', 'VSTR', 'HSTR', 'BEND'};
    values = {'QUAD_', 'SEXT_', 'VCM', 'HCM', 'BB'};
    TYPE_MAP = containers.Map(keys, values);

    usedElements = containers.Map();

    s = 0;

    for i = 1:length(THERING)
        disp(i);
        elm = THERING{i};
        s = s + elm.Length;
        insertelement(i, elm, s, ringmode);

        type = gettype(elm);
        if usedElements.isKey(type)
            usedElements(type) = usedElements(type) + 1;
        else
            usedElements(type) = 1;
        end
        pvs = getpvs(ao, elm, usedElements);
        insertpvs(i, pvs);
    end

    % The following families  and do not have their
    % own elements.  We insert their PVs separately.
    insertextrapvs('SQUAD', 'a1');
    insertextrapvs('BBVMXS', 'db0');
    insertextrapvs('BBVMXL', 'db0');

    % DCCT not in THERING.
    dcct = struct ('FamName', 'DCCT', 'Length', 0);
    i = i + 1;
    insertelement(i, dcct, 0, ringmode);
    s = pv_struct('SR-DI-DCCT-01:SIGNAL', 'I', 'get');
    insertpvs(i, {s});

    mksqlite('close');

    % finally, load unit conversion data
    load_unitconv(ringmode);

end


function type = gettype(elm)
    if isfield(elm, 'Class')
        type = elm.Class;
    elseif isfield(elm, 'FamName')
            type = elm.FamName;
    else
        type = '';
    end
end


function insertpvs(index, pvs)
    PV_INSERT = 'insert into pvs (pv, elemName, elemField, elemHandle) values (?,?,?,?)';
    for i = 1:length(pvs)
        pv = pvs{i};
        mksqlite(PV_INSERT, pv.pv, num2str(index), pv.field, pv.handle);
    end

end


% Construct BPM PVs from MML indices
function bpms = get_bpm_pvs(ao)
    nbpms = size(ao.BPMx.DeviceList, 1);
    bpms = cell(nbpms);
    for i = 1:nbpms
        ncell = ao.BPMx.DeviceList(i,1);
        index = ao.BPMx.DeviceList(i,2);
        if mod(ncell, 1) ~= 0
            % Indices of .5 correspond to SRnnS-DI-EBPM-nn.
            ncell = fix(ncell);
            bpms{i} = sprintf('SR%02dS-DI-EBPM-%02d\n', ncell, index);
        else
            bpms{i} = sprintf('SR%02dC-DI-EBPM-%02d\n', ncell, index);
        end
    end
end


function pvs = getpvs(ao, elm, usedElements)

    global BPMS;
    global TYPE_MAP;

    type = gettype(elm);

    if any(ismember(type, TYPE_MAP.keys))
        if strcmp(type, 'QUAD')
            field = 'b1';
        elseif strcmp(type, 'SEXT')
            field = 'b2';
        else
            field = 'b0';
        end
        % MML is inconsistent about whether the family for the bends
        % is BEND or BB.
        if strcmp(type, 'BEND') && isfield(ao, 'BEND')
            family = 'BEND';
        else
            family = TYPE_MAP(type);
        end
        index = usedElements(type);

        get_pv = ao.(family).Monitor.ChannelNames(index, :);
        gpv = pv_struct(get_pv, field, 'get');
        set_pv = ao.(family).Setpoint.ChannelNames(index, :);
        spv = pv_struct(set_pv, field, 'put');
        pvs = {gpv, spv};
    elseif strcmp(type, 'BPM')
        index = usedElements(type);
        get_x_pv = strcat(BPMS{index}, ':SA:X');
        x_pv = pv_struct(get_x_pv, 'x', 'get');
        get_y_pv = strcat(BPMS{index}, ':SA:Y');
        y_pv = pv_struct(get_y_pv, 'y', 'get');
        pvs = {x_pv, y_pv};
    elseif strcmp(type, 'RF')
        gfpv = ao.(type).Monitor.ChannelNames;
        get_f_pv = pv_struct(gfpv, 'f', 'get');
        sfpv = ao.(type).Setpoint.ChannelNames;
        set_f_pv = pv_struct(sfpv, 'f', 'put');
        % voltage?
        pvs = {get_f_pv, set_f_pv};
    else
        pvs = {};
    end

end

function insertextrapvs(family, field)
    elms = getfamilydata(family);
    if ~isempty(elms)
        for i = 1:length(elms.AT.ATIndex)
            get_pv = elms.Monitor.ChannelNames(i,:);
            gpv = pv_struct(get_pv, field, 'get');
            set_pv = elms.Setpoint.ChannelNames(i,:);
            spv = pv_struct(set_pv, field, 'put');
            insertpvs(elms.AT.ATIndex(i), {gpv, spv});
        end
    end
end

function s = pv_struct(pv, field, handle)
    s = struct('pv', pv, 'field', field, 'handle', handle);
end

function insertelement(i, elm, s, ringmode)
    INSERT_ELEMENT = 'insert into elements (elemName, elemLength, elemPosition, elemIndex, elemType, elemGroups, cell, k1, k2, virtual) values (?,?,?,?,?,?,?,?,?,?)';
    k1 = 0;
    k2 = 0;
    type = gettype(elm);
    groups = elm.FamName;
    cell = sprintf('%d', getcell(s, ringmode));

    % Elements with additional PVs require an extra group added.
    extra_groups = {'SQUAD', 'BBVMXS', 'BBVMXL'};
    for j = 1:length(extra_groups)
        group = extra_groups{j};
        elms = getfamilydata(group);
        if ~isempty(elms) && ismember(i, elms.AT.ATIndex)
            groups = strcat(groups, ';', group);
        end
    end

    if strcmp(type, 'QUAD')
        k1 = elm.K;
        k2 = 0;
    elseif strcmp(type, 'SEXT')
        k2 = elm.PolynomB(3);
        k1 = 0;
    elseif strcmp(type, 'BEND') && any(elm.PolynomB)
        k1 = elm.K;
    end
    mksqlite(INSERT_ELEMENT, num2str(i), elm.Length, s, num2str(i), type, groups, cell, k1, k2, 0);
end

function cell = getcell(position, ringmode)
    % Hard-coded values here - I can't see a better way to do this.
    oldcircumference = 561.6;
    newcircumference = 561.571;
    cell2diff = oldcircumference - newcircumference;
    boundaries = linspace(0, 561.6, 25);
    if is_ddba(ringmode)
        boundaries(3:end) = boundaries(3:end) - cell2diff;
    end
    for c = 1:length(boundaries)
        if position < boundaries(c)
            cell = c - 1;
            break
        end
    end
end

function is_ddba = is_ddba(ringmode)
    is_ddba = strcmp(ringmode, 'VMX') || strcmp(ringmode , 'VMXSP');
end