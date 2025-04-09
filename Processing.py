import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from warnings import filterwarnings
import glob
import os
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression

dataframe1 = pd.read_csv('evdata Table V2.10.csv')
dataframe2 = dataframe1
res = list(dataframe2.columns)

mths =  ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
for z in res:
    if z == 'Quantity' or z == 'Unnamed: 10' :
        continue

    col = dataframe2[z].unique()
    dfgraph0 = pd.DataFrame({'MTH': mths})
    for i in col:
        dfgraph0[i] =0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
        for n in dfgraph0['MTH']:
            totsum = dataframe2.loc[(dataframe2['Month']== n) & (dataframe2[z] == i ), 'Quantity'].sum()
            dfgraph0.loc[dfgraph0['MTH'] == n, i] = totsum
    
    dfgraph0 = dfgraph0.loc[:,(dfgraph0 != 0).any(axis = 0)]
    dfgraph0 = dfgraph0[dfgraph0.drop(columns='MTH').sum(axis=1) != 0]
    dfgraph0.to_csv(z + "MonthEVdf.csv", index=False)

counties = dataframe2['County'].unique()
for z in res:
    if z == 'Quantity' or z == 'Unnamed: 10' :
        continue
    col = dataframe2[z].unique()
    #engines = dataframe2['Engine'].unique()
    dfgraph1 = pd.DataFrame({'County':counties})
    for x in col:
        dfgraph1[x] = 0
        for n in dfgraph1['County']:
            sumToT = dataframe2.loc[(dataframe2['County']== n) & (dataframe2[z] == x), 'Quantity'].sum()
            dfgraph1.loc[dfgraph1['County'] == n, x] = sumToT

    dfgraph1 = dfgraph1.loc[:,(dfgraph1 != 0).any(axis = 0)]
    dfgraph1 = dfgraph1[dfgraph1.drop(columns='County').sum(axis=1) != 0]
    dfgraph1 = dfgraph1.sort_values(by=dfgraph1.columns[0])
    dfgraph1.to_csv(z + "CountyEVdf.csv",index=False)

print('done')


#---------------------------------------------------------------------------------
# combining columns and dropping others

# df = pd.read_csv('evdata Table V2.10.csv')
# values_to_remove = ['petrol electric (hybrid)', 'diesel electric (hybrid)']
# df_clean = df[~df['Engine'].isin(values_to_remove)]
# df_clean = df_clean.dropna(how='all')                                                                                                                                                                                                                  
# df_clean['Transmission'] = df['Transmission'].str.strip().replace(r'ctb\s*/\s*linear gear', 'automatic', regex=True)

