# list of processes (mandatory)
processList = {
    'p8_ee_Hgamma_ecm240':    {'fraction':1, 'crossSection': 8.20481e-05}, 
    #'p8_ee_Hgamma_ecm240':    {'fraction':1}, 
    'p8_ee_qqgamma_ecm240':    {'fraction':1, 'crossSection': 6.9},  #what are the exact values here?
    'p8_ee_ccgamma_ecm240':    {'fraction':1, 'crossSection': 2.15},  #what are the exact values here?
    #'p8_ee_ffgamma_ecm240':    {'fraction':1, 'crossSection': 0.7},
    #'p8_ee_WW_mumu_ecm240':    {'fraction':1, 'crossSection': 0.25792}, 
    #'p8_ee_ZZ_mumubb_ecm240':  {'fraction':1, 'crossSection': 2 * 1.35899 * 0.034 * 0.152},
    #'p8_ee_ZH_Zmumu_ecm240':   {'fraction':1, 'crossSection': 0.201868 * 0.034},
}

ecm= 240
# Production tag when running over EDM4Hep centrally produced events, this points to the yaml files for getting sample statistics (mandatory)
#prodTag     = "FCCee/winter2023/IDEA/"

# Link to the dictonary that contains all the cross section informations etc... (mandatory)
procDict = "FCCee_procDict_winter2023_IDEA.json"

# additional/custom C++ functions, defined in header files (optional)
includePaths = ["../tutorial/functions.h"]

# Define the input dir (optional)
#inputDir    = "outputs/FCCee/higgs/mH-recoil/mumu/stage1"
inputDir    = "/afs/cern.ch/work/l/lherrman/private/HiggsGamma/data"

#Optional: output directory, default is local running directory
outputDir   = "/afs/cern.ch/work/l/lherrman/private/HiggsGamma/analysis/FCCAnalyses/myanalysis/outputs/histmaker/recoil/"


# optional: ncpus, default is 4, -1 uses all cores available
nCPUS       = -1

# scale the histograms with the cross-section and integrated luminosity
doScale = True
intLumi = 10800000  # 10.8 /ab


# define some binning for various histograms
bins_a_p = (100, 0, 500) # 100 MeV bins
bins_a_n = (10, 0, 10) # 100 MeV bins

bins_count = (10, 0, 10)


##?| name of collections in EDM root files
collections = {
    "GenParticles": "Particle",
    "PFParticles": "ReconstructedParticles",
    "PFTracks": "EFlowTrack",
    "PFPhotons": "EFlowPhoton",
    "PFNeutralHadrons": "EFlowNeutralHadron",
    # "TrackState": "EFlowTrack_1",
    "TrackState": "_EFlowTrack_trackStates",
    "TrackerHits": "TrackerHits",
    "CalorimeterHits": "CalorimeterHits",
    # "dNdx": "EFlowTrack_2",
    "dNdx": "_EFlowTrack_dxQuantities",
    "PathLength": "EFlowTrack_L",
    "Bz": "magFieldBz",
    "Electrons": "Electron",
    "Muons": "Muon",
}

