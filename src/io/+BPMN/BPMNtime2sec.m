function sec = BPMNtime2sec(bpmn_time)
% Copyright (c) 2012-2018, Imperial College London
% All rights reserved.

sec = 0;
idx = strfind(bpmn_time,':');
if length(idx) == 4
    yy = str2double( bpmn_time(1:idx(1)-1) );
    dd = str2double( bpmn_time(idx(1)+1:idx(2)-1) );
    hh = str2double( bpmn_time(idx(2)+1:idx(3)-1) );
    mm = str2double( bpmn_time(idx(3)+1:idx(4)-1) );
    ss = str2double( bpmn_time(idx(4)+1:end) );
    sec = ss + (mm +(hh+(dd+365*yy)*24)*60)*60;
end

