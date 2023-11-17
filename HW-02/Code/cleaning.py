#https://pdas.samhsa.gov/saes/substate#

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import glob
from sklearn.feature_extraction.text import CountVectorizer


#cd HW-02
#load data from csv file
all_data_frames=glob.glob("./Part2/Data/*.csv")+glob.glob("./Part2/Data/*.xlsx")
for fname_index, fname in enumerate(all_data_frames):
    print(fname_index, fname)
df_GDP = pd.read_csv("./Part2/Data/GDP.csv") 


df_income_group = pd.read_excel("./Part2/Data/Income_group.xlsx")
df_Countries_Continents = pd.read_csv("./Part2/Data/Countries_Continents.csv")
df_education = pd.read_csv("./Part2/Data/education.csv")
df_discomfort_speaking_anxiety_depression_2020 = pd.read_csv("./Part2/Data/discomfort_speaking_anxiety_depression_2020.csv")
df_eating_disorder = pd.read_csv("./Part2/Data/eating_disorders_prevalence_males_vs_females.csv")
df_first_anxiety_or_depression = pd.read_csv("./Part2/Data/age_when_first_had_anxiety_depression.csv")

#A.clean the data named eating_disorders
# show all the columns of the dataframe
print(df_eating_disorder.columns)
print(df_eating_disorder.head())
# drop the columns Continent and Population because they are meaningless to the analysis
df_eating_disorder = df_eating_disorder.drop(columns=['Continent','Population'])
print(df_eating_disorder.shape)
# only keep the rows of the dataframe when the column 'Year' is between 1990-2021
# eating_disorder_df = eating_disorder_df.loc[eating_disorder_df['Year'] == range(1990,2022)]
df_eating_disorder = df_eating_disorder[df_eating_disorder['Year'].isin(range(1990,2022))]
print(df_eating_disorder.shape)
rename_map={
    'Entity':'Economy',
    'Year':'Year',
}
df_eating_disorder.rename(columns=rename_map, inplace=True)
print(df_eating_disorder.columns)
print(df_eating_disorder.head())

#drop the rows when the column named Eating_disorders_Male is null in the dataframe df_eating_disorder
df_eating_disorder= df_eating_disorder.dropna(subset=['Eating_disorders_Male'])

#caculate the mean of the column Male and Female of the dataframe and save it to a new column named All_gender
df_eating_disorder['All_gender'] = df_eating_disorder[['Eating_disorders_Male', 'Eating_disorders_Female']].mean(axis=1)
print(df_eating_disorder.head())
#save the dataframe to csv file
df_eating_disorder.to_csv("./Part2/Cleaned_Data/eating_disorder_male_female.csv", index=False)

#B.clean the data named discomfort_speaking_anxiety_depression_2020
df_discomfort_speaking_anxiety_depression_2020 = pd.read_csv("./Part2/Data/discomfort_speaking_anxiety_depression_2020.csv")
#rename the column 'Entity' to 'Country' and 'Share - Question: mh5 - Someone local comfortable speaking about anxiety/depression with someone they know - Answer: Not at all comfortable - Gender: all - Age_group: all' to 'Not_Comfortable'
df_discomfort_speaking_anxiety_depression_2020.rename(columns={'Entity':'Economy'}, inplace=True)
print(df_discomfort_speaking_anxiety_depression_2020.head())
df_discomfort_speaking_anxiety_depression_2020.to_csv("./Part2/Cleaned_Data/discomfort_speaking_anxiety_depression_2020.csv", index=False)

#C.clean the data named GDP
#add column names to the dataframe df_GDP
df_GDP.columns=['Code', 'Ranking','unnamed:2','Economy','GDP(2022)','unnamed:5']
df_GDP=df_GDP.drop(columns=['unnamed:2','unnamed:5'])
#check the data type of the column GDP
#convert the column GDP to numeric type
df_GDP['GDP(2022)']=df_GDP['GDP(2022)'].str.replace(',','')
#convert the column GDP from object type to numeric type
df_GDP['GDP(2022)']=pd.to_numeric(df_GDP['GDP(2022)'],errors='coerce')
# df_GDP['GDP']=pd.to_numeric(df_GDP['GDP'],errors='coerce')
print(df_Countries_Continents.head())
df_GDP.to_csv("./Part2/Cleaned_Data/GDP.csv", index=False)

#D.clean the data named Countries_Continents
#rename the column Country to Economy
df_Countries_Continents.rename(columns={'Country':'Economy'},inplace=True)
df_Countries_Continents.to_csv("./Part2/Cleaned_Data/Countries_Continents.csv", index=False)

#E.clean the data named education
#create a new column named 'average_learning_Adjusted_of_school' to calculate the average of the columns 'Average years of schooling' of each Entity
df_education['average_learning_Adjusted_of_school'] = df_education.groupby('Entity')['Learning-Adjusted Years of School'].transform('mean')
# This method keeps the first occurrence of each entity and drops the subsequent duplicates.
df_education = df_education.drop_duplicates(subset='Entity', keep='first')
# rename the column entity to Economy
df_education.rename(columns={'Entity':'Economy'},inplace=True)
df_education.to_csv("./Part2/Cleaned_Data/education.csv", index=False)

