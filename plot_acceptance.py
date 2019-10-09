import ROOT,math,os
from BaseObject import BaseObject
from mkdir_p import mkdir_p

# ________________________________________________________________________________________________________________________ ||
ROOT.gROOT.SetBatch(ROOT.kTRUE)

# ________________________________________________________________________________________________________________________ ||
hist_cfgs = [
                BaseObject(
                    "ALP_ElEl",
                    cfgs=[ BaseObject(
                            "H-To-ALP-ALP_M"+str(m),
                            inputPath="/home/lucien/AnalysisCode/Higgs/ALP/genproductions/bin/MadGraph5_aMCatNLO/workDir_acc_study_hTOalpalp_eps2e-2_mZd%s/UnpackTarball/cmsgrid_final_lhe.root"%str(m),
                            x_label = str(m)+ "GeV",
                            ) 
                            for m in [4,7,15,20,25,30,33,] ],
                    color = ROOT.kRed,
                    ),
                BaseObject(
                    "ALP_MuMu",
                    cfgs=[ BaseObject(
                            "H-To-ALP-ALP_M"+str(m),
                            inputPath="/home/lucien/AnalysisCode/Higgs/ALP/genproductions/bin/MadGraph5_aMCatNLO/workDir_acc_study_hTOalpalpTOmumu_eps2e-2_mZd%s/UnpackTarball/cmsgrid_final_lhe.root"%str(m),
                            x_label = str(m)+ "GeV",
                            ) 
                            for m in [4,7,15,20,25,30,33,] ],
                    color = ROOT.kOrange,
                    ),
                BaseObject(
                    "Zd_ElEl",
                    cfgs=[ BaseObject(
                            "H-To-Zd-Zd_M"+str(m),
                            inputPath="/home/lucien/AnalysisCode/Higgs/ALP/genproductions/bin/MadGraph5_aMCatNLO/workDir_acc_study_hTOzpzpTO4e_eps2e-2_mZd%s/UnpackTarball/cmsgrid_final_lhe.root"%str(m),
                            x_label = str(m)+ "GeV",
                            ) 
                            for m in [4,7,15,20,25,30,33,] ],
                    color = ROOT.kBlue,
                    ),
                BaseObject(
                    "Zd_MuMu",
                    cfgs=[ BaseObject(
                            "H-To-Zd-Zd_M"+str(m),
                            inputPath="/home/lucien/AnalysisCode/Higgs/ALP/genproductions/bin/MadGraph5_aMCatNLO/workDir_acc_study_hTOzpzpTO4mu_eps2e-2_mZd%s/UnpackTarball/cmsgrid_final_lhe.root"%str(m),
                            x_label = str(m)+ "GeV",
                            ) 
                            for m in [4,7,15,20,25,30,33,] ],
                    color = ROOT.kViolet,
                    ),
                ]
treeName    = "lheEvents_tchan"
histName    = "acc"
n_tot_evts  = 10000.
outputPath  = "/home/lucien/public_html/Higgs/ALP/AcceptanceStudy/2019-10-09_hToXX/plot.pdf"
y_range     = [0.,1.]

# ________________________________________________________________________________________________________________________ ||
mkdir_p(os.path.dirname(outputPath))
c = ROOT.TCanvas()
leg = ROOT.TLegend(0.70,0.65,0.89,0.87)
for i,hist_cfg in enumerate(hist_cfgs):
    hist_cfg.hist = ROOT.TH1D(hist_cfg.name,"",len(hist_cfg.cfgs),-0.5,len(hist_cfg.cfgs)-0.5)
    leg.AddEntry(hist_cfg.hist,hist_cfg.name,"l")
    for ibin,cfg in enumerate(hist_cfg.cfgs):
        f = ROOT.TFile(cfg.inputPath,"READ")
        t = f.Get(treeName)
        acc = float(t.GetEntries())/float(n_tot_evts)
        hist_cfg.hist.SetBinContent(ibin+1,acc)
        hist_cfg.hist.SetBinError(ibin+1,math.sqrt(1./float(t.GetEntries())+1./float(n_tot_evts))*acc)
        hist_cfg.hist.GetXaxis().SetBinLabel(ibin+1,cfg.x_label)
        f.Close()
    hist_cfg.hist.SetStats(0)
    hist_cfg.hist.SetLineColor(hist_cfg.color),
    hist_cfg.hist.GetYaxis().SetRangeUser(*y_range)
    if not i:
        hist_cfg.hist.Draw()
    else:
        hist_cfg.hist.Draw("same")
leg.Draw("same")
c.SaveAs(outputPath)