dfCensus = pd.read_csv('AdminCounty2022.csv')
dfCensus = dfCensus[['County','T1_1AGE18M','T1_1AGE19M','T1_1AGE20_24M','T1_1AGE25_29M',
                     'T1_1AGE30_34M','T1_1AGE35_39M','T1_1AGE40_44M','T1_1AGE45_49M',
                     'T1_1AGE50_54M','T1_1AGE55_59M','T1_1AGE60_64M','T1_1AGE65_69M',
                     'T1_1AGE70_74M','T1_1AGE75_79M','T1_1AGE80_84M','T1_1AGEGE_85M',
                     'T1_1AGE18F','T1_1AGE19F','T1_1AGE20_24F','T1_1AGE30_34F',
                     'T1_1AGE35_39F','T1_1AGE40_44F','T1_1AGE25_29F','T1_1AGE45_49F',
                     'T1_1AGE50_54F','T1_1AGE55_59F','T1_1AGE60_64F','T1_1AGE65_69F',
                     'T1_1AGE70_74F','T1_1AGE75_79F','T1_1AGE80_84F','T1_1AGEGE_85F',
                     'T1_1AGE18T','T1_1AGE19T','T1_1AGE20_24T','T1_1AGE25_29T',
                     'T1_1AGE30_34T','T1_1AGE35_39T','T1_1AGE40_44T','T1_1AGE45_49T',
                     'T1_1AGE50_54T','T1_1AGE55_59T','T1_1AGE60_64T','T1_1AGE65_69T',
                     'T1_1AGE70_74T','T1_1AGE75_79T','T1_1AGE80_84T','T1_1AGEGE_85T',
                     'T6_1_HB_H','T6_1_FA_H','T6_1_BS_H','T6_1_CM_H','T6_1_TH',
                     'T6_1_HB_P','T6_1_FA_P','T6_1_BS_P','T6_1_CM_P','T6_1_TP',
                     'T6_3_OMLH','T6_3_OOH','T6_3_RPLH','T6_3_RLAH','T6_3_RVCHBH',
                     'T6_3_OFRH','T6_3_NSH','T6_3_TH','T6_3_OMLP','T6_3_OOP',
                     'T6_3_RPLP','T6_3_RLAP','T6_3_RVCHBP','T6_3_OFRP','T6_3_NSP',
                     'T6_3_TP','T6_10_NORE','T6_10_RE','T6_10_NS','T6_10_T',
                     'T10_4_NFT','T10_4_PT','T10_4_LST','T10_4_UST','T10_4_TVT',
                     'T10_4_ACCAT','T10_4_HCT','T10_4_ODNDT','T10_4_HDPQT','T10_4_PDT',
                     'T10_4_DT','T10_4_NST','T10_4_TT','T9_2_HA','T9_2_HB','T9_2_HC',
                     'T9_2_HD','T9_2_HE','T9_2_HF','T9_2_HG','T9_2_HH','T9_2_HI',
                     'T9_2_HJ','T9_2_HZ','T9_2_HT','T9_2_PA','T9_2_PB','T9_2_PC',
                     'T9_2_PD','T9_2_PE','T9_2_PF','T9_2_PG','T9_2_PH','T9_2_PI',
                     'T9_2_PJ','T9_2_PZ','T9_2_PT','T11_1_FW','T11_1_BIW','T11_1_BUW',
                     'T11_1_TDLW','T11_1_MW','T11_1_CDW','T11_1_CPW','T11_1_VW',
                     'T11_1_OTHW','T11_1_WMFHW','T11_1_NSW','T11_1_TW','T11_1_FSCCC',
                     'T11_1_BISCCC','T11_1_BUSCCC','T11_1_TDLSCCC','T11_1_MSCCC',
                     'T11_1_CDSCCC','T11_1_CPSCCC','T11_1_VSCCC','T11_1_OTHSCCC',
                     'T11_1_WMFHSCCC','T11_1_NSSCCC','T11_1_TSCCC','T11_1_FT',
                     'T11_1_BIT','T11_1_BUT','T11_1_TDLT','T11_1_MT','T11_1_CDT',
                     'T11_1_CPT','T11_1_VT','T11_1_OTHT','T11_1_WMFHT','T11_1_NST',
                     'T11_1_TT','T15_1_NC','T15_1_1C','T15_1_2C','T15_1_3C',
                     'T15_1_GE4C','T15_1_NSC','T15_1_TC']]

# Define the columns to sum
male_age_cols = ['T1_1AGE18M','T1_1AGE19M','T1_1AGE20_24M','T1_1AGE25_29M',
                 'T1_1AGE30_34M','T1_1AGE35_39M','T1_1AGE40_44M','T1_1AGE45_49M',
                 'T1_1AGE50_54M','T1_1AGE55_59M','T1_1AGE60_64M','T1_1AGE65_69M',
                 'T1_1AGE70_74M','T1_1AGE75_79M','T1_1AGE80_84M','T1_1AGEGE_85M']

female_age_cols = ['T1_1AGE18F','T1_1AGE19F','T1_1AGE20_24F','T1_1AGE30_34F',
                   'T1_1AGE35_39F','T1_1AGE40_44F','T1_1AGE25_29F','T1_1AGE45_49F',
                   'T1_1AGE50_54F','T1_1AGE55_59F','T1_1AGE60_64F','T1_1AGE65_69F',
                   'T1_1AGE70_74F','T1_1AGE75_79F','T1_1AGE80_84F','T1_1AGEGE_85F']

# Create the new column with the sum
dfCensus['Total_Males_18plus'] = dfCensus[male_age_cols].sum(axis=1)
dfCensus['Total_Females_18plus'] = dfCensus[female_age_cols].sum(axis=1)

# Drop the original columns used for the sum
dfCensus2 = dfCensus.drop(columns=male_age_cols)
dfCensus2 = dfCensus.drop(columns=female_age_cols)

# Save the final combined dataframe
dfCensus2.to_csv("Census2022V2.0.csv", index=False)

