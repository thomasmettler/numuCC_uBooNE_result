# Instructions

Here is the numu CC inclusive result using Run 3 data from the MicroBooNE detector
The script should assists for comparison of models to the data of this analysis inclusing all systematics evaluated.

For this reason a python library is provided here along with the measured data points as well as the prediction form the base simulation of the experiment.

Additionally there are all varied historgrams for the calculation of uncertainties.

An example of how the library can be used is given in example.py. Just replace the histogram of the true distibution with a new one and let it run. It will calculate chi2 and make an event rate plot using the new signal event rate prediction.

The POT of the data is 2.144e+20.

For questions get in contact with: thomas.mettler@lhep.unibe.ch


## Functions of the library:

# arr2plot(this_arr)
Takes a numpy array and returns a ROOT THXF of it.

# plot2arr(h_this_tmp, dim)
Takes a ROOT TH1 or TH2 as well as the dimension (1 for TH1 2 for TH2) and returns a numpt array of it.

# return_detsys_covar(h_true,this_pot)
Takes the true event rate for MicroBooNE of a model as well as the simulated POT and returns the fractional covariance matrix as a numpy array for the detecotr responce uncertainties.


# return_other_covar(h_true,this_pot)


return_all_covar(h_true,this_pot)


return_flux_covar(h_true,this_pot)


return_crt_covar(h_true,this_pot)


return_dirt_covar(h_true,this_pot)


return_stat_covar(h_true,this_pot)


predict(h_true,this_pot)


eventrate_comparison(h_data_func,h_true_func,this_pot,this_frac_tot, filename,model_name)


my_chi2(h_data, h_true_func,this_pot, frac)


chi2_minus1(h_data, h_true_func,this_pot, frac)