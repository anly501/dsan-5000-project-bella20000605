import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import glob
from sklearn.feature_extraction.text import CountVectorizer
#cd HW-02

#load data from csv file
all_data_frames=glob.glob("./Part2/Data/*.csv")+glob.glob("./Part2/Data/*.xlsx")
for fname_index, fname in enumerate(all_data_frames):
    print(fname_index, fname)

#A.clean the data named mental_health
mental_health = all_data_frames[9]
mental_health_df = pd.read_excel(mental_health)  # Use the 'mental_health' variable
# show all the columns of the dataframe
# mental_health_df.columns
print(mental_health_df.head())

vectorizer = CountVectorizer()
count=vectorizer.fit_transform(mental_health_df['Entity'].values.astype('U'))
print(count)
print('vocabulary list:',vectorizer.vocabulary_)
print('vocabulary size:',len(vectorizer.vocabulary_))

# # drop the columns of the dataframes that do not belong to mental health data
mental_health_df = mental_health_df.drop(columns=['Drug use disorders (%)', 'Alcohol use disorders (%)'])
print(mental_health_df.head())
# mental_health_df['Entity'] = pd.factorize(mental_health_df['Entity'])[0]
#save the dataframe to csv file
mental_health_df.to_csv("./Part2/Code/mental_health_Count.csv", index=False)

