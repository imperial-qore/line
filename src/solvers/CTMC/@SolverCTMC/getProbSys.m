function Pn = getProbSys(self)
% PN = GETPROBSYSSTATE()

if ~isfield(self.options,'keep')
    self.options.keep = false;
end
T0 = tic;
qn = self.model.getStruct;
if self.model.isStateValid
    Pn = solver_ctmc_joint(qn, self.options);
    self.result.('solver') = self.getName();
    self.result.Prob.joint = Pn;
else
    error('The model state is invalid.');
end
runtime = toc(T0);
self.result.runtime = runtime;
end