# Instructions

Here is the numu CC inclusive result using Run 3 data from the MicroBooNE detector
The script should assists for comparison of models to the data of this analysis inclusing all systematics evaluated.

For this reason a python library is provided here along with the measured data points as well as the prediction form the base simulation of the experiment.

Additionally there are all varied historgrams for the calculation of uncertainties.

An example of how the library can be used is given in example.py. Just replace the histogram of the true distibution with a new one and let it run. It will calculate chi2 and make an event rate plot using the new signal event rate prediction.

The POT of the data is 2.144e+20.

For questions get in contact with: thomas.mettler@lhep.unibe.ch


## Functions of the library:

### arr2plot(this_arr)
Takes a numpy array and returns a ROOT THXF of it.

### plot2arr(h_this_tmp, dim)
Takes a ROOT TH1 or TH2 as well as the dimension (1 for TH1 2 for TH2) and returns a numpt array of it.

### return_detsys_covar(h_true,this_pot)
Takes the true event rate for MicroBooNE of a model as well as the simulated POT and returns the fractional covariance matrix as a numpy array for the detecotr responce uncertainties.

### return_other_covar(h_true,this_pot)
Takes the true event rate for MicroBooNE of a model as well as the simulated POT and returns the fractional covariance matrix as a numpy array for the cross section uncertainties using single variations.

### return_all_covar(h_true,this_pot)
Takes the true event rate for MicroBooNE of a model as well as the simulated POT and returns the fractional covariance matrix as a numpy array for the cross section uncertainties using a multiverse of 600 universes.

### return_flux_covar(h_true,this_pot)
Takes the true event rate for MicroBooNE of a model as well as the simulated POT and returns the fractional covariance matrix as a numpy array for the flux uncertainties.

### return_crt_covar(h_true,this_pot)
Takes the true event rate for MicroBooNE of a model as well as the simulated POT and returns the fractional covariance matrix as a numpy array for the CRT uncertainties.

### return_dirt_covar(h_true,this_pot)
Takes the true event rate for MicroBooNE of a model as well as the simulated POT and returns the fractional covariance matrix as a numpy array for the uncertainties from the dirt contribution.

### return_stat_covar(h_true,this_pot)
Takes the true event rate for MicroBooNE of a model as well as the simulated POT and returns the fractional covariance matrix as a numpy array for the statistical uncertainty of the prediction.

### predict(h_true,this_pot)
Takes the true event rate for MicroBooNE of a model as well as the simulated POT and returns the predicted event rate as a numpy array list.
First the total prediction then the estimation of the cosmic off beam contamination, then the dirt contribution, then the beam realted background and finally the smeared signal distribution.


### eventrate_comparison(h_data_func,h_true_func,this_pot,this_frac_tot, filename,model_name)
Takes the data histogram, the true event rate for MicroBooNE of a model as well as the simulated POT, the total fractional covariance as well as 2 strings for fliename (outputfile) and model name (for legend).
It returns nothing but put an output histogram in the output directory.

### my_chi2(h_data, h_true_func,this_pot, frac)
Takes the data histogram, the true event rate for MicroBooNE of a model as well as the simulated POT and the total fractional covariance. 
It returns the chisquare value between the data and the prediction including the uncertainties.

### chi2_minus1(h_data, h_true_func,this_pot, frac)
Takes the data histogram, the true event rate for MicroBooNE of a model as well as the simulated POT and the total fractional covariance. 
It returns a numpy array with the chi square values when bin i is neglected.