# Find all relevant County CSVs in the current directory
csv_files = glob.glob("*CountyEVdf.csv")
csv_files = [f for f in csv_files if os.path.basename(f) != "CountyCountyEVdf.csv"]

# Start with the first file
combined_df = pd.read_csv(csv_files[0])

# Merge the rest on 'County', avoiding duplication
for file in csv_files[1:]:
    df = pd.read_csv(file)
    # Drop 'County' from the new df before merging to avoid duplication
    df = df.drop(columns=['County'])
    combined_df = pd.concat([combined_df, df], axis=1)

# Save the final combined dataframe
combined_df.to_csv("Combined_CountyEVdf.csv", index=False)

print("Combined County DataFrame saved as Combined_CountyEVdf.csv")

#----------------------------------------------------------------------------------------
# Normalising the census data

dfCensus = pd.read_csv('AdminCounty2022.csv')
dfCensus = dfCensus[['County',
                #Table 1: Population aged persons aged 20 years and over by sex and age group
                     'T1_1AGE20_24M','T1_1AGE25_29M','T1_1AGE30_34M','T1_1AGE35_39M',
                     'T1_1AGE40_44M','T1_1AGE45_49M','T1_1AGE50_54M','T1_1AGE55_59M',
                     'T1_1AGE60_64M','T1_1AGE65_69M','T1_1AGE70_74M','T1_1AGE75_79M',
                     'T1_1AGE80_84M','T1_1AGEGE_85M','T1_1AGETM',
                     
                 #Table 1: Population aged persons aged 20 years and over by sex and age group
                     'T1_1AGE20_24F','T1_1AGE30_34F',
                     'T1_1AGE35_39F','T1_1AGE40_44F','T1_1AGE25_29F','T1_1AGE45_49F',
                     'T1_1AGE50_54F','T1_1AGE55_59F','T1_1AGE60_64F','T1_1AGE65_69F',
                     'T1_1AGE70_74F','T1_1AGE75_79F','T1_1AGE80_84F','T1_1AGEGE_85F',
                     'T1_1AGETF',

                #Table 1: Population aged persons aged 20 years and over by sex and age group
                     'T1_1AGE20_24T','T1_1AGE25_29T','T1_1AGE30_34T','T1_1AGE35_39T',
                     'T1_1AGE40_44T','T1_1AGE45_49T','T1_1AGE50_54T','T1_1AGE55_59T',
                     'T1_1AGE60_64T','T1_1AGE65_69T','T1_1AGE70_74T','T1_1AGE75_79T',
                     'T1_1AGE80_84T','T1_1AGEGE_85T','T1_1AGETT',

                #Table 1: Private households by type of accommodation (households)
                     'T6_1_HB_H','T6_1_FA_H','T6_1_BS_H','T6_1_CM_H','T6_1_TH',
                #Table 1: Private households by type of accommodation (No.persons)
                     'T6_1_HB_P','T6_1_FA_P','T6_1_BS_P','T6_1_CM_P','T6_1_TP',

                #Table 3: Permanent private households by type of occupancy (households)
                     'T6_3_OMLH','T6_3_OOH','T6_3_RPLH','T6_3_RLAH','T6_3_RVCHBH',
                     'T6_3_OFRH','T6_3_TH',
                #Table 3: Permanent private households by type of occupancy (No.persons)     
                     'T6_3_OMLP','T6_3_OOP','T6_3_RPLP','T6_3_RLAP','T6_3_RVCHBP',
                     'T6_3_OFRP','T6_3_TP',

                #Table 10: Permanent private households by number of renewables (households)     
                     'T6_10_NORE','T6_10_RE','T6_10_T',

                #Table 4: Population aged 15 years and over by sex and highest level of education completed 
                     'T10_4_NFT','T10_4_PT','T10_4_LST','T10_4_UST','T10_4_TVT',
                     'T10_4_ACCAT','T10_4_HCT','T10_4_ODNDT','T10_4_HDPQT','T10_4_PDT',
                     'T10_4_DT','T10_4_TT',
                       
                #Table 2: Persons in private households by socio-economic group of reference person (households)
                     'T9_2_HA','T9_2_HB','T9_2_HC','T9_2_HD','T9_2_HE','T9_2_HF',
                     'T9_2_HG','T9_2_HH','T9_2_HI','T9_2_HJ','T9_2_HT',  
                #Table 2: Persons in private households by socio-economic group of reference person (No.Persons)     
                     'T9_2_PA','T9_2_PB','T9_2_PC','T9_2_PD','T9_2_PE','T9_2_PF',
                     'T9_2_PG','T9_2_PH','T9_2_PI','T9_2_PJ','T9_2_PT',
                     
                #Table 1: Population aged 5 years and over by means of travel to work     
                     'T11_1_FW','T11_1_BIW','T11_1_BUW','T11_1_TDLW','T11_1_CDW',
                     'T11_1_TW',
                #Table 1: Population aged 5 years and over by means of travel to school or college     
                     'T11_1_FSCCC','T11_1_BISCCC','T11_1_BUSCCC','T11_1_TDLSCCC',
                     'T11_1_CDSCCC','T11_1_TSCCC',
                #Table 1: Total Population aged 5 years and over by means of travel to work, school or college
                     'T11_1_FT','T11_1_BIT','T11_1_BUT','T11_1_TDLT','T11_1_CDT',
                     'T11_1_TT',

                #Table 1: Number of households with cars
                     'T15_1_1C','T15_1_2C','T15_1_3C',
                     'T15_1_GE4C','T15_1_TC']]

