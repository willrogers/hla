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
    keys = {'QUAD', 'SEXT', 'VSTR', 'HSTR'};
    values = {'QUAD_', 'SEXT_', 'VCM', 'HCM'};
    TYPE_MAP = containers.Map(keys, values);

    usedElements = containers.Map();

    s = 0;

    for i = 1:length(THERING)
        disp(i);
        elm = THERING{i};
        s = s + elm.Length;
        insertelement(i, elm, s);

        type = gettype(elm);
        if usedElements.isKey(type)
            usedElements(type) = usedElements(type) + 1;
        else
            usedElements(type) = 1;
        end
        pvs = getpvs(ao, elm, usedElements);
        insertpvs(i, pvs);
    end

    % DCCT not in THERING.
    dcct = struct ('FamName', 'DCCT', 'Length', 0);
    i = i + 1;
    insertelement(i, dcct, 0);
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

    if strcmp(type, 'QUAD') || strcmp(type, 'SEXT') || strcmp(type, 'HSTR') || strcmp(type, 'VSTR')
        if strcmp(type, 'QUAD')
            field = 'b1';
        elseif strcmp(type, 'SEXT')
            field = 'b2';
        else
            field = 'b0';
        end
        index = usedElements(type);
        family = TYPE_MAP(type);
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


function s = pv_struct(pv, field, handle)
    s = struct('pv', pv, 'field', field, 'handle', handle);
end

function insertelement(i, elm, s)
    INSERT_ELEMENT = 'insert into elements (elemName, elemLength, elemPosition, elemIndex, elemType, elemGroups, k1, k2, virtual) values (?,?,?,?,?,?,?,?,?)';
    k1 = 0;
    k2 = 0;
    type = gettype(elm);

    if strcmp(type, 'QUAD')
        k1 = elm.K;
        k2 = 0;
    elseif strcmp(type, 'SEXT')
        k2 = elm.PolynomB(3);
        k1 = 0;
    elseif strcmp(type, 'BEND' ) && any(elm.PolynomB)
        k1 = elm.K;
    end
    mksqlite(INSERT_ELEMENT, num2str(i), elm.Length, s, num2str(i), type, elm.FamName, k1, k2, 0);
end

