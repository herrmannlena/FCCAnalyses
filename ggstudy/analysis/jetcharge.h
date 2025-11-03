// JetUtils.h
#pragma once
#include "FCCAnalyses/JetConstituentsUtils.h"
#include "edm4hep/ReconstructedParticleData.h"
#include "ROOT/RVec.hxx"
#include <cmath>


namespace JetUtils {

/// Jet charge Q_kappa = sum_i q_i * (pt_i)^kappa / (pt_jet)^kappa
/// Uses jet constituents (per-jet arrays of edm4hep::ReconstructedParticleData).
struct jet_charge {
    float m_kappa;
    jet_charge(float kappa);
    ROOT::VecOps::RVec<float> operator()(const ROOT::VecOps::RVec<fastjet::PseudoJet>& jets,const ROOT::VecOps::RVec<ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData>>& jcs, const vector<vector<int>> &indices,
                                        const ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData>& recopart, 
                                        const ROOT::VecOps::RVec< edm4hep::TrackState>& track);
};

jet_charge::jet_charge(float kappa) : m_kappa(kappa) {};
ROOT::VecOps::RVec<float> jet_charge::jet_charge::operator()(const ROOT::VecOps::RVec<fastjet::PseudoJet>& jets,
              const ROOT::VecOps::RVec<ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData>>& jcs,
              const vector<vector<int>>& indices,
              const ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData>& recopart,
              const ROOT::VecOps::RVec< edm4hep::TrackState>& track)
  {
    using rvf = ROOT::VecOps::RVec<float>;
    const auto nJ = jets.size();
    rvf out(nJ, 0.f);

    ROOT::VecOps::RVec<bool> rp_hasTRK = FCCAnalyses::ReconstructedParticle2Track::hasTRK(recopart); //has the reconstructed particle a track?
    ROOT::VecOps::RVec<edm4hep::TrackState> tracks = FCCAnalyses::ReconstructedParticle2Track::getRP2TRK(recopart, track); //get the tracks
    ROOT::VecOps::RVec<float> trk_q = FCCAnalyses::ReconstructedParticle2Track::getRP2TRK_charge(recopart, track); //get trk charge
    ROOT::VecOps::RVec<float> trk_mom = FCCAnalyses::ReconstructedParticle2Track::getRP2TRK_mom(recopart, track); //get trk p
    ROOT::VecOps::RVec<float> trk_tanlam = FCCAnalyses::ReconstructedParticle2Track::getRP2TRK_tanLambda(recopart, track); //get trk tan lam

   
    ROOT::VecOps::RVec<ROOT::VecOps::RVec<float>> TrkCharges(nJ);
    ROOT::VecOps::RVec<ROOT::VecOps::RVec<float>> Trkpt(nJ);
    //loop over jets
    for (size_t j=0; j < nJ; ++j){
      for (int i=0; i < indices[j].size(); ++i){
        if (rp_hasTRK[indices[j][i]]) {
          TrkCharges[j].push_back(trk_q[indices[j][i]]);
          float pt = trk_mom[indices[j][i]]/std::sqrt(1+std::pow(trk_tanlam[indices[j][i]],2));
          Trkpt[j].push_back(pt);
        }
      }
    }

    // per-jet constituent pt and charge (shape: nJ × nConst_jet)
    //const auto c_pt  = FCCAnalyses::JetConstituentsUtils::get_pt(jcs);     // RVec<RVec<float>>
    //const auto c_q   = FCCAnalyses::JetConstituentsUtils::get_charge(jcs); // RVec<RVec<float>>

    const auto jets_p4 = FCCAnalyses::JetConstituentsUtils::compute_tlv_jets(jets);
    
    for (size_t j = 0; j < nJ; ++j) {
      const float ptj = std::hypot(jets_p4[j].Px(), jets_p4[j].Py()); // pt(jet) from edm4hep 3-vector
      if (!(ptj > 0)) { out[j] = 0.f; continue; }
      
      const double denom = std::pow(static_cast<double>(ptj), static_cast<double>(m_kappa));
      const auto& vpt = Trkpt[j];
      const auto& vq  = TrkCharges[j];

      double num = 0.0;
      const size_t nC = std::min(vpt.size(), vq.size());

      for (size_t i = 0; i < nC; ++i) {
        const double w = std::pow(static_cast<double>(vpt[i]), static_cast<double>(m_kappa));
        num += static_cast<double>(vq[i]) * w;
      }
      out[j] = static_cast<float>(num / denom); 
    } 

    return out;
  }

float get_charge_i(int index, ROOT::VecOps::RVec<float> jet_charges){
    return jet_charges[index];
}

float return_abs_sum(float charge0, float charge1){
  return std::fabs(charge0)+std::fabs(charge1);
}


};