# Define the columns to sum
male_age_cols = ['T1_1AGE20_24M','T1_1AGE25_29M',
                 'T1_1AGE30_34M','T1_1AGE35_39M','T1_1AGE40_44M','T1_1AGE45_49M',
                 'T1_1AGE50_54M','T1_1AGE55_59M','T1_1AGE60_64M','T1_1AGE65_69M',
                 'T1_1AGE70_74M','T1_1AGE75_79M','T1_1AGE80_84M','T1_1AGEGE_85M']

female_age_cols = ['T1_1AGE20_24F','T1_1AGE30_34F',
                   'T1_1AGE35_39F','T1_1AGE40_44F','T1_1AGE25_29F','T1_1AGE45_49F',
                   'T1_1AGE50_54F','T1_1AGE55_59F','T1_1AGE60_64F','T1_1AGE65_69F',
                   'T1_1AGE70_74F','T1_1AGE75_79F','T1_1AGE80_84F','T1_1AGEGE_85F']

plus2_car_cols = ['T15_1_2C','T15_1_3C','T15_1_GE4C']
activeT = ['T11_1_FT','T11_1_BIT']
pT = ['T11_1_BUT','T11_1_TDLT']

# Create the new column with the sum
dfCensus['Total_Males_20plus'] = dfCensus[male_age_cols].sum(axis=1)
dfCensus['Total_Females_20plus'] = dfCensus[female_age_cols].sum(axis=1)
dfCensus['T11_1_ACT'] = dfCensus[activeT].sum(axis=1)
dfCensus['T11_1_PUT'] = dfCensus[pT].sum(axis=1)
dfCensus['T15_1_2C+'] = dfCensus[plus2_car_cols].sum(axis=1)

# Drop the original columns used for the sum
dfCensus2 = dfCensus.drop(columns=male_age_cols)
dfCensus2 = dfCensus2.drop(columns=female_age_cols)
dfCensus2 = dfCensus2.drop(columns=plus2_car_cols)
dfCensus2 = dfCensus2.drop(columns=activeT)
dfCensus2 = dfCensus2.drop(columns=pT)
dfCensus2 = dfCensus2.drop(columns='County')

#normalise each column
all_cols = dfCensus2.columns

#Table 1: Population aged 18+ by sex
dfCensus2['%Total_Males_20plus']  = (dfCensus2['Total_Males_20plus'] /dfCensus2['T1_1AGETM'])*100
dfCensus2['%Total_Females_20plus'] = (dfCensus2['Total_Females_20plus']/dfCensus2['T1_1AGETF'])*100

