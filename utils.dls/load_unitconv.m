function load_unitconv(ringmode)

dir = fileparts(mfilename('fullpath'));
cd(dir);
ini_file = fullfile(dir, '..', 'aphla', 'machines', ringmode, 'unitconv.ini');


fprintf('Loading unit conversions to file %s\n', ini_file);

quad_families = {'Q1D', 'Q2D', 'Q3D', 'Q2AD', 'Q1AD', 'Q1AB', 'Q2AB', 'Q3B', 'Q2B', 'Q1B', 'QM09', 'QM13'};
sext_families = {'S1D', 'S2D', 'S2A', 'S1A', 'S2C', 'S1C', 'S1B', 'S2B'};
bend_families = {'BEND', 'HCM', 'VCM'};

keys = {'BEND', 'VCM', 'HCM'};
values = {'BEND', 'VSTR', 'HSTR'};
BEND_TYPE_MAP = containers.Map(keys, values);

f = fopen(ini_file, 'w');

fprintf(f, '# Unit conversions generated by load_unitconv.m.\n\n');

for i = 1:length(quad_families)
   coeffs = get_poly_coeffs(quad_families{i}); 
   write_section(f, quad_families{i}, 'b1', 'A', 'm^-2', coeffs);
end

for i = 1:length(sext_families)
   coeffs = get_poly_coeffs(sext_families{i}); 
   write_section(f, sext_families{i}, 'b2', 'A', 'm^-3', coeffs);
end

for i = 1:length(bend_families)
   coeffs = get_poly_coeffs(bend_families{i}); 
   write_section(f, BEND_TYPE_MAP(bend_families{i}), 'b0', 'A', 'rad', coeffs);
end

write_section(f, 'BPM', 'x', 'mm', 'm', [0, 0, 0, 0.001, 0]);
write_section(f, 'BPM', 'y', 'mm', 'm', [0, 0, 0, 0.001, 0]);
fclose(f);

end


function write_section(file, group, field, src_unit, dst_unit, coeffs)

    fprintf(file, '[%s(%s)]\n', group, field);
    fprintf(file, 'dst_unit_sys: phy\n');
    fprintf(file, 'src_unit: %s\n', src_unit);
    fprintf(file, 'dst_unit: %s\n', dst_unit);
    fprintf(file, 'polynomial: %0.15f %0.15f %0.15f %0.15f %0.15f\n', coeffs);
    fprintf(file, 'groups: %s\n', group);
    fprintf(file, 'field: %s\n\n', field);

end


function coeffs = get_poly_coeffs(family)

    cal_data = get_cal_data(family);
    current_max = max(cal_data.current);
    if current_max < 0
        current_max = 0;
    end
    current_min = min(cal_data.current);
    if current_min > 0
        current_min = 0;
    end
    range = current_min:1:current_max;
    cal = [];
    for j = 1:length(range)
        cal(j) = hw2physics(family, 'Monitor', range(j), [1]);
    end
    coeffs = polyfit(range, cal, 4);
    disp(coeffs);
    
   % plot(cal_data.current, cal_data.field, 'x');
   % hold on
   % f = @(x) coeffs(1) .* x .^3 + coeffs(2) .* x .^2 + coeffs(3) .* x + coeffs(4);
   % plot(range, f(range) .* 10, 'r');
   % plot(range, cal .* 10, 'g');
   
   
end


function cal_data = get_cal_data(famname)

    global calibration_data;

    disp(famname);
    fd = getfamilydata(famname);
    chan = fd.Monitor.ChannelNames(1,:);
    index = calibration_lookup2(chan);
    cal_data = calibration_data{index};
    disp(cal_data);
    
end
