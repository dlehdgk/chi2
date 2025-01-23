# $\chi^2$ test on Cosmologies

- This repository contains code to obtain $\chi^2$ values for fixed cosmological parameters.
- tested with mean $\Lambda$CDM parameter values from Planck 2018 results.
- beta include runs for different values of the $\beta_{DE}$ parameter.

## Aims

- to obtain $\chi^2$ values for fixed cosmological parameters, varying my $\beta_{DE}$ parameter to see if there is a jump in the values over the interval where the transition from the standard paramterisation to log parameterisation occurs for small $\beta_{DE}$.
- this is important as the cobaya runs for the $\beta_{DE}$ CAMB modification is resulting in frequent segmentation faults.
- seeing if this transition is the causing this issue might be able to resolve the problem.
- plot the values of $\chi^2$ for the range of $\beta_{DE}$ and see if there are abnormalities

## Progress

- created a shell script to loop over the values of $\beta_{DE}$ but there is an issue with the plots.
- the override in `evaluate` is not working as expected. Changed the code to modify the $\beta_{DE}$ line directly
- need to add the `dark_energy_model: ppf` line to the theory section of the input yaml file for non $\Lambda$CDM models.
- remove the `drop: true` line from `logA` as this is a relevant parameter to constrain *(but why is this in the usual input yaml file?)*
- thought we need to remove H0 and use `theta_MC_100` instead but this does not work. Might be to do with CAMB taking H0 in the ini input file
- as the log parameterisation is independent of $\beta_{DE}$ we should expect the $\chi^2$ values to be constant over the log interval but this is not the case.
- issue may be to do with the the fact that the planck likelihoods contain internal parameters which are being varied for each run.
- this would result in varying $\chi^2$ even when all the cosmological parameters are fixed
- need to remove the planck likelihoods and just use bao and sne likelihoods as they do not contain internal parameters (or use planck-lite likelihoods which also do not have additional parameters)

- issue with the transition being at 0.0005 is that CAMB cannot compute the cosmology in the region around this point and so cannot verify if we need the transition point to be smaller
- points are very close together but there are several discontinuities in the region **why?**
- might be a good idea to compare the values for 0.001 transition with something larger like 0.01 or larger to see what difference it would make.
- it's clear that having 0.0005 does not improve the transition smoothness compared to 0.001
