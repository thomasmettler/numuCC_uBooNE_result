#import stuff you eventually need
import numpy as np
import pandas as pd
import os
import ROOT
import time
import math
from array import array

import imp
CC = imp.load_source('CC_inclusive_2D_lib','CC_inclusive_2D_lib.py')


inputdir = '' # please give here path to inputfile
outputdir = inputdir+'plots/' 
# make output dir if not existing
try:
    os.stat(outputdir)
except:
    os.mkdir(outputdir)
RootFile = ROOT.TFile(outputdir+"result_histo.root","RECREATE");


f = ROOT.TFile.Open(inputdir+'FF_detsys.root', 'read')


ROOT.gStyle.SetOptStat(0)
ROOT.gStyle.SetOptTitle(0)
c1 = ROOT.TCanvas("c1","c1",1600,1200)
c1.SetGrid(1)
c1.SetLeftMargin(0.14)
c1.SetRightMargin(0.1)
c1.SetBottomMargin(0.14)

h_true = f.Get('h_gen_cv')
'''
frac_det = CC.return_detsys_covar(h_true,2.144e+20)
frac_other = CC.return_other_covar(h_true,2.144e+20)
frac_det_all,bkg_all = CC.return_all_covar(h_true,2.144e+20)
frac_det_flux = CC.return_flux_covar(h_true,2.144e+20)
frac_crt = CC.return_crt_covar(h_true,2.144e+20)
frac_dirt = CC.return_dirt_covar(h_true,2.144e+20)
frac_stat = CC.return_stat_covar(h_true,2.144e+20)

np.save(outputdir+'frac_det',frac_det)
np.save(outputdir+'frac_other',frac_other)
np.save(outputdir+'frac_det_all',frac_det_all)
np.save(outputdir+'bkg_all',bkg_all)
np.save(outputdir+'frac_det_flux',frac_det_flux)
np.save(outputdir+'frac_crt',frac_crt)
np.save(outputdir+'frac_dirt',frac_dirt)
np.save(outputdir+'frac_stat',frac_stat)
'''
frac_det = np.load(outputdir+'frac_det.npy')
frac_other = np.load(outputdir+'frac_other.npy')
frac_det_all = np.load(outputdir+'frac_det_all.npy')
#bkg_all = np.load(outputdir+'bkg_all.npy')
frac_det_flux = np.load(outputdir+'frac_det_flux.npy')
frac_crt = np.load(outputdir+'frac_crt.npy')
frac_dirt = np.load(outputdir+'frac_dirt.npy')
frac_stat = np.load(outputdir+'frac_stat.npy')

frac_tot = frac_det+frac_other+frac_det_all+frac_det_flux+frac_crt+frac_dirt+frac_stat

h_frac = CC.plot_err_array(frac_tot)
h_frac.Draw()
h_histo = CC.histBkg(h_frac)
h_histo.Draw('hist same')
c1.Draw()

h_true = f.Get('h_gen_cv')  # load true histogram (Genie V3 uB tune)
h_data = f.Get('h_data') # load data historgram

# calculate chi2 between smeared model + bkg and data
chi2 = CC.my_chi2(h_data, h_true,2.144e+20,frac_tot)
print chi2

# calculates chi when bin n is neglected
chi2_nMinus1 = CC.chi2_minus1(h_data, h_true,2.144e+20,frac_tot)
print chi2_nMinus1
print chi2_nMinus1.size

# makes event rate plot and stores in plot out put folder
CC.eventrate_comparison(h_data,h_true,2.144e+20,frac_tot, 'EventRate_G3uB','G3 uB')

















