# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 12:33:54 2019

@author: PCR Gen
"""

#This script makes it easier to determine which phenotypic resistance pattern is present in MDRTB sl assay. It especially pays attention to AG & CP resistance markers to determine the drug resistance combo.

print("For all of the following questions, please answer Yes or No.")
#For rrs AG/CP resistance determination.

tub = input("Is the TUB band present?")

if tub == "Yes":
       
       rrs_WT1 = str(input("Is the rrs WT1 band visible?"))
       rrs_WT2 = str(input("Is the rrs WT2 band visible?"))
       rrs_Mut1 = str(input("Is the rrs MUT1 band visible?"))
       rrs_Mut2 = str(input("Is the rrs MUT2 band visible?"))
       eis_WT1 = str(input("Is the eis WT1 band visible?"))
       eis_WT2 = str(input("Is the eis WT2 band visible?"))
       eis_WT3 = str(input("Is the eis WT3 band visible?"))
       eis_Mut1 =str( input("Is the eis MUT1 band visible?"))

else:
       
       print("Please repeat this sample on the next HAIN batch as M. tubercolosis is not identifiable due to a missing TUB band.")
       
#print(agcp)

if rrs_WT1 == "No":
      rrs_result = ("KAN, CAP & VIO")
      
elif rrs_Mut1 == "Yes":
       rrs_result = ("KAN, AMK & CAP") 

elif rrs_Mut2 == "Yes":
       rrs_result = ("KAN, AMK, CAP & VIO")
       
else:
       rrs_result = ("There is no AG/CP phenotypic resistance pattern.")
       

if eis_WT1 == "No": 
       eis_result = ("low level KAN resistance")

elif eis_WT2 == "No":
       eis_result = ("low level KAN resistance")

elif eis_WT3 == "No":
       eis_result = ("low level KAN resistance")
       
if eis_Mut1 == "Yes":
       eis_result = ("low level KAN resistance")
 
else:
       eis_result = ("no low level KAN phenotypic resistance pattern")
       
       
if rrs_result ==  ("KAN, AMK & CAP") :
       eis_result = ("High level KAN resistance present due to rrs phenotypic resistance pattern.")
       
elif rrs_result == ("KAN, CAP & VIO"): 
       eis_result = ("High level KAN resistance present due to rrs phenotypic resistance pattern.")
       
elif rrs_result == ("KAN, AMK, CAP & VIO"):
       eis_result = ("High level KAN resistance present due to rrs phenotypic resistance pattern.")
       
else:
       eis_result = ("There is no KAN phenotypic resistance pattern present.")
 
       
print("\nThe sample shows the following phenotypic resistance pattern for the rrs gene:\n %s" %(rrs_result))

print("\nThe sample shows the following phenotypic resistance pattern for the eis gene:\n %s" %(eis_result))
