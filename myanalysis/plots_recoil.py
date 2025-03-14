import ROOT

# global parameters
intLumi        = 1.
intLumiLabel   = "L = 10.8 ab^{-1}"
ana_tex        = 'e^{+}e^{-} #rightarrow AH'
delphesVersion = '3.4.2'
energy         = 240.0
collider       = 'FCC-ee'
formats        = ['png','pdf']

outdir         = './outputs/plots/recoil/' 
inputDir       = './outputs/histmaker/recoil/' 

plotStatUnc    = True

colors = {}
colors['AH'] = ROOT.kRed
colors['Acc'] = ROOT.kBlue+1
colors['Aqq'] = ROOT.kGreen+2

#procs = {}
#procs['signal'] = {'ZH':['wzp6_ee_mumuH_ecm240']}
#procs['backgrounds'] =  {'WW':['p8_ee_WW_ecm240'], 'ZZ':['p8_ee_ZZ_ecm240']}
procs = {}
procs['signal'] = {'AH':['p8_ee_Hgamma_ecm240']}
#procs['backgrounds'] =  {'WW':['p8_ee_WW_mumu_ecm240'], 'ZZ':['p8_ee_ZZ_mumubb_ecm240']}
procs['backgrounds'] =  {'Aqq':['p8_ee_qqgamma_ecm240'], 'Acc':['p8_ee_ccgamma_ecm240']}


legend = {}
legend['AH'] = 'AH'
legend['Aqq'] = 'Aqq'
legend['Acc'] = 'Acc'



hists = {}
hists2D = {}




hists["cutFlow"] = {
    "input":   "cutFlow",
    "output":   "cutFlow",
    "logy":     True,
    "stack":    True,
    "xmin":     0,
    "xmax":     6,
    "ymin":     1e4,
    "ymax":     1e11,
    "xtitle":   ["All events", "p(#gamma) > 50 GeV", "other", "other", "other", "other"],
    "ytitle":   "Events ",
    "scaleSig": 1
}

hists["gamma_recoil_m"] = {
    "input":   "gamma_recoil_m",
    "output":   "gamma_recoil_m",
    "logy":     False,
    "stack":    True,
    "xmin":     80,
    "xmax":     150,
    "xtitle":   "Recoil (GeV)",
    "ytitle":   "Events ",
    "scaleSig": 1000

}

hists["photons_p_cut_0"] = {
    "input":   "photons_p_cut_0",
    "output":   "photons_p_cut_0",
    "logy":     False,
    "stack":    True,
    "xmin":     0,
    "xmax":     100,
    "xtitle":   "photons_p_cut_0",
    "ytitle":   "Events ",
    "processes": ['AH','Aff'],
    "density": False,
}

"""
hists["photons_p_cut_1"] = {
    "input":   "photons_p_cut_1",
    "output":   "photons_p_cut_1",
    "logy":     False,
    "stack":    True,
    "xmin":     0,
    "xmax":     100,
    "xtitle":   "photons_p_cut_1",
    "ytitle":   "Events ",
    "processes": ['AH','Aff'],
    "density": False,
}
"""
hists["photons_n_cut_0"] = {
    "input":   "photons_n_cut_0",
    "output":   "photons_n_cut_0",
    "logy":     False,
    "stack":    True,
    "xmin":     0,
    "xmax":     10,
    "xtitle":   "photons_n_cut_0",
    "ytitle":   "Events ",
}

hists["photons_cos_theta_cut_0"] = {
    "input":   "photons_cos_theta_cut_0",
    "output":   "photons_cos_theta_cut_0",
    "logy":     False,
    "stack":    True,
    "xmin":     -1,
    "xmax":     1,
    "xtitle":   "photons_cos_theta_cut_0",
    "ytitle":   "Events ",
}
"""
hists["photons_n_cut_1"] = {
    "input":   "photons_n_cut_1",
    "output":   "photons_n_cut_1",
    "logy":     False,
    "stack":    True,
    "xmin":     0,
    "xmax":     10,
    "xtitle":   "photons_n_cut_1",
    "ytitle":   "Events ",
}
"""
"""
hists["photons_boosted_p"] = {
    "input":   "photons_boosted_p",
    "output":   "photons_boosted_p",
    "logy":     False,
    "stack":    True,
    "xmin":     0,
    "xmax":     100,
    "xtitle":   "photons_boosted_p",
    "ytitle":   "Events ",
}



hists["photons_boosted_n"] = {
    "input":   "photons_boosted_n",
    "output":   "photons_boosted_n",
    "logy":     False,
    "stack":    True,
    "xmin":     0,
    "xmax":     10,
    "xtitle":   "photons_boosted_n",
    "ytitle":   "Events ",
}
"""


"""



hists["zmumu_recoil_m"] = {
    "output":   "zmumu_recoil_m",
    "logy":     False,
    "stack":    True,
    "rebin":    100,
    "xmin":     120,
    "xmax":     140,
    "ymin":     0,
    "ymax":     2500,
    "xtitle":   "Recoil (GeV)",
    "ytitle":   "Events / 100 MeV",
}

hists["zmumu_p"] = {
    "output":   "zmumu_p",
    "logy":     False,
    "stack":    True,
    "rebin":    2,
    "xmin":     0,
    "xmax":     80,
    "ymin":     0,
    "ymax":     2000,
    "xtitle":   "p(#mu^{#plus}#mu^{#minus}) (GeV)",
    "ytitle":   "Events ",
}

hists["zmumu_m"] = {
    "output":   "zmumu_m",
    "logy":     False,
    "stack":    True,
    "rebin":    2,
    "xmin":     86,
    "xmax":     96,
    "ymin":     0,
    "ymax":     3000,
    "xtitle":   "m(#mu^{#plus}#mu^{#minus}) (GeV)",
    "ytitle":   "Events ",
}"""