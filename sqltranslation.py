
"""
Created on Sun Jun  3 18:06:45 2018

@author: mirakraju

This is the code I was able to write from the SQL file. The only two tables that were independent of treatment id and patient id were "alldata2" and "txpro4"
I was able to create these tables. Their column values orginate from the original data, however that can be altered simply by changing the dataframe
specified in the "get columns from original data" sections. 

If you have any other questions, please email me. 

- Mira
"""
import pandas as pd
import math

#original data table from csv

df = pd.read_csv('sdp.csv')

#alldata2 initialization
 
alldata2 = pd.DataFrame()

#create new lists to turn into columns

loctype= []
maxsize = []
largesize=[]
lgsize=[]
gt10size=[]
hounsunit = []
eswl_fluro_time_min2 = []
eswl_fluro_time_sec2 = []
xraytime = []
xraysec = []

#get columns from original data

stonloc = df["stone_location"].tolist()
sw = df["stone_width"].tolist();
sh = df["stone_height"].tolist();
houns_unit = df["houns_unit"].tolist();
eswl_fluro_time_sec = df["eswl_fluro_time_sec"].tolist();
eswl_fluro_time_min = df["eswl_fluro_time_min"].tolist();

#add elements to new lists

for i in range(len(sw)):
    a = max(sw[i], sh[i])
    maxsize.append(a)
    
alldata2.fillna(0)

for i in maxsize:
    if i>=14:
        largesize.append(1)
        lgsize.append(1)
    else:
        largesize.append(0)
        lgsize.append(0)
    if i > 10:
        gt10size.append(1)
    else:
        gt10size.append(0)
        
for s in stonloc:
    if s == 'UVJ' or s == 'MU' or s == 'LU' or s=='UU':
        loctype.append('Ureteral')
    elif s == 'UC' or s =='MC' or s=='LC' or s=='P' or s=='UPJ':
        loctype.append('Renal')
    elif s=='Staghorn' or s=='Bladder' or s=='PD':
        loctype.append('Other')
    else:
        loctype.append('Other')

for a in houns_unit:
    if math.isnan(a):
        hounsunit.append(" ")
    else:
        hounsunit.append("%.0f"%a);
        
for a in eswl_fluro_time_min:
    e = int(round(a))
    eswl_fluro_time_min2.append(a)

for a in eswl_fluro_time_sec:
    e = int(round(a))
    eswl_fluro_time_sec2.append(a)
    
for a in range(len(eswl_fluro_time_sec2)):
    b = eswl_fluro_time_min[a]
    c = eswl_fluro_time_sec[a]
    xraytime.append(b+(c/100))
    xraysec.append((b*60)+c)
    
#set the alldata2 columns
        
alldata2['largesize'] = largesize
alldata2['lgsize'] = lgsize
alldata2['gt10size'] = gt10size
alldata2['maxsize'] = maxsize
alldata2['loctype'] = loctype
alldata2['houns_unit'] = hounsunit  
alldata2["eswl_fluro_time_min2"] = eswl_fluro_time_min2
alldata2["eswl_fluro_time_sec2"] = eswl_fluro_time_sec2
alldata2["xraytime"] = xraytime
alldata2["xraysec"] = xraysec



#--------------------------------------------------------------------------------------------------------------------

    

#txpro4 table

txpro4 = pd.DataFrame()

#create lists to turn into columns for txpro4

dense = []
lowerpole = []
general = []
#anticoagulant = [] (unable to code)
#literature_success = [] (unable to code)
MAC = []
hfjv = []
consious_sedation = []
storzf2 = []
storzslxt = []
Dornierd1 = []
Dornierd2 = []
Dornierd3 = []
dorniersigma = []
lowercalyx = []
midcalyx = []
uppercalyx = []
lowerureter = []
midureter = []
upperureter =[]
pelvis = []
upj = []
uvj = []
NoKUb = []
ANovis = []
Novisconv = []
convuret = []
convuretphy = []
facarm = []
noimage = []
other = []
patcomp = []
titwaived =[] 
GTFDA = []
LT4 = []
SNP = []
Novis = []
Cancelledhos = []
cancelledpat = []
cancelledphy = []
cancelledequip = []
treatdelayhos = []
Treatdelayphy = []
Treatdelayequip = []
Treatdelayext = []
Treatdelayphyschedu = []
Treatdelaypremat = []

#get columns from original dataframe (can be changed)

ston_loc = df["stone_location"].tolist()
mt = df["machine_type"].tolist()
anes = df["anesthesia"].tolist()
var1 = df["variances1"].tolist()
var2 = df["variances2"].tolist()
var3 = df["variances3"].tolist()

#assign values to newly created lists

for i in houns_unit:
    if i>=1000:
        dense.append(2);
    elif i < 1000 and i>=900:
        dense.append(1)
    else:
        dense.append(0)

