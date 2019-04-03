classdef DelayStation < Delay
    % Alias for the Delay class
    %
    % Copyright (c) 2012-2019, Imperial College London
    % All rights reserved.
    
    methods
        %Constructor
        function self = DelayStation(model, name)
            self@Delay(model, name);
        end
    end
    
end
