## PURPOSE: Plot kinematics from root files which were produced from LHE skimmer.
## SYNTAX:  python <script.py> <input_root_file>
## AUTHOR:  Jake Rosenzweig
## DATE:    2018-10-03
## UPDATED: 2019-05-18
## NOTES:   Make sure to point to the correct files!

import numpy as np
import os
import sys
from shutil import copy2
from ROOT import *
from tdrStyle import *
from mkdir_p import mkdir_p
from BaseObject import BaseObject

## enter batch mode in root (so python can access displays)
gROOT.SetBatch(kTRUE) #kTRUE = will NOT draw plots to the screen!
setTDRStyle()                                             

##### PARAMETERS
cuts = "WITH"    ## Choose: "WITH" or "WITHOUT"
inputFilePath1  = "/home/lucien/AnalysisCode/Higgs/ALP/genproductions/bin/MadGraph5_aMCatNLO/workDir_acc_study_hTOzpzpTO4mu_eps2e-2_mZd15/UnpackTarball/cmsgrid_final_lhe.root"
inputFilePath2  = "/home/lucien/AnalysisCode/Higgs/ALP/genproductions/bin/MadGraph5_aMCatNLO/workDir_acc_study_hTOalpalpTOmumu_eps2e-2_mZd15/UnpackTarball/cmsgrid_final_lhe.root"
mass            = "15"
mass_int        = int(mass)
outPlotDir      = "/home/lucien/public_html/Higgs/ALP/KinematicStudy/2019-10-09_hToXX/"
kinemlist       = [
                    "mass4l",
                    "eta3","eta4","eta5","eta6","phi3","phi4","phi5","phi6",
                    "pto1","pto2","pto3","pto4",
                    "massZ1","massZ2","pT4l",
                    "costheta1","costheta2","costhetastar","phi","phi1",
                    ]