for i in ston_loc:
    if i == 'LC':
        lowerpole.append(1)
        lowercalyx.append(1)
    else:
        lowerpole.append(0)
        lowercalyx.append(0)
    if i == "MC":
        midcalyx.append(1)
    else:
        midcalyx.append(0)
    if i == "UU":
        uppercalyx.append(1)
        upperureter.append(1)
    else:
        uppercalyx.append(0)
        upperureter.append(0)
    if i == "LU":
        lowerureter.append(1)
    else:
        lowerureter.append(0)
    if i == "MU":
        midureter.append(1)
    else:
        midureter.append(0)
    if i == "P":
        pelvis.append(1)
    else:
        pelvis.append(0)
    if i == "UP":
        upj.append(1)
    else:
        upj.append(0)
    if i == "UV":
        uvj.append(1)
    else:
        uvj.append(0)


for i in anes:
    if i == "General Anesthesia":
        general.append(1)
    else:
        general.append(0)
    if i == "General HFJV":
        hfjv.append(1)
    else:
        hfjv.append(0)
    if i == "Conscious Sedation":
        consious_sedation.append(1)
    else:
        consious_sedation.append(0)
        
        
for i in mt:
    if i == "Storz F2":
        storzf2.append(1)
    else:
        storzf2.append(0)
    if i == "Storz SLX-T":
        storzslxt.append(1)
    else:
        storzslxt.append(0)
    if i == "Dornier Compact Delta I":
        Dornierd1.append(1)
    else:
        Dornierd1.append(0)
    if i == 'Dornier Compact Delta II':
        Dornierd2.append(1)
    else:
         Dornierd2.append(0)
    if i == 'Dornier Compact Delta III':
         Dornierd3.append(1)
    else:
         Dornierd3.append(0)
    if i == 'Dornier Compact Sigma':
         dorniersigma.append(1)
    else:
        dorniersigma.append(0)

for i in range(len(var1)):
    if var1[i] == 'Absence of KUB or other imaging within 48 hours' or var2[i] == 'Absence of KUB or other imaging within 48 hours' or var3[i] == 'Absence of KUB or other imaging within 48 hours':
        NoKUb.append(1)
    else:
        NoKUb.append(0)
    if var1[i] == 'Attempted due to non-visualization of stone' or var2[i] == 'Attempted due to non-visualization of stone' or var3[i] == 'Attempted due to non-visualization of stone':
        ANovis.append(1)
    else:
        ANovis.append(0)
    if var1[i] == 'Attempted due to non-visualization of stone, Converted to ureteroscopy' or var2[i] == 'Attempted due to non-visualization of stone, Converted to ureteroscopy' or var3[i] == 'Attempted due to non-visualization of stone, Converted to ureteroscopy':
        Novisconv.append(1)
    else:
        Novisconv.append(0)
    if var1[i] == 'Converted to ureteroscopy' or var2[i] == 'Converted to ureteroscopy' or var3[i] == 'Converted to ureteroscopy':
        convuret.append(1)
    else:
        convuret.append(0)
    if var1[i] == 'Converted to ureteroscopy, Treatment cancelled by physician' or var2[i] == 'Converted to ureteroscopy, Treatment cancelled by physician' or var3[i] == 'Converted to ureteroscopy, Treatment cancelled by physician':
        convuretphy.append(1)
    else:
        convuretphy.append(0)
    if var1[i] == 'Facility C-arm was used' or var2[i] == 'Facility C-arm was used' or var3[i] == 'Facility C-arm was used':
        facarm.append(1)
    else:
        facarm.append(0)
    if var1[i] == 'Lack of imaging within 48 hours' or var2[i] == 'Lack of imaging within 48 hours' or var3[i] == 'Lack of imaging within 48 hours':
        noimage.append(1)
    else:
        noimage.append(0)
    if var1[i] == 'Other' or var2[i] == 'Other' or var3[i] == 'Other':
        other.append(1)
    else:
        other.append(0)
    if var1[i] == 'Patient complaint' or var2[i] == 'Patient complaint' or var3[i] == 'Patient complaint':
        patcomp.append(1)
    else:
        patcomp.append(0)
    if var1[i] == 'Recommended titration waived' or var2[i] == 'Recommended titration waived' or var3[i] == 'Recommended titration waived':
        titwaived.append(1)
    else:
        titwaived.append(0)
    if var1[i] == 'Shocks greater than FDA recommended (3000 for Storz)' or var2[i] == 'Shocks greater than FDA recommended (3000 for Storz)' or var3[i] == 'Shocks greater than FDA recommended (3000 for Storz)':
        GTFDA.append(1)
    else:
        GTFDA.append(0)
    if var1[i] == 'Solitary Stone Less than or Equal to 4MM. Reason for Treatment Documented in Medical Record' or var2[i] == 'Solitary Stone Less than or Equal to 4MM. Reason for Treatment Documented in Medical Record' or var3[i] == 'Solitary Stone Less than or Equal to 4MM. Reason for Treatment Documented in Medical Record':
        LT4.append(1)
    else:
        LT4.append(0)
    if var1[i] == 'Special needs patient' or var2[i] == 'Special needs patient' or var3[i] == 'Special needs patient':
        SNP.append(1)
    else:
        SNP.append(0)
    if var1[i] == 'Stone treated without visualization - reason documented in MR' or var2[i] == 'Stone treated without visualization - reason documented in MR' or var3[i] == 'Stone treated without visualization - reason documented in MR':
        Novis.append(1)
    else:
        Novis.append(0)
    if var1[i] == 'Treatment cancelled by hospital' or var2[i] == 'Treatment cancelled by hospital' or var3[i] == 'Treatment cancelled by hospital':
        Cancelledhos.append(1)
    else:
        Cancelledhos.append(0)
    if var1[i] == 'Treatment cancelled by patient' or var2[i] == 'Treatment cancelled by patient' or var3[i] == 'Treatment cancelled by patient':
        cancelledpat.append(1)
    else:
        cancelledpat.append(0)
    if var1[i] == 'Treatment cancelled by physician' or var2[i] == 'Treatment cancelled by physician' or var3[i] == 'Treatment cancelled by physician':
        cancelledphy.append(1)
    else:
        cancelledphy.append(0)
    if var1[i] == 'Treatment cancelled due to equipment failure' or var2[i] == 'Treatment cancelled due to equipment failure' or var3[i] =='Treatment cancelled due to equipment failure':
        cancelledequip.append(1)
    else:
        cancelledequip.append(0)
    if var1[i] == 'Treatment delayed by hospital' or var2[i] == 'Treatment delayed by hospital' or var3[i] =='Treatment delayed by hospital':
        treatdelayhos.append(1)
    else:
        treatdelayhos.append(0)
    if var1[i] == 'Treatment delayed by physician' or var2[i] == 'Treatment delayed by physician' or var3[i] =='Treatment delayed by physician':
        Treatdelayphy.append(1)
    else:
        Treatdelayphy.append(0)
    if var1[i] == 'Treatment delayed due to equipment failure' or var2[i] == 'Treatment delayed due to equipment failure' or var3[i] == 'Treatment delayed due to equipment failure':
        Treatdelayequip.append(1)
    else:
        Treatdelayequip.append(0)
    if var1[i] == 'Treatment delayed due to extenuating circumstances' or var2[i] == 'Treatment delayed due to extenuating circumstances' or var3[i] == 'Treatment delayed due to extenuating circumstances':
        Treatdelayext.append(1)
    else:
        Treatdelayext.append(0)
    if var1[i] == 'Treatment delayed due to scheduling conflict' or var2[i] == 'Treatment delayed due to scheduling conflict' or var3[i] == 'Treatment delayed due to scheduling conflict':
        Treatdelayphyschedu.append(1)
    else:
        Treatdelayphyschedu.append(0)
    if var1[i] == 'Treatment prematurely terminated by physician' or var2[i] == 'Treatment prematurely terminated by physician' or var3[i] == 'Treatment prematurely terminated by physician':
        Treatdelaypremat.append(1)
    else:
        Treatdelaypremat.append(0)
        
