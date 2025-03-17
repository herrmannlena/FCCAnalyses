import ROOT

# global parameters
intLumi        = 1.
intLumiLabel   = "L = 10.8 ab^{-1}"
ana_tex        = 'e^{+}e^{-} #rightarrow AH'
delphesVersion = '3.4.2'
energy         = 240.0
collider       = 'FCC-ee'
formats        = ['png','pdf']

outdir         = './outputsl/plots/recoil/' 
inputDir       = './outputsl/histmaker/recoil/' 

plotStatUnc    = True

colors = {}
colors['AH'] = ROOT.kRed
colors['Acc'] = ROOT.kBlue+1
colors['Aqq'] = ROOT.kGreen+2
colors['Abb'] = ROOT.kYellow+3
colors['WW'] = ROOT.kCyan
colors['ZZ'] = ROOT.kAzure-9
colors['Aee'] = ROOT.kViolet+3
colors['Atautau'] = ROOT.kOrange
colors['Amumu'] = ROOT.kMagenta

#procs = {}
#procs['signal'] = {'ZH':['wzp6_ee_mumuH_ecm240']}
#procs['backgrounds'] =  {'WW':['p8_ee_WW_ecm240'], 'ZZ':['p8_ee_ZZ_ecm240']}
procs = {}
procs['signal'] = {'AH':['p8_ee_Hgamma_ecm240']}
#procs['backgrounds'] =  {'WW':['p8_ee_WW_mumu_ecm240'], 'ZZ':['p8_ee_ZZ_mumubb_ecm240']}
procs['backgrounds'] =  {'Aqq':['p8_ee_qqgamma_ecm240'], 'Acc':['p8_ee_ccgamma_ecm240'], 'Abb':['p8_ee_bbgamma_ecm240'], 'Atautau':['p8_ee_tautaugamma_ecm240'], 'Amumu':['p8_ee_mumugamma_ecm240'], 'WW':['p8_ee_WW_ecm240'], 'ZZ':['p8_ee_ZZ_ecm240'], 'Aee':['p8_ee_eegamma_ecm240']}

legend = {}
legend['AH'] = 'AH'
legend['Aqq'] = 'Aqq'
legend['Acc'] = 'Acc'
legend['Abb'] = 'Abb'
legend['WW'] = 'WW'
legend['ZZ'] = 'ZZ'
legend['Aee'] = 'Aee'
legend['Atautau'] = 'Atautau'
legend['Amumu'] = 'Amumu'


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
    "xtitle":   ["All events", "isolation", "60 GeV < p(#gamma) < 100 GeV", "|cos(#theta)|<0.9", "cut ee", "110 GeV < m_recoil < 140 GeV", "123.5 GeV < m_recoil < 126.5 GeV"],
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
    "scaleSig": 1000,
    "density": False

}

hists["gamma_recoil_m_norm"] = {
    "input":   "gamma_recoil_m",
    "output":   "gamma_recoil_m_norm",
    "logy":     False,
    "stack":    False,
    "xmin":     80,
    "xmax":     150,
    "xtitle":   "Recoil (GeV)",
    "ytitle":   "Events ",
   # "scaleSig": 1000,
    "density": True

}

hists["gamma_recoil_m_signal_cut"] = {
    "input":   "gamma_recoil_m_signal_cut",
    "output":   "gamma_recoil_m_signal_cut",
    "logy":     False,
    "stack":    True,
    "xmin":     80,
    "xmax":     150,
    "xtitle":   "Recoil (GeV)",
    "ytitle":   "Events ",
    "scaleSig": 1000,
    "density": False

}

hists["gamma_recoil_m_tight_cut"] = {
    "input":   "gamma_recoil_m_tight_cut",
    "output":   "gamma_recoil_m_tight_cut",
    "logy":     False,
    "stack":    True,
    "xmin":     80,
    "xmax":     150,
    "xtitle":   "Recoil (GeV)",
    "ytitle":   "Events ",
    "scaleSig": 1000,
    "density": False

}