#Table 1: Population aged 18 - 19 by sex and year of age, persons aged 20 years and over by sex and age group
dfCensus2['%T1_1AGE20_24T'] = (dfCensus2['T1_1AGE20_24T']/dfCensus2['T1_1AGETT'])*100
dfCensus2['%T1_1AGE25_29T'] = (dfCensus2['T1_1AGE25_29T']/dfCensus2['T1_1AGETT'])*100
dfCensus2['%T1_1AGE30_34T'] = (dfCensus2['T1_1AGE30_34T']/dfCensus2['T1_1AGETT'])*100
dfCensus2['%T1_1AGE35_39T'] = (dfCensus2['T1_1AGE35_39T']/dfCensus2['T1_1AGETT'])*100
dfCensus2['%T1_1AGE40_44T'] = (dfCensus2['T1_1AGE40_44T']/dfCensus2['T1_1AGETT'])*100
dfCensus2['%T1_1AGE45_49T'] = (dfCensus2['T1_1AGE45_49T']/dfCensus2['T1_1AGETT'])*100
dfCensus2['%T1_1AGE50_54T'] = (dfCensus2['T1_1AGE50_54T']/dfCensus2['T1_1AGETT'])*100
dfCensus2['%T1_1AGE55_59T'] = (dfCensus2['T1_1AGE55_59T']/dfCensus2['T1_1AGETT'])*100
dfCensus2['%T1_1AGE60_64T'] = (dfCensus2['T1_1AGE60_64T']/dfCensus2['T1_1AGETT'])*100
dfCensus2['%T1_1AGE65_69T'] = (dfCensus2['T1_1AGE65_69T']/dfCensus2['T1_1AGETT'])*100
dfCensus2['%T1_1AGE70_74T'] = (dfCensus2['T1_1AGE70_74T']/dfCensus2['T1_1AGETT'])*100
dfCensus2['%T1_1AGE75_79T'] = (dfCensus2['T1_1AGE75_79T']/dfCensus2['T1_1AGETT'])*100
dfCensus2['%T1_1AGE80_84T'] = (dfCensus2['T1_1AGE80_84T']/dfCensus2['T1_1AGETT'])*100
dfCensus2['%T1_1AGEGE_85T'] = (dfCensus2['T1_1AGEGE_85T']/dfCensus2['T1_1AGETT'])*100

#Table 1: Private households by type of accommodation (households)
dfCensus2['%T6_1_HB_H'] = (dfCensus2['T6_1_HB_H']/dfCensus2['T6_1_TH'])*100
dfCensus2['%T6_1_FA_H'] = (dfCensus2['T6_1_FA_H']/dfCensus2['T6_1_TH'])*100
dfCensus2['%T6_1_BS_H'] = (dfCensus2['T6_1_BS_H']/dfCensus2['T6_1_TH'])*100
dfCensus2['%T6_1_CM_H'] = (dfCensus2['T6_1_CM_H']/dfCensus2['T6_1_TH'])*100
#Table 1: Private households by type of accommodation (No.persons)
dfCensus2['%T6_1_HB_P'] = (dfCensus2['T6_1_HB_P']/dfCensus2['T6_1_TP'])*100
dfCensus2['%T6_1_FA_P'] = (dfCensus2['T6_1_FA_P']/dfCensus2['T6_1_TP'])*100
dfCensus2['%T6_1_BS_P'] = (dfCensus2['T6_1_BS_P']/dfCensus2['T6_1_TP'])*100
dfCensus2['%T6_1_CM_P'] = (dfCensus2['T6_1_CM_P']/dfCensus2['T6_1_TP'])*100

#Table 3: Permanent private households by type of occupancy (households)
dfCensus2['%T6_3_OMLH']   = (dfCensus2['T6_3_OMLH']  /dfCensus2['T6_3_TH'])*100
dfCensus2['%T6_3_OOH']    = (dfCensus2['T6_3_OOH']   /dfCensus2['T6_3_TH'])*100
dfCensus2['%T6_3_RPLH']   = (dfCensus2['T6_3_RPLH']  /dfCensus2['T6_3_TH'])*100
dfCensus2['%T6_3_RLAH']   = (dfCensus2['T6_3_RLAH']  /dfCensus2['T6_3_TH'])*100
dfCensus2['%T6_3_RVCHBH'] = (dfCensus2['T6_3_RVCHBH']/dfCensus2['T6_3_TH'])*100
dfCensus2['%T6_3_OFRH']   = (dfCensus2['T6_3_OFRH']  /dfCensus2['T6_3_TH'])*100

