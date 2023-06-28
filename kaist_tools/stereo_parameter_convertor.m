stereo_params = load("stereoParams.mat");
json = jsonencode(stereo_params, "PrettyPrint", true);
fid = fopen('file.json','w');
fprintf(fid, '%s', json);
fclose(fid);