hists["electrons_p_baseline"] = {
    "input":   "electrons_p_baseline",
    "output":   "electrons_p_baseline",
    "logy":     False,
    "stack":    False,
    "xmin":     0,
    "xmax":     130,
    "xtitle":   "electrons_p_baseline",
    "ytitle":   "Events ",
    "density": False,
    "density": True
}


hists["photons_p_cut_0"] = {
    "input":   "photons_p_cut_0",
    "output":   "photons_p_cut_0",
    "logy":     False,
    "stack":    True,
    "xmin":     0,
    "xmax":     130,
    "xtitle":   "photons_p_cut_0",
    "ytitle":   "Events ",
    "density": False,
    "scaleSig": 1000,
    "density": True
}


hists["photons_p_cut_1"] = {
    "input":   "photons_p_cut_1",
    "output":   "photons_p_cut_1",
    "logy":     False,
    "stack":    True,
    "xmin":     0,
    "xmax":     130,
    "xtitle":   "photons_p_cut_1",
    "ytitle":   "Events ",
    "density": False,
    "scaleSig": 1000,
    "density": True
}

hists["photons_p_cut_2"] = {
    "input":   "photons_p_cut_2",
    "output":   "photons_p_cut_2",
    "logy":     False,
    "stack":    True,
    "xmin":     0,
    "xmax":     130,
    "xtitle":   "photons_p_cut_2",
    "ytitle":   "Events ",
    "density": False,
    "scaleSig": 1000,
    "density": True
}

hists["photons_p_cut_3"] = {
    "input":   "photons_p_cut_3",
    "output":   "photons_p_cut_3",
    "logy":     False,
    "stack":    True,
    "xmin":     0,
    "xmax":     130,
    "xtitle":   "photons_p_cut_3",
    "ytitle":   "Events ",
    "density": False,
    "scaleSig": 1000,
    "density": True
}

hists["photons_p_cut_4"] = {
    "input":   "photons_p_cut_4",
    "output":   "photons_p_cut_4",
    "logy":     False,
    "stack":    True,
    "xmin":     0,
    "xmax":     130,
    "xtitle":   "photons_p_cut_4",
    "ytitle":   "Events ",
    "density": False,
    "scaleSig": 1000,
    "density": True
}

hists["electrons_n_baseline"] = {
    "input":   "electrons_n_baseline",
    "output":   "electrons_n_baseline",
    "logy":     False,
    "stack":    False,
    "xmin":     0,
    "xmax":     10,
    "xtitle":   "electrons_n_baseline",
    "ytitle":   "Events ",
    "density": True
}

hists["photons_n_cut_0"] = {
    "input":   "photons_n_cut_0",
    "output":   "photons_n_cut_0",
    "logy":     False,
    "stack":    True,
    "xmin":     0,
    "xmax":     10,
    "xtitle":   "photons_n_cut_0",
    "ytitle":   "Events ",
    "density": True
}

hists["photons_n_cut_1"] = {
    "input":   "photons_n_cut_1",
    "output":   "photons_n_cut_1",
    "logy":     False,
    "stack":    True,
    "xmin":     0,
    "xmax":     10,
    "xtitle":   "photons_n_cut_1",
    "ytitle":   "Events ",
    "density": True
}

hists["photons_n_cut_2"] = {
    "input":   "photons_n_cut_2",
    "output":   "photons_n_cut_2",
    "logy":     False,
    "stack":    True,
    "xmin":     0,
    "xmax":     10,
    "xtitle":   "photons_n_cut_2",
    "ytitle":   "Events ",
    "density": True
}

hists["photons_n_cut_3"] = {
    "input":   "photons_n_cut_3",
    "output":   "photons_n_cut_3",
    "logy":     False,
    "stack":    True,
    "xmin":     0,
    "xmax":     10,
    "xtitle":   "photons_n_cut_3",
    "ytitle":   "Events ",
    "density": True
}

hists["photons_n_cut_4"] = {
    "input":   "photons_n_cut_4",
    "output":   "photons_n_cut_4",
    "logy":     False,
    "stack":    True,
    "xmin":     0,
    "xmax":     10,
    "xtitle":   "photons_n_cut_4",
    "ytitle":   "Events ",
    "density": True
}

