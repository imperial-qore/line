function W=qsys_gig1_approx_heyman(lambda,mu,ca,cs)
rho=lambda/mu;
W=rho/(1-rho)/mu*(ca^2+cs^2)/2+1/mu;
end