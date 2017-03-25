#!/usr/bin/env python
'''@package docstring
Just a giant list of processes and properties
'''

processes =	{
'DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8':('ZJets_nlo','MC',6025.2),
'DYJetsToNuNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8':('ZtoNuNu_nlo','MC',11433.),
'WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8':('WJets_nlo','MC',61527.),

'DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8':('ZJets_ht100to200','MC',148.),
'DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8':('ZJets_ht200to400','MC',40.94),
'DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8':('ZJets_ht400to600','MC',5.497),
'DYJetsToLL_M-50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8':('ZJets_ht600toinf','MC',2.193),
'DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8':('ZJets_ht1200to2500','MC',0.1514),
'DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8':('ZJets_ht2500toinf','MC',0.003565),
'DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8':('ZJets_ht600to800','MC',1.367),
'DYJetsToLL_M-50_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8':('ZJets_ht800to1200','MC',0.6304),

'WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8':('WJets_ht100to200','MC',1343),
'WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8':('WJets_ht200to400','MC',359.6),
'WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8':('WJets_ht400to600','MC',48.85),
'WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8':('WJets_ht600to800','MC',12.05),
'WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8':('WJets_ht800to1200','MC',5.501),
'WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8':('WJets_ht1200to2500','MC',1.329),
'WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8':('WJets_ht2500toinf','MC',0.03216),
'WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8':('WJets_ht600toinf','MC',18.91),

'WJetsToLNu_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8':('WJets_pt100to250','MC',682.2),
'WJetsToLNu_Pt-250To400_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8':('WJets_pt250to400','MC',24.10),
'WJetsToLNu_Pt-400To600_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8':('WJets_pt400to600','MC',3.054),
'WJetsToLNu_Pt-600ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8':('WJets_pt600toinf','MC',0.4590),

'DYJetsToLL_Pt-50To100_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8':('ZJets_pt50to100','MC',355.3),
'DYJetsToLL_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8':('ZJets_pt100to250','MC',81.02),
'DYJetsToLL_Pt-250To400_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8':('ZJets_pt250to400','MC',2.991),
'DYJetsToLL_Pt-400To650_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8':('ZJets_pt400to650','MC',0.3882),
'DYJetsToLL_Pt-650ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8':('ZJets_pt650toinf','MC',0.03737),

'ZJetsToNuNu_HT-100To200_13TeV-madgraph':('ZtoNuNu_ht100to200','MC',280.5),
'ZJetsToNuNu_HT-200To400_13TeV-madgraph':('ZtoNuNu_ht200to400','MC',77.7),
'ZJetsToNuNu_HT-400To600_13TeV-madgraph':('ZtoNuNu_ht400to600','MC',10.71),
'ZJetsToNuNu_HT-600To800_13TeV-madgraph':('ZtoNuNu_ht600to800','MC',2.562),
'ZJetsToNuNu_HT-800To1200_13TeV-madgraph':('ZtoNuNu_ht800to1200','MC',1.183),
'ZJetsToNuNu_HT-1200To2500_13TeV-madgraph':('ZtoNuNu_ht1200to2500','MC',0.286),
'ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph':('ZtoNuNu_ht2500toinf','MC',0.006945),
'ZJetsToNuNu_HT-600ToInf_13TeV-madgraph':('ZtoNuNu_ht600toinf','MC',4.098),

'GJets_HT-40To100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8':('GJets_ht40to100','MC',23080.0),
'GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8':('GJets_ht100to200','MC',9235),
'GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8':('GJets_ht200to400','MC',2298),
'GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8':('GJets_ht400to600','MC',277.6),
'GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8':('GJets_ht600toinf','MC',93.47),

'QCD_HT100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8':('QCD_ht100to200','MC',27990000),
'QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8':('QCD_ht200to300','MC',1735000),
'QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8':('QCD_ht300to500','MC',366800),
'QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8':('QCD_ht500to700','MC',29370),
'QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8':('QCD_ht700to1000','MC',6524),
'QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8':('QCD_ht1000to1500','MC',1064),
'QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8':('QCD_ht1500to2000','MC',121.5),
'QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8':('QCD_ht2000toinf','MC',25.42),

'ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8':('SingleTop_tTbar_lep','MC',26.22),
'ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8':('SingleTop_tT_lep','MC',44.07),
'ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1':('SingleTop_tW','MC',35.85),
'ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1':('SingleTop_tbarW','MC',35.85),
'ST_t-channel_antitop_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1':('SingleTop_tTbar','MC',80.95),
'ST_t-channel_top_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1':('SingleTop_tT','MC',136.02),
'ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1':('SingleTop_s_lep','MC',10.11),
'ST_t-channel_5f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1':('SingleTop_t_lep','MC',216.99),
'ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1':('SingleTop_tchannel','MC',44.3),

'TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8':                    ('TTbar_MLM','MC',831.76),
'TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8':             ('TTbar_2L','MC',831.76*(1-0.68)*(1-0.68)),
'TTJets_SingleLeptFromT_TuneCUETP8M1_13TeV-madgraphMLM-pythia8':    ('TTbar_1LT','MC',831.76*0.68*(1-0.68)),
'TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8': ('TTbar_1LTbar','MC',831.76*0.68*(1-0.68)),
'TT_TuneEE5C_13TeV-powheg-herwigpp':                                ('TTbar_Herwig','MC',831.76),
'TTJets_TuneCUETP8M2T4_13TeV-amcatnloFXFX-pythia8':                 ('TTbar_FXFX','MC',831.76),
'TT_TuneCUETP8M2T4_13TeV-powheg-pythia8':                           ('TTbar_Powheg','MC',831.76),
'TT_TuneCUETP8M2T4_13TeV-powheg-isrdown-pythia8':                   ('TTbar_PowhegISRDown','MC',831.76),
'TT_TuneCUETP8M2T4_13TeV-powheg-isrup-pythia8':                     ('TTbar_PowhegISRUp','MC',831.76),
'TT_TuneCUETP8M2T4down_13TeV-powheg-pythia8':                       ('TTbar_PowhegTuneDown','MC',831.76),
'TT_TuneCUETP8M2T4up_13TeV-powheg-pythia8':                         ('TTbar_PowhegTuneUp','MC',831.76),
#'TT_TuneCUETP8M2T4_13TeV-powheg-pythia8':                           ('TTbar_Powheg','MC',831.76),
#'TT_TuneCUETP8M2T4_13TeV-powheg-isrdown-pythia8':                   ('TTbar_PowhegISRDown','MC',831.76),
#'TT_TuneCUETP8M2T4_13TeV-powheg-isrup-pythia8':                     ('TTbar_PowhegISRUp','MC',831.76),
#'TT_TuneCUETP8M2T4down_13TeV-powheg-pythia8':                       ('TTbar_PowhegTuneDown','MC',831.76),
#'TT_TuneCUETP8M2T4up_13TeV-powheg-pythia8':                         ('TTbar_PowhegTuneUp','MC',831.76),


'tZq_ll_4f_13TeV-amcatnlo-pythia8':('SingleTop_tZll','MC',0.0758),
'tZq_nunu_4f_13TeV-amcatnlo-pythia8_TuneCUETP8M1':('SingleTop_tZnunu','MC',0.1379),
'TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8':('TTbar_GJets','MC',3.786),
'TGJets_TuneCUETP8M1_13TeV_amcatnlo_madspin_pythia8':('SingleTop_tG','MC',2.967),

'EWKZ2Jets_ZToNuNu_13TeV-madgraph-pythia8':('ZtoNuNu_EWK','MC',10.04),
'EWKZ2Jets_ZToLL_M-50_13TeV-madgraph-pythia8':('ZJets_EWK','MC',3.99),
'EWKWPlus2Jets_WToLNu_M-50_13TeV-madgraph-pythia8':('WJets_EWKWPlus','MC',25.81),
'EWKWMinus2Jets_WToLNu_M-50_13TeV-madgraph-pythia8':('WJets_EWKWMinus','MC',20.35),

'WW_TuneCUETP8M1_13TeV-pythia8':('Diboson_ww','MC',118.7),
'WZ_TuneCUETP8M1_13TeV-pythia8':('Diboson_wz','MC',47.2),
'ZZ_TuneCUETP8M1_13TeV-pythia8':('Diboson_zz','MC',16.6),

'Monotop_S1_Mres-2100_Mchi-100_TuneCUETP8M1_13TeV-madgraph-pythia8':('monotop_res_mMed2100','MC',1),
'Monotop_S1_Mres-1900_Mchi-100_TuneCUETP8M1_13TeV-madgraph-pythia8':('monotop_res_mMed1900','MC',1),
'Monotop_S1_Mres-1700_Mchi-100_TuneCUETP8M1_13TeV-madgraph-pythia8':('monotop_res_mMed1700','MC',1),
'Monotop_S1_Mres-1500_Mchi-100_TuneCUETP8M1_13TeV-madgraph-pythia8':('monotop_res_mMed1500','MC',1),
'Monotop_S1_Mres-1300_Mchi-100_TuneCUETP8M1_13TeV-madgraph-pythia8':('monotop_res_mMed1300','MC',1),
'Monotop_S1_Mres-1100_Mchi-100_TuneCUETP8M1_13TeV-madgraph-pythia8':('monotop_res_mMed1100','MC',1),
'Monotop_S1_Mres-900_Mchi-100_TuneCUETP8M1_13TeV-madgraph-pythia8':('monotop_res_mMed900','MC',1),
'Monotop_S4_Mchi-300_TuneCUETP8M1_13TeV-madgraph-pythia8':('monotop_fcnc_mMed300','MC',1),
'Monotop_S4_Mchi-500_TuneCUETP8M1_13TeV-madgraph-pythia8':('monotop_fcnc_mMed500','MC',1),
'Monotop_S4_Mchi-700_TuneCUETP8M1_13TeV-madgraph-pythia8':('monotop_fcnc_mMed700','MC',1),
'Monotop_S4_Mchi-900_TuneCUETP8M1_13TeV-madgraph-pythia8':('monotop_fcnc_mMed900','MC',1),
'Monotop_S4_Mchi-1100_TuneCUETP8M1_13TeV-madgraph-pythia8':('monotop_fcnc_mMed1100','MC',1),
'Monotop_S4_Mchi-1300_TuneCUETP8M1_13TeV-madgraph-pythia8':('monotop_fcnc_mMed1300','MC',1),
'Monotop_S4_Mchi-1500_TuneCUETP8M1_13TeV-madgraph-pythia8':('monotop_fcnc_mMed1500','MC',1),
'Monotop_S4_Mchi-1700_TuneCUETP8M1_13TeV-madgraph-pythia8':('monotop_fcnc_mMed1700','MC',1),

'TTbarDMJets_pseudoscalar_Mchi-1_Mphi-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8':('TTbarDM','MC',1),

'MET':('MET','Data',1),
'SingleMuon':('SingleMuon','Data',1),
'DoubleEG':('DoubleEG','Data',1),
'SingleElectron':('SingleElectron','Data',1),
'SinglePhoton':('SinglePhoton','Data',1),


'monotop_med-900_dm-100':('monotop_med-900_dm-100','MC',3.09067),
'monotop_med-1100_dm-100':('monotop_med-1100_dm-100','MC',1.307),
'monotop_med-1300_dm-100':('monotop_med-1300_dm-100','MC',0.6149),
'monotop_med-1500_dm-100':('monotop_med-1500_dm-100','MC',0.314),
'monotop_med-1700_dm-100':('monotop_med-1700_dm-100','MC',0.1699),
'monotop_med-1900_dm-100':('monotop_med-1900_dm-100','MC',0.09622),
'monotop_med-2100_dm-100':('monotop_med-2100_dm-100','MC',0.05673),
'monotop_med-2300_dm-100':('monotop_med-2300_dm-100','MC',0.03456),
'monotop_med-2500_dm-100':('monotop_med-2500_dm-100','MC',0.02148),
'monotop_med-2700_dm-100':('monotop_med-2700_dm-100','MC',0.01375),
'monotop_med-2900_dm-100':('monotop_med-2900_dm-100','MC',0.008956),

'monotop-nr-300_med-300':('monotop-nr-300_med-300','MC',32.55),
'monotop-nr-500_med-500':('monotop-nr-500_med-500','MC',7.535),
'monotop-nr-700_med-700':('monotop-nr-700_med-700','MC',2.403),
'monotop-nr-900_med-900':('monotop-nr-900_med-900','MC',0.9205),
'monotop-nr-1100_med-1100':('monotop-nr-1100_med-1100','MC',0.3961),
'monotop-nr-1300_med-1300':('monotop-nr-1300_med-1300','MC',0.186),
'monotop-nr-1500_med-1500':('monotop-nr-1500_med-1500','MC',0.09258),
'monotop-nr-1700_med-1700':('monotop-nr-1700_med-1700','MC',0.04817),
'monotop-nr-1900_med-1900':('monotop-nr-1900_med-1900','MC',0.02614),
'monotop-nr-2100_med-2100':('monotop-nr-2100_med-2100','MC',0.01453),
'monotop-nr-2300_med-2300':('monotop-nr-2300_med-2300','MC',0.00826),
'monotop-nr-2500_med-2500':('monotop-nr-2500_med-2500','MC',0.00826),
'monotop-nr-2700_med-2700':('monotop-nr-2700_med-2700','MC',0.00826),
'monotop-nr-2900_med-2900':('monotop-nr-2900_med-2900','MC',0.00826),

'monotop-nr-v3-50-10_dm-10':('monotop-nr-v3-50-10','MC',1),
'monotop-nr-v3-100-10_med-100_dm-10':('monotop-nr-v3-100-10','MC',1),
'monotop-nr-v3-200-10_med-200_dm-10':('monotop-nr-v3-200-10','MC',1),
'monotop-nr-v3-300-10_med-300_dm-10':('monotop-nr-v3-300-10','MC',1),
'monotop-nr-v3-500-10_med-500_dm-10':('monotop-nr-v3-500-10','MC',1),
'monotop-nr-v3-700-10_med-700_dm-10':('monotop-nr-v3-700-10','MC',1),
'monotop-nr-v3-900-10_med-900_dm-10':('monotop-nr-v3-900-10','MC',1),
'monotop-nr-v3-1100-10_med-1100_dm-10':('monotop-nr-v3-1100-10','MC',1),
'monotop-nr-v3-1300-10_med-1300_dm-10':('monotop-nr-v3-1300-10','MC',1),
'monotop-nr-v3-1500-10_med-1500_dm-10':('monotop-nr-v3-1500-10','MC',1),
'monotop-nr-v3-1700-10_med-1700_dm-10':('monotop-nr-v3-1700-10','MC',1),
'monotop-nr-v3-1900-10_med-1900_dm-10':('monotop-nr-v3-1900-10','MC',1),
'monotop-nr-v3-2100-10_med-2100_dm-10':('monotop-nr-v3-2100-10','MC',1),
'monotop-nr-v3-2300-10_med-2300_dm-10':('monotop-nr-v3-2300-10','MC',1),
'monotop-nr-v3-2500-10_med-2500_dm-10':('monotop-nr-v3-2500-10','MC',1),
'monotop-nr-v3-2700-10_med-2700_dm-10':('monotop-nr-v3-2700-10','MC',1),
'monotop-nr-v3-2900-10_med_2900_dm-10':('monotop-nr-v3-2900-10','MC',1),

'non-res-v3-1100':('non-res-v3-1100','MC',1),
'op-resonant-1100':('op-resonant-1100','MC',1),
'op-non-resonant-1100':('op-non-resonant-1100','MC',1),
'new-non-res-1100-10':('new-non-res-1100-10','MC',1),
'monotop-nr-50ns_med-1100':('monotop-nr-50ns_med-1100','MC',1),
'monotop-nr-v3-50ns_med-1100_dm-10':('monotop-nr-v3-50ns_med-1100_dm-10','MC',1),

'GluGlu_HToInvisible_M125_13TeV_powheg_pythia8':('ggFHinv','MC',48.6),
'Glu_HToInvisible_M125_13TeV_powheg_pythia8':('ggf-m125','MC',48.6),
'VBF_HToInvisible_M125_13TeV_powheg_pythia8':('vbf-m125','MC',3.78),
'VBF_HToInvisible_M1000_13TeV_powheg_pythia8':('vbf-m1000','MC',1),
'VBF_HToInvisible_M110_13TeV_powheg_pythia8':('vbf-m110','MC',1),
'VBF_HToInvisible_M150_13TeV_powheg_pythia8':('vbf-m150','MC',1),
'VBF_HToInvisible_M200_13TeV_powheg_pythia8':('vbf-m200','MC',1),
'VBF_HToInvisible_M300_13TeV_powheg_pythia8':('vbf-m300','MC',1),
'VBF_HToInvisible_M500_13TeV_powheg_pythia8':('vbf-m500','MC',1),
'VBF_HToInvisible_M600_13TeV_powheg_pythia8':('vbf-m600','MC',1),
'VBF_HToInvisible_M800_13TeV_powheg_pythia8':('vbf-m800','MC',1),

'ZprimeToTTJet_M-500_TuneCUETP8M1_13TeV-amcatnlo-pythia8':('ZpTT_med-500','MC',1),
'ZprimeToTTJet_M-750_TuneCUETP8M1_13TeV-amcatnlo-pythia8':('ZpTT_med-750','MC',1),
'ZprimeToTTJet_M-1000_TuneCUETP8M1_13TeV-amcatnlo-pythia8':('ZpTT_med-1000','MC',1),
'ZprimeToTTJet_M-1250_TuneCUETP8M1_13TeV-amcatnlo-pythia8':('ZpTT_med-1250','MC',1),
'ZprimeToTTJet_M-1500_TuneCUETP8M1_13TeV-amcatnlo-pythia8':('ZpTT_med-1500','MC',1),
'ZprimeToTTJet_M-2000_TuneCUETP8M1_13TeV-amcatnlo-pythia8':('ZpTT_med-2000','MC',1),
'ZprimeToTTJet_M-2500_TuneCUETP8M1_13TeV-amcatnlo-pythia8':('ZpTT_med-2500','MC',1),
'ZprimeToTTJet_M-3000_TuneCUETP8M1_13TeV-amcatnlo-pythia8':('ZpTT_med-3000','MC',1),
'ZprimeToTTJet_M-3500_TuneCUETP8M1_13TeV-amcatnlo-pythia8':('ZpTT_med-3500','MC',1),
'ZprimeToTTJet_M-4000_TuneCUETP8M1_13TeV-amcatnlo-pythia8':('ZpTT_med-4000','MC',1),

'ZprimeToWW_narrow_M-800_13TeV-madgraph':('ZpWW_med-800','MC',1),
'ZprimeToWW_narrow_M-1000_13TeV-madgraph':('ZpWW_med-1000','MC',1),
'ZprimeToWW_narrow_M-1200_13TeV-madgraph':('ZpWW_med-1200','MC',1),
'ZprimeToWW_narrow_M-1400_13TeV-madgraph':('ZpWW_med-1400','MC',1),
'ZprimeToWW_narrow_M-1600_13TeV-madgraph':('ZpWW_med-1600','MC',1),
'ZprimeToWW_narrow_M-1800_13TeV-madgraph':('ZpWW_med-1800','MC',1),
'ZprimeToWW_narrow_M-2000_13TeV-madgraph':('ZpWW_med-2000','MC',1),
'ZprimeToWW_narrow_M-2500_13TeV-madgraph':('ZpWW_med-2500','MC',1),

'ZprimeToA0hToA0chichihbb_2HDM_MZp-800_MA0-300_13TeV-madgraph':('ZpA0h_med-800','MC',1),
'ZprimeToA0hToA0chichihbb_2HDM_MZp-1000_MA0-300_13TeV-madgraph':('ZpA0h_med-1000','MC',1),
'ZprimeToA0hToA0chichihbb_2HDM_MZp-1200_MA0-300_13TeV-madgraph':('twohdm_med-1200','MC',1),
'ZprimeToA0hToA0chichihbb_2HDM_MZp-1400_MA0-300_13TeV-madgraph':('ZpA0h_med-1400','MC',1),
'ZprimeToA0hToA0chichihbb_2HDM_MZp-1700_MA0-300_13TeV-madgraph':('ZpA0h_med-1700','MC',1),
'ZprimeToA0hToA0chichihbb_2HDM_MZp-2000_MA0-300_13TeV-madgraph':('ZpA0h_med-2000','MC',1),
'ZprimeToA0hToA0chichihbb_2HDM_MZp-2500_MA0-300_13TeV-madgraph':('ZpA0h_med-2500','MC',1),

'MonoHbb_ZpBaryonic_MZp-10_MChi-1_13TeV-madgraph':('ZpBaryonic_med-10_dm-1','MC',1),
'MonoHbb_ZpBaryonic_MZp-10_MChi-10_13TeV-madgraph':('ZpBaryonic_med-10_dm-10','MC',1),
'MonoHbb_ZpBaryonic_MZp-10_MChi-50_13TeV-madgraph':('ZpBaryonic_med-10_dm-50','MC',1),
'MonoHbb_ZpBaryonic_MZp-10_MChi-150_13TeV-madgraph':('ZpBaryonic_med-10_dm-150','MC',1),
'MonoHbb_ZpBaryonic_MZp-10_MChi-500_13TeV-madgraph':('ZpBaryonic_med-10_dm-500','MC',1),
'MonoHbb_ZpBaryonic_MZp-10_MChi-1000_13TeV-madgraph':('ZpBaryonic_med-10_dm-1000','MC',1),
'MonoHbb_ZpBaryonic_MZp-15_MChi-10_13TeV-madgraph':('ZpBaryonic_med-15_dm-10','MC',1),
'MonoHbb_ZpBaryonic_MZp-20_MChi-1_13TeV-madgraph':('ZpBaryonic_med-20_dm-1','MC',1),
'MonoHbb_ZpBaryonic_MZp-50_MChi-1_13TeV-madgraph':('ZpBaryonic_med-50_dm-1','MC',1),
'MonoHbb_ZpBaryonic_MZp-50_MChi-10_13TeV-madgraph':('ZpBaryonic_med-50_dm-10','MC',1),
'MonoHbb_ZpBaryonic_MZp-50_MChi-50_13TeV-madgraph':('ZpBaryonic_med-50_dm-50','MC',1),
'MonoHbb_ZpBaryonic_MZp-95_MChi-50_13TeV-madgraph':('ZpBaryonic_med-95_dm-50','MC',1),
'MonoHbb_ZpBaryonic_MZp-100_MChi-1_13TeV-madgraph':('ZpBaryonic_med-100_dm-1','MC',1),
'MonoHbb_ZpBaryonic_MZp-100_MChi-10_13TeV-madgraph':('ZpBaryonic_med-100_dm-10','MC',1),
'MonoHbb_ZpBaryonic_MZp-200_MChi-1_13TeV-madgraph':('ZpBaryonic_med-200_dm-1','MC',1),
'MonoHbb_ZpBaryonic_MZp-200_MChi-50_13TeV-madgraph':('ZpBaryonic_med-200_dm-50','MC',1),
'MonoHbb_ZpBaryonic_MZp-200_MChi-150_13TeV-madgraph':('ZpBaryonic_med-200_dm-150','MC',1),
'MonoHbb_ZpBaryonic_MZp-295_MChi-150_13TeV-madgraph':('ZpBaryonic_med-295_dm-150','MC',1),
'MonoHbb_ZpBaryonic_MZp-300_MChi-1_13TeV-madgraph':('ZpBaryonic_med-300_dm-1','MC',1),
'MonoHbb_ZpBaryonic_MZp-300_MChi-50_13TeV-madgraph':('ZpBaryonic_med-300_dm-50','MC',1),
'MonoHbb_ZpBaryonic_MZp-500_MChi-1_13TeV-madgraph':('ZpBaryonic_med-500_dm-1','MC',1),
'MonoHbb_ZpBaryonic_MZp-500_MChi-150_13TeV-madgraph':('ZpBaryonic_med-500_dm-150','MC',1),
'MonoHbb_ZpBaryonic_MZp-500_MChi-500_13TeV-madgraph':('ZpBaryonic_med-500_dm-500','MC',1),
'MonoHbb_ZpBaryonic_MZp-995_MChi-500_13TeV-madgraph':('ZpBaryonic_med-995_dm-500','MC',1),
'MonoHbb_ZpBaryonic_MZp-1000_MChi-1_13TeV-madgraph':('ZpBaryonic_med-1000_dm-1','MC',1),
'MonoHbb_ZpBaryonic_MZp-1000_MChi-150_13TeV-madgraph':('ZpBaryonic_med-1000_dm-150','MC',1),
'MonoHbb_ZpBaryonic_MZp-1000_MChi-1000_13TeV-madgraph':('ZpBaryonic_med-1000_dm-1000','MC',1),
'MonoHbb_ZpBaryonic_MZp-1995_MChi-1000_13TeV-madgraph':('ZpBaryonic_med-1995_dm-1000','MC',1),
'MonoHbb_ZpBaryonic_MZp-2000_MChi-1_13TeV-madgraph':('ZpBaryonic_med-2000_dm-1','MC',1),
'MonoHbb_ZpBaryonic_MZp-2000_MChi-500_13TeV-madgraph':('ZpBaryonic_med-2000_dm-500','MC',1),
'MonoHbb_ZpBaryonic_MZp-10000_MChi-1_13TeV-madgraph':('ZpBaryonic_med-10000_dm-1','MC',1),
'MonoHbb_ZpBaryonic_MZp-10000_MChi-10_13TeV-madgraph':('ZpBaryonic_med-10000_dm-10','MC',1),
'MonoHbb_ZpBaryonic_MZp-10000_MChi-50_13TeV-madgraph':('ZpBaryonic_med-10000_dm-50','MC',1),
'MonoHbb_ZpBaryonic_MZp-10000_MChi-150_13TeV-madgraph':('ZpBaryonic_med-10000_dm-150','MC',1),
'MonoHbb_ZpBaryonic_MZp-10000_MChi-500_13TeV-madgraph':('ZpBaryonic_med-10000_dm-500','MC',1),
'MonoHbb_ZpBaryonic_MZp-10000_MChi-1000_13TeV-madgraph':('ZpBaryonic_med-10000_dm-1000','MC',1),

'/ZprimeToA0hToA0chichihbb_2HDM_MZp-2500_MA0-500_13TeV-madgraph':('ZpA0h_med-2500_dm-500','MC',1),
'/ZprimeToA0hToA0chichihbb_2HDM_MZp-1400_MA0-500_13TeV-madgraph':('ZpA0h_med-1400_dm-500','MC',1),
'/ZprimeToA0hToA0chichihbb_2HDM_MZp-800_MA0-600_13TeV-madgraph':('ZpA0h_med-800_dm-600','MC',1),
'/ZprimeToA0hToA0chichihbb_2HDM_MZp-800_MA0-500_13TeV-madgraph':('ZpA0h_med-800_dm-500','MC',1),
'/ZprimeToA0hToA0chichihbb_2HDM_MZp-800_MA0-400_13TeV-madgraph':('ZpA0h_med-800_dm-400','MC',1),
'/ZprimeToA0hToA0chichihbb_2HDM_MZp-800_MA0-300_13TeV-madgraph':('ZpA0h_med-800_dm-300','MC',1),
'/ZprimeToA0hToA0chichihbb_2HDM_MZp-600_MA0-400_13TeV-madgraph':('ZpA0h_med-600_dm-400','MC',1),
'/ZprimeToA0hToA0chichihbb_2HDM_MZp-600_MA0-300_13TeV-madgraph':('ZpA0h_med-600_dm-300','MC',1),
'/ZprimeToA0hToA0chichihbb_2HDM_MZp-2500_MA0-800_13TeV-madgraph':('ZpA0h_med-2500_dm-800','MC',1),
'/ZprimeToA0hToA0chichihbb_2HDM_MZp-2500_MA0-700_13TeV-madgraph':('ZpA0h_med-2500_dm-700','MC',1),
'/ZprimeToA0hToA0chichihbb_2HDM_MZp-2500_MA0-600_13TeV-madgraph':('ZpA0h_med-2500_dm-600','MC',1),
'/ZprimeToA0hToA0chichihbb_2HDM_MZp-2500_MA0-400_13TeV-madgraph':('ZpA0h_med-2500_dm-400','MC',1),
'/ZprimeToA0hToA0chichihbb_2HDM_MZp-2500_MA0-300_13TeV-madgraph':('ZpA0h_med-2500_dm-300','MC',1),
'/ZprimeToA0hToA0chichihbb_2HDM_MZp-2000_MA0-800_13TeV-madgraph':('ZpA0h_med-2000_dm-800','MC',1),
'/ZprimeToA0hToA0chichihbb_2HDM_MZp-2000_MA0-700_13TeV-madgraph':('ZpA0h_med-2000_dm-700','MC',1),
'/ZprimeToA0hToA0chichihbb_2HDM_MZp-2000_MA0-600_13TeV-madgraph':('ZpA0h_med-2000_dm-600','MC',1),
'/ZprimeToA0hToA0chichihbb_2HDM_MZp-2000_MA0-500_13TeV-madgraph':('ZpA0h_med-2000_dm-500','MC',1),
'/ZprimeToA0hToA0chichihbb_2HDM_MZp-2000_MA0-400_13TeV-madgraph':('ZpA0h_med-2000_dm-400','MC',1),
'/ZprimeToA0hToA0chichihbb_2HDM_MZp-2000_MA0-300_13TeV-madgraph':('ZpA0h_med-2000_dm-300','MC',1),
'/ZprimeToA0hToA0chichihbb_2HDM_MZp-1700_MA0-800_13TeV-madgraph':('ZpA0h_med-1700_dm-800','MC',1),
'/ZprimeToA0hToA0chichihbb_2HDM_MZp-1700_MA0-700_13TeV-madgraph':('ZpA0h_med-1700_dm-700','MC',1),
'/ZprimeToA0hToA0chichihbb_2HDM_MZp-1700_MA0-600_13TeV-madgraph':('ZpA0h_med-1700_dm-600','MC',1),
'/ZprimeToA0hToA0chichihbb_2HDM_MZp-1700_MA0-500_13TeV-madgraph':('ZpA0h_med-1700_dm-500','MC',1),
'/ZprimeToA0hToA0chichihbb_2HDM_MZp-1700_MA0-300_13TeV-madgraph':('ZpA0h_med-1700_dm-300','MC',1),
'/ZprimeToA0hToA0chichihbb_2HDM_MZp-1400_MA0-800_13TeV-madgraph':('ZpA0h_med-1400_dm-800','MC',1),
'/ZprimeToA0hToA0chichihbb_2HDM_MZp-1400_MA0-700_13TeV-madgraph':('ZpA0h_med-1400_dm-700','MC',1),
'/ZprimeToA0hToA0chichihbb_2HDM_MZp-1400_MA0-600_13TeV-madgraph':('ZpA0h_med-1400_dm-600','MC',1),
'/ZprimeToA0hToA0chichihbb_2HDM_MZp-1400_MA0-400_13TeV-madgraph':('ZpA0h_med-1400_dm-400','MC',1),
'/ZprimeToA0hToA0chichihbb_2HDM_MZp-1400_MA0-300_13TeV-madgraph':('ZpA0h_med-1400_dm-300','MC',1),
'/ZprimeToA0hToA0chichihbb_2HDM_MZp-1200_MA0-800_13TeV-madgraph':('ZpA0h_med-1200_dm-800','MC',1),
'/ZprimeToA0hToA0chichihbb_2HDM_MZp-1200_MA0-700_13TeV-madgraph':('ZpA0h_med-1200_dm-700','MC',1),
'/ZprimeToA0hToA0chichihbb_2HDM_MZp-1200_MA0-600_13TeV-madgraph':('ZpA0h_med-1200_dm-600','MC',1),
'/ZprimeToA0hToA0chichihbb_2HDM_MZp-1200_MA0-500_13TeV-madgraph':('ZpA0h_med-1200_dm-500','MC',1),
'/ZprimeToA0hToA0chichihbb_2HDM_MZp-1200_MA0-400_13TeV-madgraph':('ZpA0h_med-1200_dm-400','MC',1),
'/ZprimeToA0hToA0chichihbb_2HDM_MZp-1000_MA0-800_13TeV-madgraph':('ZpA0h_med-1000_dm-800','MC',1),
'/ZprimeToA0hToA0chichihbb_2HDM_MZp-1000_MA0-700_13TeV-madgraph':('ZpA0h_med-1000_dm-700','MC',1),
'/ZprimeToA0hToA0chichihbb_2HDM_MZp-1000_MA0-600_13TeV-madgraph':('ZpA0h_med-1000_dm-600','MC',1),
'/ZprimeToA0hToA0chichihbb_2HDM_MZp-1000_MA0-500_13TeV-madgraph':('ZpA0h_med-1000_dm-500','MC',1),
'/ZprimeToA0hToA0chichihbb_2HDM_MZp-1000_MA0-400_13TeV-madgraph':('ZpA0h_med-1000_dm-400','MC',1),
'/ZprimeToA0hToA0chichihbb_2HDM_MZp-1000_MA0-300_13TeV-madgraph':('ZpA0h_med-1000_dm-300','MC',1),




'ZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8':('ZHbb_mH125','MC',0.1),
'ggZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8':('ggZHbb_mH125','MC',0.012),
'WminusH_HToBB_WToLNu_M125_13TeV_powheg_pythia8':('WmLNuHbb','MC',0.100),
'WplusH_HToBB_WToLNu_M125_13TeV_powheg_pythia8':('WpLNuHbb','MC',0.159),

						}