#F.clean the data named mental_health.xlsx and merge the dataframes

df_mental_health = pd.read_excel('./Part2/Data/mental_health.xlsx')
# show all the columns of the dataframe
# mental_health_df.columns
print(df_mental_health.head())
# # drop the columns of the dataframes that do not belong to mental health disorders
df_mental_health = df_mental_health.drop(columns=['Drug use disorders (%)', 'Alcohol use disorders (%)'])

#rename the column Entity to Economy
df_mental_health.rename(columns={'Entity':'Economy'},inplace=True)

#drop the code column when the column Code is null
df_mental_health=df_mental_health.dropna(subset=['Code'])

#merge the dataframe df_mental_health to df_income_group
df_mental_health_merge= df_mental_health.merge(df_income_group[['Code','Income group']], on='Code', how='left')

#merge the dataframe df_education to df_mental_health_merge
df_mental_health_merge=df_mental_health_merge.merge(df_education[['Code','average_learning_Adjusted_of_school']], on='Code', how='left')

# merge the two dataframes countries_continents and mental_health_merge
df_mental_health_merge=df_mental_health_merge.merge(df_Countries_Continents[['Economy','Continent']], on='Economy', how='left')
print(df_mental_health_merge.head())

#merge the dataframe df_GDP to df_mental_health_merge
df_mental_health_merge=df_mental_health_merge.merge(df_GDP[['Code','GDP(2022)']], on='Code', how='left')
print(df_discomfort_speaking_anxiety_depression_2020.head())

#merge the dataframe df_discomfort_speaking_anxiety_depression_2020 to df_mental_health_merge
df_mental_health_merge=df_mental_health_merge.merge(df_discomfort_speaking_anxiety_depression_2020[['Code','not_at_all_comfortable_speaking_anxiety_or_depression_percent']], on='Code', how='left')
print(df_mental_health_merge.head())

#save the dataframe to csv file
df_mental_health_merge.to_csv("./Part2/Cleaned_Data/mental_health.csv", index=False)

#G.clean the data named age_when_first_anxiety_depression.csv
df_first_anxiety_or_depression=df_first_anxiety_or_depression.drop(columns=['Code'])
print(df_first_anxiety_or_depression.head())
print(df_first_anxiety_or_depression.columns)
#melt the dataframe
df_first_anxiety_or_depression=pd.melt(df_first_anxiety_or_depression, id_vars=['Entity'], value_vars=['Ages <13','Ages_13_19','Ages_20_29','Ages_30_39','Ages ≥40','Dont_know/Refused'], var_name='Age', value_name='Percentage')
print(df_first_anxiety_or_depression.head())
df_first_anxiety_or_depression.to_csv("./Part2/Cleaned_Data/age_when_first_anxiety_or_depression.csv", index=False)

# # Sample dataframe
# df = pd.DataFrame({
#     'A': ['a1', 'a2', 'a3'],
#     'B': [1, 2, 3],
#     'C': [4, 5, 6],
#     'D': [7, 8, 9]
# })

# print("Original DataFrame:")
# print(df)

# # Use melt to transform the dataframe
# melted_df = pd.melt(df, id_vars=['A'], value_vars=['B', 'C', 'D'], var_name='Variable', value_name='Value')

# print("\nMelted DataFrame:")
# print(melted_df)

#H.cleaning GDP_per_capita.csv
df_mental_health=df_mental_health_merge
df_gdp_per_captita=pd.read_csv('./Part2/Data/GDP_per_captita.csv')
df_gdp_per_captita.head()  
df_gdp_per_captita.columns
#make a new dataframe with the column '2017'
df_gdp_per_captita_2017=df_gdp_per_captita[['GDP per capita, current prices(U.S. dollars per capita)','2017']]
df_gdp_per_captita_2017=df_gdp_per_captita_2017.rename(columns={'GDP per capita, current prices(U.S. dollars per capita)':'Economy'})
print(df_gdp_per_captita_2017.head())

#selet rows in df_mental_health when the column 'Year' is 2017
df_mental_health_2017=df_mental_health[df_mental_health['Year']==2017]

#select columns Economy,Schizophrenia (%),Bipolar disorder (%),in df_mental_health_2017,Eating disorders (%),Anxiety disorders (%) in 
#df_mental_health_2017
df_mental_health_2017=df_mental_health_2017[['Economy','Schizophrenia (%)','Bipolar disorder (%)','Eating disorders (%)','Anxiety disorders (%)','Depression (%)']]
print(df_mental_health_2017.head())

# #merge two dataframes
df_gdp_mental_health_2017=pd.merge(df_gdp_per_captita_2017,df_mental_health_2017,on='Economy',how='inner')

#merge df_gdp_mental_health_2017 with df_income_group
df_gdp_mental_health_2017=pd.merge(df_gdp_mental_health_2017,df_income_group,on='Economy',how='inner')
print(df_gdp_mental_health_2017.head())
df_gdp_mental_health_2017.to_csv('./Cleaned_Data/GDP_percaptita_mental_health_2017.csv',index=False)


