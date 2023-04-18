import numpy as np
import pandas as pd

# Transformación de los datasets
def transformation(df, word, platform):
    df['show_id']= word + df['show_id'] #Addtion of the extra word
    df['rating'].fillna('G', inplace= True) #replace NaN with "G"
    df['date_added']= pd.to_datetime(df['date_added']) #Type change of "date_added" column from Object to DateTime
    df= df.applymap(lambda s: s.lower() if type(s)== str else s) #Lower case all the Dataframe elements
    df[['duration_int', 'duration_type']]= df['duration'].str.split(' ', expand= True) #Split of "duration" columns into "duration_int" and "duration_type"
    df.insert(loc= df.columns.get_loc('duration') + 1, column='duration_int',value=df.pop('duration_int')) #Relocation of "duration_int" column
    df.insert(loc= df.columns.get_loc('duration') + 2, column='duration_type',value=df.pop('duration_type')) #Relocation of "duration_type" column
    df['duration_type']=df['duration_type'].str.replace('seasons','season') #Standarize "seasons" and "season" into "season"
    df= df.drop(columns=['duration']) #Drop of duration column
    df['platform']= platform #Column added to filter
    return df

#Importo los Datasets

amazon_df = pd.read_csv('amazon_prime_titles.csv')
disney_plus_df = pd.read_csv('disney_plus_titles.csv')
hulu_df = pd.read_csv('hulu_titles.csv')
netflix_df = pd.read_csv('netflix_titles.csv')

#Aplico las transformaciones a los datasets
df_amazon= transformation(amazon_df,'a','amazon')
df_disney= transformation(disney_plus_df,'d','disney')
df_hulu= transformation(hulu_df,'h','hulu')
df_netflix= transformation(netflix_df,'n','netflix')

#Unifico todas las platformas de los datasets en uno único
df_platform= pd.concat([df_amazon,df_disney,df_hulu,df_netflix], axis=0)