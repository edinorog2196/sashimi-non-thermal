Here  you can find the output products for  Mixed Warm Dark Matter Constraints using Milky Way Satellite Galaxy Counts by Chin Yi Tan, Ariane Dekker, and Alex Drlica Wagner [(2409.18917)](https://arxiv.org/abs/2409.18917).

The `Get_suppression_function.ipynb` notebook contains plots of the suppression function for mixed warm dark matter scenarios where the WDM components could be either thermal relic WDM or 7keV sterlie neutrino.

The `Get_limits_and_posterior.ipynb` contains the posterior distribution function and the constraints for the mixed thermal relic scenario with different warm dark matter mass. The posterior is obtained by comparing the predicted MW satellite poppulation for different Mixed WDM scenarios with the observed satellite population using a [subhalo_satellite_connection model](https://github.com/eonadler/subhalo_satellite_connection/tree/master).

We run the python package emcee for 20,000 steps with 8 walkers to sample the posterior of nine free parameters in the model:
θmcmc = { Faint-end Slope (α), Luminosity scatter(σM), 50% occupation mass(M50), Occupation scatter(σgal), Baryonic effects(B), Size amplitude(A), Size scatter(σlog R),  Size power-law index(n), WDM fraction(fwdm)}. For the pure wdm chains: We have half-mode mass (Mhm) instead of WDM fraction(fwdm), which we defined as mwdm =  3 * ((10^Mhm) / 5e8)^(-3 / 10). We obtain limits for the mixed thermal relic scenario by considering the 20:1 and 10:1 posterior ratio constraints for wdm fraction for each MWDM mass.