extratitle      = ""
plotlist        = [
    BaseObject("mass4l",xmin=100.0,xmax=170.0,binwidth=0.5,xlabel="m_{4l} [GeV]",ylabel=str("%.5f" % 0.5)+" [GeV]",xminrange=100.0,xmaxrange=170.0,ymaxrange=0.6),
    BaseObject("massZ1",xmin=4.0,xmax=62.5,binwidth=0.5,xlabel="m_{Z1} [GeV]",ylabel=str("%.5f" % 0.5)+" [GeV]",xminrange=4.0,xmaxrange=62.5,ymaxrange=0.6),
    BaseObject("massZ2",xmin=4.0,xmax=62.5,binwidth=0.5,xlabel="m_{Z2} [GeV]",ylabel=str("%.5f" % 0.5)+" [GeV]",xminrange=4.0,xmaxrange=62.5,ymaxrange=0.6),
    BaseObject("eta3",xmin=-2.8,xmax=2.8,binwidth=0.2,xlabel="#eta_{3}",ylabel=str("%.5f" % 0.2),xminrange=-2.8,xmaxrange=2.8,ymaxrange=0.07),
    BaseObject("eta4",xmin=-2.8,xmax=2.8,binwidth=0.2,xlabel="#eta_{4}",ylabel=str("%.5f" % 0.2),xminrange=-2.8,xmaxrange=2.8,ymaxrange=0.07),
    BaseObject("eta5",xmin=-2.8,xmax=2.8,binwidth=0.2,xlabel="#eta_{5}",ylabel=str("%.5f" % 0.2),xminrange=-2.8,xmaxrange=2.8,ymaxrange=0.07),
    BaseObject("eta6",xmin=-2.8,xmax=2.8,binwidth=0.2,xlabel="#eta_{6}",ylabel=str("%.5f" % 0.2),xminrange=-2.8,xmaxrange=2.8,ymaxrange=0.07),
    BaseObject("phi3",xmin=-np.pi,xmax=np.pi,binwidth=np.pi/20,xlabel="#phi_{3}"+" [radians]",ylabel=str("%.5f" % (np.pi/20))+" [radians]",xminrange=-3.5,xmaxrange=3.5,ymaxrange=0.04),
    BaseObject("phi4",xmin=-np.pi,xmax=np.pi,binwidth=np.pi/20,xlabel="#phi_{4}"+" [radians]",ylabel=str("%.5f" % (np.pi/20))+" [radians]",xminrange=-3.5,xmaxrange=3.5,ymaxrange=0.04),
    BaseObject("phi5",xmin=-np.pi,xmax=np.pi,binwidth=np.pi/20,xlabel="#phi_{5}"+" [radians]",ylabel=str("%.5f" % (np.pi/20))+" [radians]",xminrange=-3.5,xmaxrange=3.5,ymaxrange=0.04),
    BaseObject("phi6",xmin=-np.pi,xmax=np.pi,binwidth=np.pi/20,xlabel="#phi_{6}"+" [radians]",ylabel=str("%.5f" % (np.pi/20))+" [radians]",xminrange=-3.5,xmaxrange=3.5,ymaxrange=0.04),
    BaseObject("pto1",xmin=0.0,xmax=120.0,binwidth=1.0,xlabel="p_{T,1} [GeV]",ylabel=str("%.5f" % 1.0)+" [GeV]",xminrange=0.0,xmaxrange=120.0,ymaxrange=0.1),
    BaseObject("pto2",xmin=0.0,xmax=120.0,binwidth=1.0,xlabel="p_{T,2} [GeV]",ylabel=str("%.5f" % 1.0)+" [GeV]",xminrange=0.0,xmaxrange=120.0,ymaxrange=0.1),
    BaseObject("pto3",xmin=0.0,xmax=120.0,binwidth=1.0,xlabel="p_{T,3} [GeV]",ylabel=str("%.5f" % 1.0)+" [GeV]",xminrange=0.0,xmaxrange=120.0,ymaxrange=0.1),
    BaseObject("pto4",xmin=0.0,xmax=120.0,binwidth=1.0,xlabel="p_{T,4} [GeV]",ylabel=str("%.5f" % 1.0)+" [GeV]",xminrange=0.0,xmaxrange=120.0,ymaxrange=0.1),
    BaseObject("costheta1",xmin=-1.0,xmax=1.0,binwidth=0.05,xlabel="cos(#theta_{1})",ylabel=str("%.5f" % 0.05),xminrange=-1.2,xmaxrange=1.2,ymaxrange=0.05),
    BaseObject("costheta2",xmin=-1.0,xmax=1.0,binwidth=0.05,xlabel="cos(#theta_{2})",ylabel=str("%.5f" % 0.05),xminrange=-1.2,xmaxrange=1.2,ymaxrange=0.05),
    BaseObject("costhetastar",xmin=-1.0,xmax=1.0,binwidth=0.05,xlabel="cos(#theta_{*})",ylabel=str("%.5f" % 0.05),xminrange=-1.2,xmaxrange=1.2,ymaxrange=0.05),
    BaseObject("phi",xmin=-np.pi,xmax=np.pi,binwidth=np.pi/20,xlabel="#phi"+" [radians]",ylabel=str("%.5f" % (np.pi/20))+" [radians]",xminrange=-3.5,xmaxrange=3.5,ymaxrange=0.04),
    BaseObject("phi1",xmin=-np.pi,xmax=np.pi,binwidth=np.pi/20,xlabel="#phi_{1}"+" [radians]",ylabel=str("%.5f" % (np.pi/20))+" [radians]",xminrange=-3.5,xmaxrange=3.5,ymaxrange=0.04),
    ]


mkdir_p(outPlotDir)
if extratitle != "": 
    extratitle = ", " + extratitle

