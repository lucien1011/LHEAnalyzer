#!/bin/bash

#baseInputDir=/home/lucien/AnalysisCode/Higgs/ALP/genproductions/bin/MadGraph5_aMCatNLO/workDir_acc_study_hTOalpalp_eps2e-2_mZd
#baseInputDir=/home/lucien/AnalysisCode/Higgs/ALP/genproductions/bin/MadGraph5_aMCatNLO/workDir_acc_study_hTOzpzpTO4e_eps2e-2_mZd
#baseInputDir=/home/lucien/AnalysisCode/Higgs/ALP/genproductions/bin/MadGraph5_aMCatNLO/workDir_acc_study_hTOalpalpTOmumu_eps2e-2_mZd
#baseInputDir=/home/lucien/AnalysisCode/Higgs/ALP/genproductions/bin/MadGraph5_aMCatNLO/workDir_acc_study_hTOzpzpTO4mu_eps2e-2_mZd
#baseInputDir=/home/lucien/AnalysisCode/Higgs/ALP/genproductions/bin/MadGraph5_aMCatNLO/workDir_acc_study_hTOzzpTO4mu_eps2e-2_mZd

#baseInputDir=/home/rosedj1/DarkZ-EvtGeneration/CMSSW_9_4_2/src/DarkZ-EvtGeneration/all_workDirs_ALPvsZdark/workDir_acc_study_hTOzzpTO4mu_eps2e-2_mZd
#outputDir=/home/lucien/AnalysisCode/Higgs/ALP/genproductions/bin/MadGraph5_aMCatNLO/workDir_acc_study_hTOzzpTO4mu_eps2e-2_mZd

baseInputDir=/home/rosedj1/DarkZ-EvtGeneration/CMSSW_9_4_2/src/DarkZ-EvtGeneration/all_workDirs_ALPvsZdark/workDir_acc_study_hTOzalpTO4mu_eps2e-2_mZd
outputDir=/home/lucien/AnalysisCode/Higgs/ALP/genproductions/bin/MadGraph5_aMCatNLO/workDir_acc_study_hTOzalpTO4mu_eps2e-2_mZd
#for m in 15 20 25 30 ; 
for m in 4 5 7 10 ; 
do
    mkdir ${outputDir}${m}/UnpackTarball/ ;
    root -l -q ZZD_lhe.C\(\"${baseInputDir}${m}/UnpackTarball/cmsgrid_final.lhe\",\"${outputDir}${m}/UnpackTarball/cmsgrid_final_lhe.root\",10000\) ; 
    #root -l -q ZDZD_lhe.C\(\"${baseInputDir}${m}/UnpackTarball/cmsgrid_final.lhe\",\"${baseInputDir}${m}/UnpackTarball/cmsgrid_final_lhe.root\",10000\) ; 
done
