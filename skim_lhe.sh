#!/bin/bash

#baseInputDir=/home/lucien/AnalysisCode/Higgs/ALP/genproductions/bin/MadGraph5_aMCatNLO/workDir_acc_study_hTOalpalp_eps2e-2_mZd
#baseInputDir=/home/lucien/AnalysisCode/Higgs/ALP/genproductions/bin/MadGraph5_aMCatNLO/workDir_acc_study_hTOzpzpTO4e_eps2e-2_mZd
#baseInputDir=/home/lucien/AnalysisCode/Higgs/ALP/genproductions/bin/MadGraph5_aMCatNLO/workDir_acc_study_hTOalpalpTOmumu_eps2e-2_mZd
baseInputDir=/home/lucien/AnalysisCode/Higgs/ALP/genproductions/bin/MadGraph5_aMCatNLO/workDir_acc_study_hTOzpzpTO4mu_eps2e-2_mZd
for m in 4 7 15 20 25 30 33 ; 
do
    #root -l -q ZZD_lhe.C\(\"${baseInputDir}${m}/UnpackTarball/cmsgrid_final.lhe\",\"${baseInputDir}${m}/UnpackTarball/cmsgrid_final_lhe.root\",10000\) ; 
    root -l -q ZDZD_lhe.C\(\"${baseInputDir}${m}/UnpackTarball/cmsgrid_final.lhe\",\"${baseInputDir}${m}/UnpackTarball/cmsgrid_final_lhe.root\",10000\) ; 
done
