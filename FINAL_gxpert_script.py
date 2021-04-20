# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 12:20:24 2019
"""
Purpose of this script is to read CSV files created by a GeneXpert instrument or any instrument really displaying the number of samples run along with 
every month or year. The script reads a big mess of info in the CSV and processes it neatly into tables with clearly defined headers that allows
the lab manager to easily visualise different types of information such as how many samples for a particular test were performed each month of a year.
This is quite a useful little script as it allows a lab manager to make better data driven decisions.
"""
@author: PCR Gen
"""

""
import pandas as pd
import csv



in_csv = r'C:\Users\S10749User\Desktop\scr\Input\D\June 2019\TB Ultra GeneXpert D June 2019.csv'
headers = ['Sample ID', 'Test Result', 'Module Name', 'Module S/N', 'Instrument S/N', 'Reagent Lot ID', 'Expiration Date',  'User' ]
df = pd.DataFrame(columns=headers)
output_file = r'C:\Users\S10749User\Desktop\scr\Output\D\June 2019\TB Ultra GeneXpert D June 2019.xlsx'

with open(in_csv, 'r') as mycsv:
	reader = csv.reader(x.replace('\0', '') for x in mycsv)
	for row in reader:
		if row:
			for i, v in enumerate(headers):
				if row[0] == v:
					if i == 0:
						sample = {}
					if v not in sample.keys():
						sample[v] = row[1]
					if i == len(headers) - 1:
#						print(sample)
						df = df.append(sample, ignore_index=True)
						del sample
						
print(df.head())

df.to_excel(output_file)		   	
   