#create columns for txpro4
    
txpro4["dense"] = dense
txpro4["lowerpole"] = lowerpole
txpro4["lowercalyx"] = lowercalyx
txpro4["midcalyx"] = midcalyx
txpro4["uppercalyx"] = uppercalyx
txpro4["upperureter"] = upperureter
txpro4["lowerureter"] = lowerureter
txpro4["midureter"] = midureter
txpro4["pelvis"] = pelvis
txpro4["upj"] = upj
txpro4["uvj"] = uvj
txpro4["general"] = general
txpro4["hfjv"] = hfjv
txpro4["consious_sedation"] = consious_sedation
txpro4["storzf2"] = storzf2
txpro4["storzslxt"] = storzslxt
txpro4["Dornierd1"] = Dornierd1
txpro4["Dornierd2"] = Dornierd2
txpro4["Dornierd3"] = Dornierd3
txpro4["dorniersigma"] = dorniersigma
txpro4["NoKUb"] = NoKUb
txpro4["ANovis"] = ANovis
txpro4["Novisconv"] = Novisconv
txpro4["convuret"] = convuret
txpro4["convuretphy"] = convuretphy
txpro4["facarm"] = facarm
txpro4["noimage"] = noimage
txpro4["other"] = other
txpro4["patcomp"] = patcomp
txpro4["titwaived"] = titwaived  
txpro4["GTFDA"] = GTFDA
txpro4["LT4"] = LT4
txpro4["SNP"] = SNP
txpro4["Novis"] = Novis
txpro4["Cancelledhos"] = Cancelledhos
txpro4["cancelledpat"] = cancelledpat
txpro4["cancelledphy"] = cancelledphy
txpro4["cancelledequip"] = cancelledequip
txpro4["treatdelayhos"] = treatdelayhos
txpro4["Treatdelayphy"] = Treatdelayphy
txpro4["Treatdelayequip"] = Treatdelayequip
txpro4["Treatdelayext"] = Treatdelayext
txpro4["Treatdelayphyschedu"] = Treatdelayphyschedu
txpro4["Treatdelaypremat"] = Treatdelaypremat
    

    
    