#Table 3: Permanent private households by type of occupancy (No.persons)   
dfCensus2['%T6_3_OMLP']   = (dfCensus2['T6_3_OMLP']  /dfCensus2['T6_3_TP'])*100
dfCensus2['%T6_3_OOP']    = (dfCensus2['T6_3_OOP']   /dfCensus2['T6_3_TP'])*100
dfCensus2['%T6_3_RPLP']   = (dfCensus2['T6_3_RPLP']  /dfCensus2['T6_3_TP'])*100
dfCensus2['%T6_3_RLAP']   = (dfCensus2['T6_3_RLAP']  /dfCensus2['T6_3_TP'])*100
dfCensus2['%T6_3_RVCHBP'] = (dfCensus2['T6_3_RVCHBP']/dfCensus2['T6_3_TP'])*100
dfCensus2['%T6_3_OFRP']   = (dfCensus2['T6_3_OFRP']  /dfCensus2['T6_3_TP'])*100

#Table 10: Permanent private households by number of renewables (households) 
dfCensus2['%T6_10_NORE'] = (dfCensus2['T6_10_NORE']/dfCensus2['T6_10_T'])*100
dfCensus2['%T6_10_RE']   = (dfCensus2['T6_10_RE']  /dfCensus2['T6_10_T'])*100   

#Table 4: Population aged 15 years and over by sex and highest level of education completed 
dfCensus2['%T10_4_NFT']   = (dfCensus2['T10_4_NFT']  /dfCensus2['T10_4_TT'])*100
dfCensus2['%T10_4_PT']    = (dfCensus2['T10_4_PT']   /dfCensus2['T10_4_TT'])*100   
dfCensus2['%T10_4_LST']   = (dfCensus2['T10_4_LST']  /dfCensus2['T10_4_TT'])*100
dfCensus2['%T10_4_UST']   = (dfCensus2['T10_4_UST']  /dfCensus2['T10_4_TT'])*100   
dfCensus2['%T10_4_TVT']   = (dfCensus2['T10_4_TVT']  /dfCensus2['T10_4_TT'])*100
dfCensus2['%T10_4_ACCAT'] = (dfCensus2['T10_4_ACCAT']/dfCensus2['T10_4_TT'])*100   
dfCensus2['%T10_4_HCT']   = (dfCensus2['T10_4_HCT']  /dfCensus2['T10_4_TT'])*100
dfCensus2['%T10_4_ODNDT'] = (dfCensus2['T10_4_ODNDT']/dfCensus2['T10_4_TT'])*100   
dfCensus2['%T10_4_HDPQT'] = (dfCensus2['T10_4_HDPQT']/dfCensus2['T10_4_TT'])*100
dfCensus2['%T10_4_PDT']   = (dfCensus2['T10_4_PDT']  /dfCensus2['T10_4_TT'])*100 
dfCensus2['%T10_4_DT']    = (dfCensus2['T10_4_DT']   /dfCensus2['T10_4_TT'])*100  
                  
#Table 2: Persons in private households by socio-economic group of reference person (households)
dfCensus2['%T9_2_HA'] = (dfCensus2['T9_2_HA']/dfCensus2['T9_2_HT'])*100
dfCensus2['%T9_2_HB'] = (dfCensus2['T9_2_HB']/dfCensus2['T9_2_HT'])*100
dfCensus2['%T9_2_HC'] = (dfCensus2['T9_2_HC']/dfCensus2['T9_2_HT'])*100
dfCensus2['%T9_2_HD'] = (dfCensus2['T9_2_HD']/dfCensus2['T9_2_HT'])*100
dfCensus2['%T9_2_HE'] = (dfCensus2['T9_2_HE']/dfCensus2['T9_2_HT'])*100
dfCensus2['%T9_2_HF'] = (dfCensus2['T9_2_HF']/dfCensus2['T9_2_HT'])*100
dfCensus2['%T9_2_HG'] = (dfCensus2['T9_2_HG']/dfCensus2['T9_2_HT'])*100
dfCensus2['%T9_2_HH'] = (dfCensus2['T9_2_HH']/dfCensus2['T9_2_HT'])*100
dfCensus2['%T9_2_HI'] = (dfCensus2['T9_2_HI']/dfCensus2['T9_2_HT'])*100
dfCensus2['%T9_2_HJ'] = (dfCensus2['T9_2_HJ']/dfCensus2['T9_2_HT'])*100

