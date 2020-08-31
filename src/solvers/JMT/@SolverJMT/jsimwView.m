function jsimwView(self, options)
% JSIMWVIEW(OPTIONS)

% Copyright (c) 2012-2020, Imperial College London
% All rights reserved.

<<<<<<< HEAD
if ~self.supports(self.model)
    error('Line:FeatureNotSupportedBySolver','This model contains features not supported by the solver.');
=======
if self.enableChecks && ~self.supports(self.model)
   %line_warning(mfilename,'This model contains features not supported by the solver.'); 
ME = MException('Line:FeatureNotSupportedBySolver', 'This model contains features not supported by the solver.'); 
throw(ME);
>>>>>>> refs/remotes/origin/master
    %    runtime = toc(T0);
    %    return
end
if nargin<2
    options=self.options;
end
if options.samples< 5e3
    line_warning(mfilename,'JMT requires at least 5000 samples for each metric. Setting the samples to 5000.\n');
    options.samples = 5e3;
end
self.seed = options.seed;
self.maxSamples = options.samples;
writeJSIM(self);
%            if options.verbose
fileName = [self.getFilePath(),'jsimg',filesep, self.getFileName(), '.jsimg'];
<<<<<<< HEAD
fprintf(1,'JMT Model: %s\n',fileName);
=======
line_printf('\nJMT Model: %s',fileName);
>>>>>>> refs/remotes/origin/master
jsimwView(fileName);
end
