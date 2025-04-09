import ROOT

# global parameters
intLumi        = 1.
intLumiLabel   = "L = 10.8 ab^{-1}"
ana_tex        = 'e^{+}e^{-} #rightarrow #gamma H'
delphesVersion = '3.4.2'
energy         = 240.0
collider       = 'FCC-ee'
formats        = ['png','pdf']

outdir         = './outputstest/plots/recoil/' 
inputDir       = './outputstest/histmaker/recoil/' 

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
procs['backgrounds'] =  {'Aqq':['p8_ee_qqgamma_ecm240'], 'Acc':['p8_ee_ccgamma_ecm240'], 'Abb':['p8_ee_bbgamma_ecm240'], 'Atautau':['p8_ee_tautaugamma_ecm240'], 'Amumu':['p8_ee_mumugamma_ecm240'], 'Aee':['p8_ee_eegamma_ecm240'], 'WW':['p8_ee_WW_ecm240'], 'ZZ':['p8_ee_ZZ_ecm240']}

legend = {}
legend['AH'] = '#gamma H'
legend['Aqq'] = '#gamma q#bar{q}'
legend['Acc'] = '#gamma c#bar{c}'
legend['Abb'] = '#gamma b#bar{b}'
legend['WW'] = 'WW'
legend['ZZ'] = 'ZZ'
legend['Aee'] = '#gamma e^{+} e^{-}'
legend['Atautau'] = '#gamma #tau^{+} #tau^{-}'
legend['Amumu'] = '#gamma #mu^{+} #mu^{-}'


hists = {}
hists2D = {}





hists["cutFlow"] = {
    "input":   "cutFlow",
    "output":   "cutFlow",
    "logy":     True,
    "stack":   True,
    "xmin":     0,
    "xmax":     6,
    "ymin":     1e4,
    "ymax":     1e11,
    "xtitle":   ["All events", "iso < 0.2", "60  < p_{#gamma} < 100 ", "|cos(#theta)_{#gamma}|<0.9", "n particles > 5", "110 < m_{recoil} < 140 ", "123.5  < m_{recoil} < 126.5 "],
    "ytitle":   "Events ",
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
    "density": True,
}