# build_graph function that contains the analysis logic, cuts and histograms (mandatory)
def build_graph(df, dataset):

    results = []
    df = df.Define("weight", "1.0")
    weightsum = df.Sum("weight")
    

    df = df.Alias("Photon0", "Photon#0.index")
    df = df.Define(
            "photons_all",
            "FCCAnalyses::ReconstructedParticle::get(Photon0, ReconstructedParticles)",
        )


    df = df.Define("photons_p", "FCCAnalyses::ReconstructedParticle::get_p(photons_all)") 
    df = df.Define("photons_n","FCCAnalyses::ReconstructedParticle::get_n(photons_all)")  #number of photons per event
    df = df.Define("photons_cos_theta","cos(FCCAnalyses::ReconstructedParticle::get_theta(photons_all))")

    #first isolate, sort in pt, take first, (hole pt von isolate..), cut ist dann die laenge von der selection


    #########
    ### CUT 0: all events
    #########
    df = df.Define("cut0", "0")
    results.append(df.Histo1D(("cutFlow", "", *bins_count), "cut0"))


    #Baseline selection
    results.append(df.Histo1D(("photons_p_cut_0", "", 100, 0, 100), "photons_p"))
    results.append(df.Histo1D(("photons_n_cut_0", "", *bins_a_n), "photons_n"))
    results.append(df.Histo1D(("photons_cos_theta_cut_0", "", 50, -1, 1), "photons_cos_theta"))
    
    #energy cut
    df = df.Define("photons_boosted", "FCCAnalyses::ReconstructedParticle::sel_p(50)(photons_all)")


    df = df.Define("photons_boosted_p", "FCCAnalyses::ReconstructedParticle::get_p(photons_boosted)") # is this correct?
    df = df.Define("photons_boosted_n","FCCAnalyses::ReconstructedParticle::get_n(photons_boosted)") 
    df = df.Define("photons_boosted_cos_theta","cos(FCCAnalyses::ReconstructedParticle::get_theta(photons_boosted))")

    results.append(df.Histo1D(("photons_cos_theta_cut_1", "", 50, -1, 1), "photons_boosted_cos_theta"))

       
   # select the highest energetic photon!

    

    #isolation cut
    #df = df.Define(
     #       "photons_iso",
     #       "FCCAnalyses::ZHfunctions::coneIsolation(0.01, 0.5)(photons_boosted, ReconstructedParticles)",
     #   )  # is this correct?
   # df = df.Define(
   #         "photons_sel_iso",
   #         "FCCAnalyses::ZHfunctions::sel_iso(0.25)(photons, photons_iso)",
    #    )

    #df = df.Define("isophotons_no", "photons_sel_iso.size()")

    df = df.Define(
            "missingEnergy",
            f"FCCAnalyses::ZHfunctions::missingEnergy({ecm}., ReconstructedParticles)",
        )
    
    
    #variables to later cut on
   
   
    



    #df = df.Define("photons_print", "FCCAnalyses::ZHfunctions::print_momentum(photons_all)")
    #results.append(df.Histo1D(("photons_print", "", 100, 0, 100), "photons_print"))
   
   
    

    """
     #########
    ### CUT 1: Photons must have momentum larger 50 GeV
    #########
    
    df = df.Filter("photons_p>50")  
    df = df.Define("cut1", "1")
    results.append(df.Histo1D(("cutFlow", "", *bins_count), "cut1"))
    
    results.append(df.Histo1D(("photons_p_cut_1", "", 100, 0, 100), "photons_p"))
    results.append(df.Histo1D(("photons_n_cut_1", "", *bins_a_n), "photons_n"))
    """
 
   
    # isolated photon

    

    # recoil plot
    df = df.Define("gamma_recoil", "FCCAnalyses::ReconstructedParticle::recoilBuilder(240)(photons_boosted)") # do I need here already the first element?? check...
    df = df.Define("gamma_recoil_m", "FCCAnalyses::ReconstructedParticle::get_mass(gamma_recoil)[0]") # recoil mass
    results.append(df.Histo1D(("gamma_recoil_m", "", 70, 80, 150), "gamma_recoil_m"))

    #define further variables for plotting
    #df = df.Define("photons_all_p", "FCCAnalyses::ReconstructedParticle::get_p(photons_all)")
    #df = df.Define("photons_boosted_p", "FCCAnalyses::ReconstructedParticle::get_p(photons_boosted)")
    #df = df.Define("photons_boosted_n","FCCAnalyses::ReconstructedParticle::get_n(photons_boosted)")  #number of photons per event
    
   
    #select highest energetic photon

    ########################
    # Final histograms
    ########################
    #results.append(df.Histo1D(("photons_all_p", "", 100, 0, 100), "photons_all_p"))
   # results.append(df.Histo1D(("photons_boosted_p", "", *bins_a_p), "photons_boosted_p"))
    #results.append(df.Histo1D(("photons_n", "", *bins_a_n), "photons_n"))
    #results.append(df.Histo1D(("photons_boosted_n", "", *bins_a_n), "photons_boosted_n"))
    
    #results.append(df.Histo1D(("zmumu_recoil_m", "", *bins_recoil), "zmumu_recoil_m"))   # see how recoil determined
   
    #need to select the highest energetic photon

    return results, weightsum