#Table 2: Persons in private households by socio-economic group of reference person (No.Persons)     
dfCensus2['%T9_2_PA'] = (dfCensus2['T9_2_PA']/dfCensus2['T9_2_PT'])*100
dfCensus2['%T9_2_PB'] = (dfCensus2['T9_2_PB']/dfCensus2['T9_2_PT'])*100
dfCensus2['%T9_2_PC'] = (dfCensus2['T9_2_PC']/dfCensus2['T9_2_PT'])*100
dfCensus2['%T9_2_PD'] = (dfCensus2['T9_2_PD']/dfCensus2['T9_2_PT'])*100
dfCensus2['%T9_2_PE'] = (dfCensus2['T9_2_PE']/dfCensus2['T9_2_PT'])*100
dfCensus2['%T9_2_PF'] = (dfCensus2['T9_2_PF']/dfCensus2['T9_2_PT'])*100
dfCensus2['%T9_2_PG'] = (dfCensus2['T9_2_PG']/dfCensus2['T9_2_PT'])*100
dfCensus2['%T9_2_PH'] = (dfCensus2['T9_2_PH']/dfCensus2['T9_2_PT'])*100
dfCensus2['%T9_2_PI'] = (dfCensus2['T9_2_PI']/dfCensus2['T9_2_PT'])*100
dfCensus2['%T9_2_PJ'] = (dfCensus2['T9_2_PJ']/dfCensus2['T9_2_PT'])*100 
 
#Table 1: Population aged 5 years and over by means of travel to work     
dfCensus2['%T11_1_FW']   = (dfCensus2['T11_1_FW']   /dfCensus2['T11_1_TW'])*100
dfCensus2['%T11_1_BIW']  = (dfCensus2['T11_1_BIW']  /dfCensus2['T11_1_TW'])*100
dfCensus2['%T11_1_BUW']  = (dfCensus2['T11_1_BUW']  /dfCensus2['T11_1_TW'])*100
dfCensus2['%T11_1_TDLW'] = (dfCensus2['T11_1_TDLW'] /dfCensus2['T11_1_TW'])*100
dfCensus2['%T11_1_CDW']  = (dfCensus2['T11_1_CDW']  /dfCensus2['T11_1_TW'])*100
 
#Table 1: Population aged 5 years and over by means of travel to school or college   
dfCensus2['%T11_1_FSCCC']   = (dfCensus2['T11_1_FSCCC']   /dfCensus2['T11_1_TSCCC'])*100
dfCensus2['%T11_1_BISCCC']  = (dfCensus2['T11_1_BISCCC']  /dfCensus2['T11_1_TSCCC'])*100
dfCensus2['%T11_1_BUSCCC']  = (dfCensus2['T11_1_BUSCCC']  /dfCensus2['T11_1_TSCCC'])*100
dfCensus2['%T11_1_TDLSCCC'] = (dfCensus2['T11_1_TDLSCCC'] /dfCensus2['T11_1_TSCCC'])*100
dfCensus2['%T11_1_CDSCCC']  = (dfCensus2['T11_1_CDSCCC']  /dfCensus2['T11_1_TSCCC'])*100   
                    
#Table 1: Total Population aged 5 years and over by means of travel to work, school or college
dfCensus2['%T11_1_ACT'] = (dfCensus2['T11_1_ACT']/dfCensus2['T11_1_TT'])*100
dfCensus2['%T11_1_PUT'] = (dfCensus2['T11_1_PUT']/dfCensus2['T11_1_TT'])*100
dfCensus2['%T11_1_CDT'] = (dfCensus2['T11_1_CDT']/dfCensus2['T11_1_TT'])*100
  
#Table 1: Number of households with cars
dfCensus2['%T15_1_1C']  = (dfCensus2['T15_1_1C'] /dfCensus2['T15_1_TC'])*100
dfCensus2['%T15_1_2C+'] = (dfCensus2['T15_1_2C+']/dfCensus2['T15_1_TC'])*100

#Total BEVs
dfTregCars = pd.read_excel('passenger-cars-by-county.xlsx')
dfCountyBEVs = pd.read_csv('Combined_CountyEVdf.csv')
dfCensus2['%Total BEVs'] = (dfCountyBEVs['2024']/dfTregCars['2024 Units'])*100

# Drop the original columns used for the normalising
dfCensus2 = dfCensus2.drop(columns=all_cols)

# Save the final combined dataframe
dfCensus2.to_csv("Census2022V3.0Normalised.csv", index=False)
