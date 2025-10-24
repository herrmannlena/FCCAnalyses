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
    ROOT::VecOps::RVec<float> operator()(const ROOT::VecOps::RVec<fastjet::PseudoJet>& jets,const ROOT::VecOps::RVec<ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData>>& jcs);
};

jet_charge::jet_charge(float kappa) : m_kappa(kappa) {};
ROOT::VecOps::RVec<float> jet_charge::jet_charge::operator()(const ROOT::VecOps::RVec<fastjet::PseudoJet>& jets,
             const ROOT::VecOps::RVec<ROOT::VecOps::RVec<edm4hep::ReconstructedParticleData>>& jcs) 
  {
    using rvf = ROOT::VecOps::RVec<float>;
    const auto nJ = jets.size();
    rvf out(nJ, 0.f);
     
    // per-jet constituent pt and charge (shape: nJ × nConst_jet)
    const auto c_pt  = FCCAnalyses::JetConstituentsUtils::get_pt(jcs);     // RVec<RVec<float>>
    const auto c_q   = FCCAnalyses::JetConstituentsUtils::get_charge(jcs); // RVec<RVec<float>>

    const auto jets_p4 = FCCAnalyses::JetConstituentsUtils::compute_tlv_jets(jets);
    
    for (size_t j = 0; j < nJ; ++j) {
      const float ptj = std::hypot(jets_p4[j].Px(), jets_p4[j].Py()); // pt(jet) from edm4hep 3-vector
      if (!(ptj > 0)) { out[j] = 0.f; continue; }
      
      const double denom = std::pow(static_cast<double>(ptj), static_cast<double>(m_kappa));
      const auto& vpt = c_pt[j];
      const auto& vq  = c_q[j];

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


};



