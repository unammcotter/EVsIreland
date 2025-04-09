import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import glob
import os
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression

# df = pd.read_csv('evdata Table V2.10.csv')
# values_to_remove = ['petrol electric (hybrid)', 'diesel electric (hybrid)']
# df_clean = df[~df['Engine'].isin(values_to_remove)]
# df_clean = df_clean.dropna(how='all')                                                                                                                                                                                                                  
# df_clean['Transmission'] = df['Transmission'].str.strip().replace(r'ctb\s*/\s*linear gear', 'automatic', regex=True)
# #MERCEDES-BENZ eqs 640 - 690
#AUDI a6 etron esate/station 475 - 565
#
#AUDI etron gt 585 600
#MERCEDES-BENZ eqs amg 640 - 690
#PORSCHE taycan 575

dfCensus = pd.read_csv("Census2022V2.0.csv")
dfCensus = dfCensus[['County',
 #Table 1: Population aged 18+ by sex
                     'Total_Males_18plus', 'Total_Females_18plus',

 #Table 1: Population aged 18 - 19 by sex and year of age, persons aged 20 years and over by sex and age group
                     'T1_1AGE18T','T1_1AGE19T','T1_1AGE20_24T','T1_1AGE25_29T',
                     'T1_1AGE30_34T','T1_1AGE35_39T','T1_1AGE40_44T','T1_1AGE45_49T',
                     'T1_1AGE50_54T','T1_1AGE55_59T','T1_1AGE60_64T','T1_1AGE65_69T',
                     'T1_1AGE70_74T','T1_1AGE75_79T','T1_1AGE80_84T','T1_1AGEGE_85T',
 
 #Table 1: Private households by type of accommodation                     
                     'T6_1_HB_H','T6_1_FA_H','T6_1_BS_H','T6_1_CM_H',

 #Table 3: Permanent private households by type of occupancy                     
                     'T6_3_RPLH','T6_3_RLAH','T6_3_RVCHBH','T6_3_OFRH',

 #Table 10: Permanent private households by number of renewables                    
                     'T6_10_RE',
 
 #Table 4: Population aged 15 years and over by sex and highest level of education completed        
                     'T10_4_TVT','T10_4_ACCAT','T10_4_HCT','T10_4_ODNDT','T10_4_HDPQT',
                     'T10_4_PDT','T10_4_DT',

 #Table 2: Persons in private households by socio-economic group of reference person
                     'T9_2_HA','T9_2_HB','T9_2_HC','T9_2_HD','T9_2_HE','T9_2_HF',
                     'T9_2_HG','T9_2_HH','T9_2_HI','T9_2_HJ','T9_2_HZ',

 #Table 1: Population aged 5 years and over by means of travel to work, school or college
                     'T11_1_FW','T11_1_BIW','T11_1_BUW','T11_1_TDLW','T11_1_MW',
                     'T11_1_CDW','T11_1_CPW','T11_1_VW','T11_1_OTHW','T11_1_WMFHW',
                     'T11_1_NSW','T11_1_FT','T11_1_BIT','T11_1_BUT','T11_1_TDLT',
                     'T11_1_CDT',
                
 #Table 1: Number of households with cars
                     'T15_1_NC','T15_1_1C','T15_1_2C','T15_1_3C','T15_1_GE4C']]

plus2_car_cols = ['T15_1_2C','T15_1_3C','T15_1_GE4C']
activeT = ['T11_1_FT','T11_1_BIT']
pT = ['T11_1_BUT','T11_1_TDLT']

dfCensus['T15_1_2C+'] = dfCensus[plus2_car_cols].sum(axis=1)
dfCensus['T11_1_ACT'] = dfCensus[activeT].sum(axis=1)
dfCensus['T11_1_PUT'] = dfCensus[pT].sum(axis=1)

dfCensus2 = dfCensus.drop(columns=plus2_car_cols)
dfCensus2 = dfCensus.drop(columns=activeT)
dfCensus2 = dfCensus.drop(columns=pT)

dfBEVs = pd.read_csv("Combined_CountyEVdf.csv")
dfCensus['Total BEVs'] =  dfBEVs[['2024']]
dfCensus.drop(dfCensus.tail(1).index,
        inplace = True)

# Independent variables (features)
X = dfCensus[[#Table 1: Population aged 18+ by sex
                'Total_Males_18plus', 'Total_Females_18plus',#
                
                # #Table 1: Population aged 18 - 19 by sex and year of age, persons aged 20 years and over by sex and age group
                # 'T1_1AGE18T','T1_1AGE19T','T1_1AGE20_24T','T1_1AGE25_29T',
                # 'T1_1AGE30_34T','T1_1AGE35_39T','T1_1AGE40_44T','T1_1AGE45_49T',
                # 'T1_1AGE50_54T','T1_1AGE55_59T','T1_1AGE60_64T','T1_1AGE65_69T',
                # 'T1_1AGE70_74T','T1_1AGE75_79T','T1_1AGE80_84T','T1_1AGEGE_85T',

                # #Table 1: Private households by type of accommodation                     
                # 'T6_1_HB_H','T6_1_FA_H','T6_1_BS_H','T6_1_CM_H',

                # #Table 3: Permanent private households by type of occupancy                     
                # 'T6_3_RPLH','T6_3_RLAH','T6_3_RVCHBH','T6_3_OFRH',

                # #Table 10: Permanent private households by number of renewables                    
                # 'T6_10_RE',

                # #Table 4: Population aged 15 years and over by sex and highest level of education completed        
                # 'T10_4_TVT','T10_4_ACCAT','T10_4_HCT','T10_4_ODNDT','T10_4_HDPQT',
                # 'T10_4_PDT','T10_4_DT',

                # #Table 2: Persons in private households by socio-economic group of reference person
                # 'T9_2_HA','T9_2_HB','T9_2_HC','T9_2_HD','T9_2_HE','T9_2_HF',
                # 'T9_2_HG','T9_2_HH','T9_2_HI','T9_2_HJ','T9_2_HZ',

                # #Table 1: Population aged 5 years and over by means of travel to work, school or college
                # 'T11_1_ACT','T11_1_PUT','T11_1_CDT',

                # #Table 1: Number of households with cars
                # 'T15_1_NC','T15_1_1C','T15_1_2C+'#
                ]]

# Dependent variable (target)
y = dfCensus['Total BEVs']



# Create and fit the regression model
model = LinearRegression()
model.fit(X, y)

# Output model details
print(f"Intercept: {model.intercept_}")
print(f"Coefficients: {model.coef_}")
print(f"Feature names: {X.columns.tolist()}")

print('Done')