hists["electrons_cos_theta"] = {
    "input":   "electrons_cos_theta",
    "output":   "electrons_cos_theta",
    "logy":     False,
    "stack":    True,
    "xmin":     -1,
    "xmax":     1,
    "xtitle":   "electrons_cos_theta",
    "ytitle":   "Events ",
     "scaleSig": 10000,
     "density": False
}

hists["electrons_cos_theta_cut_1"] = {
    "input":   "electrons_cos_theta_cut_1",
    "output":   "electrons_cos_theta_cut_1",
    "logy":     False,
    "stack":    True,
    "xmin":     -1,
    "xmax":     1,
    "xtitle":   "electrons_cos_theta_cut_1",
    "ytitle":   "Events ",
     "scaleSig": 10000,
     "density": False
}

hists["electrons_cos_theta_cut_2"] = {
    "input":   "electrons_cos_theta_cut_2",
    "output":   "electrons_cos_theta_cut_2",
    "logy":     False,
    "stack":    True,
    "xmin":     -1,
    "xmax":     1,
    "xtitle":   "electrons_cos_theta_cut_2",
    "ytitle":   "Events ",
     "scaleSig": 10000,
     "density": False
}



hists["electrons_cos_theta_cut_3"] = {
    "input":   "electrons_cos_theta_cut_3",
    "output":   "electrons_cos_theta_cut_3",
    "logy":     False,
    "stack":    True,
    "xmin":     -1,
    "xmax":     1,
    "xtitle":   "electrons_cos_theta_cut_3",
    "ytitle":   "Events ",
     "scaleSig": 10000,
     "density": False
}

hists["electrons_cos_theta_cut_4"] = {
    "input":   "electrons_cos_theta_cut_4",
    "output":   "electrons_cos_theta_cut_4",
    "logy":     False,
    "stack":    True,
    "xmin":     -1,
    "xmax":     1,
    "xtitle":   "electrons_cos_theta_cut_4",
    "ytitle":   "Events ",
     "scaleSig": 10000,
     "density": False
}

hists["photons_cos_theta_cut_0"] = {
    "input":   "photons_cos_theta_cut_0",
    "output":   "photons_cos_theta_cut_0",
    "logy":     False,
    "stack":    False,
    "xmin":     -1,
    "xmax":     1,
    "xtitle":   "photons_cos_theta_cut_0",
    "ytitle":   "Events ",
     "scaleSig": 10000,
     "density": True
}



hists["photons_cos_theta_cut_1"] = {
    "input":   "photons_cos_theta_cut_1",
    "output":   "photons_cos_theta_cut_1",
    "logy":     False,
    "stack":    False,
    "xmin":     -1,
    "xmax":     1,
    "xtitle":   "photons_cos_theta_cut_1",
    "ytitle":   "Events ",
     "scaleSig": 10000,
     "density": True
}

hists["photons_cos_theta_cut_2"] = {
    "input":   "photons_cos_theta_cut_2",
    "output":   "photons_cos_theta_cut_2",
    "logy":     False,
    "stack":    False,
    "xmin":     -1,
    "xmax":     1,
    "xtitle":   "photons_cos_theta_cut_2",
    "ytitle":   "Events ",
     "scaleSig": 10000,
     "density": True
}


hists["photons_cos_theta_cut_3"] = {
    "input":   "photons_cos_theta_cut_3",
    "output":   "photons_cos_theta_cut_3",
    "logy":     False,
    "stack":    False,
    "xmin":     -1,
    "xmax":     1,
    "xtitle":   "photons_cos_theta_cut_3",
    "ytitle":   "Events ",
     "scaleSig": 10000,
     "density": True
}

hists["photons_cos_theta_cut_4"] = {
    "input":   "photons_cos_theta_cut_4",
    "output":   "photons_cos_theta_cut_4",
    "logy":     False,
    "stack":    False,
    "xmin":     -1,
    "xmax":     1,
    "xtitle":   "photons_cos_theta_cut_4",
    "ytitle":   "Events ",
     "scaleSig": 10000,
     "density": True
}

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
    "density": True
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