f1 = TFile(inputFilePath1,"READ")
f2 = TFile(inputFilePath2,"READ")
t1 = f1.Get("lheEvents_tchan")
t2 = f2.Get("lheEvents_tchan")
for p in plotlist:
    kinem = p.name
    xmin = p.xmin
    xmax = p.xmax
    binwidth = p.binwidth
    xlabel = p.xlabel
    ylabel = p.ylabel
    xminrange = p.xmin
    xmaxrange = p.xmax
    ymaxrange = p.ymaxrange

    h1 = TH1D("h1_mZd%s_%s" % (mass,kinem),"h1_mZd%s_%s" % (mass,kinem), int( (xmax-xmin)/binwidth ), xmin, xmax)
    h2 = TH1D("h2_mZd%s_%s" % (mass,kinem),"h2_mZd%s_%s" % (mass,kinem), int( (xmax-xmin)/binwidth ), xmin, xmax)
    h1.Sumw2()                              
    h2.Sumw2()                              

    c1 = TCanvas("c_mZd%s_%s" % (mass,kinem),"c_mZd%s_%s" % (mass,kinem),800,800)
    c1.cd()                                                   
    t1.Draw("%s>>h1_mZd%s_%s" % (kinem,mass,kinem), "", "goff")
    t2.Draw("%s>>h2_mZd%s_%s" % (kinem,mass,kinem), "", "goff")
    if h1.Integral() != 0: 
        #print("Scaling "+kinem)
        h1.Scale(1./h1.Integral())
    else: print("WARNING!: "+kinem+" for mass "+mass+" has Integral() = 0!")
    if h2.Integral() != 0: 
        #print("Scaling "+kinem)
        h2.Scale(1./h2.Integral())
    else: print("WARNING!: "+kinem+" for mass "+mass+" has Integral() = 0!")

    ## Try GetXaxis instead if you need to set range
    #h1.GetXaxis().SetRangeUser(xmin, xmax)

    h1.SetLineWidth(3)
    h1.SetLineColor(ROOT.kBlack)                                
    h1.SetTitle("pp #rightarrow H #rightarrow XX #rightarrow 4l, mZ_{d} = %d GeV%s" % (mass_int, extratitle))
    h1.SetXTitle("%s" % xlabel)
    h1.SetYTitle("Fraction of Events / %s" % ylabel )
    h1.SetLabelSize(0.025, "XY")
    h1.SetAxisRange(xminrange, xmaxrange, "X")
    h1.SetAxisRange(0, ymaxrange, "Y")
    h2.SetLineWidth(3)
    h2.SetLineColor(ROOT.kRed)                                
    h2.SetTitle("pp #rightarrow H #rightarrow XX #rightarrow 4l, mZ_{d} = %d GeV%s" % (mass_int, extratitle))
    h2.SetXTitle("%s" % xlabel)
    h2.SetYTitle("Fraction of Events / %s" % ylabel )
    h2.SetLabelSize(0.025, "XY")
    h2.SetAxisRange(xminrange, xmaxrange, "X")
    h2.SetAxisRange(0, ymaxrange, "Y")
                    
    h1.Draw("e1 hist 9 goff")                                  
    h2.Draw("e1 hist 9 same goff")                                  

    ## Make sure legend doesn't block histogram lines
    if kinem in ["phi","phi1","phi3","phi4","phi5","phi6","costheta1","costheta2","costhetastar"]:
        legend = TLegend(0.42,0.20,0.62,0.40)
    else:
        legend = TLegend(0.67,0.7,0.87,0.9)
    legend.AddEntry(h1, "#splitline{POWHEG+JHUGen}{(NLO)}", "lpf")
    legend.SetLineWidth(2)
    legend.SetBorderSize(0)
    legend.SetTextSize(0.025)
    legend.SetFillStyle(0)  ## transparent legend
    #legend.Draw("same goff")

    ## For plot-ordering purposes on tier2 website, change 1 --> 01, 2-->02, etc.
    outputFile = outPlotDir + kinem+"_mZd"+mass+".png"
    c1.SaveAs( outputFile )
    outputFile = outPlotDir + kinem+"_mZd"+mass+".pdf"
    c1.SaveAs( outputFile )
