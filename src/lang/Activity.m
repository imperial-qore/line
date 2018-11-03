classdef Activity < matlab.mixin.Copyable
% Copyright (c) 2012-2018, Imperial College London
% All rights reserved.
    
    properties
        name;                       %string
        phase = 1;                  %int
        hostDemand = [];
        hostDemandMean = 0;         %double
        hostDemandSCV = 0;         %double
        parent;
        parentName;            %string
        boundToEntry;               %string
        synchCallDests = cell(0);   %string array
        synchCallMeans = [];        %integer array
        asynchCallDests = cell(0);  %string array
        asynchCallMeans = [];       %integer array
    end
    
    methods
        %public methods, including constructor
        
        %constructor
        function obj = Activity(model, name, hostDemand, boundToEntry, phase)
            if ~exist('name','var')
                error('Constructor requires to specify at least: name, hostDemandMean.');
            end
            obj.name = name;
            obj.parentName = '';
            if isnumeric(hostDemand)
                obj.hostDemand = Exp(1/hostDemand);
                obj.hostDemandMean = hostDemand;
                obj.hostDemandSCV = 1.0;
            elseif isa(hostDemand,'Distrib')
                obj.hostDemand = hostDemand;
                obj.hostDemandMean = hostDemand.getMean();
                obj.hostDemandSCV = hostDemand.getSCV();
            end
            if ~exist('boundToEntry','var')
                boundToEntry = '';
            end
            if ~exist('phase','var')
                phase = 1;
            end
            obj.boundToEntry = boundToEntry;
            obj.phase = phase;
            model.objects.activities{end+1} = obj;
        end
        
        function obj = setParent(obj, parentName)
            if isa(parentName,'Entry') ||  isa(parentName,'Task')
                obj.parentName = parentName.name;
                obj.parent = parentName;
            else
                obj.parentName = parentName;
                obj.parent = [];
            end
        end
        
        function obj = on(obj, parent)
            parent.addActivity(obj);
            obj.parent = parent;
        end
        
        function obj = repliesTo(obj, entry)
            if ~isempty(obj.parent)
                switch obj.parent.scheduling
                    case SchedStrategy.REF
                        error('Activities in reference tasks cannot reply.');
                    otherwise
                        entry.replyActivity{end+1} = obj.name;
                end
            else
                entry.replyActivity{end+1} = obj.name;
            end
        end
                
        function obj = boundTo(obj, entry)
            if isa(entry,'Entry')
                obj.boundToEntry = entry.name;
            elseif ischar(entry)
                obj.boundToEntry = entry;
            else
                    error('Wrong entry parameter for boundTo method.');
            end
        end
        
        %synchCall
        function obj = synchCall(obj, synchCallDest, synchCallMean)
            if ~exist('synchCallMean','var')
                synchCallMean = 1.0;
            end
            if ischar(synchCallDest)
                obj.synchCallDests{length(obj.synchCallDests)+1} = synchCallDest;
            else % object
                obj.synchCallDests{length(obj.synchCallDests)+1} = synchCallDest.name;
            end
            obj.synchCallMeans = [obj.synchCallMeans; synchCallMean];
        end
        
        %asynchCall
        function obj = asynchCall(obj, asynchCallDest, asynchCallMean)
            if nargin == 3
                if ischar(asynchCallDest)
                    obj.asynchCallDests{length(obj.asynchCallDests)+1} = asynchCallDest;
                else % object
                    obj.asynchCallDests{length(obj.asynchCallDests)+1} = asynchCallDest.name;
                end
                obj.asynchCallMeans = [obj.asynchCallMeans; asynchCallMean];
            end
        end
        
    end
    
end