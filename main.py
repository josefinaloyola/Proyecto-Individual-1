import pandas as pd
from fastapi import FastAPI

app = FastAPI(title= 'Peliculas y series',
              description= 'Con esta API puedes encontrar las series y películas de las siguientes plataformas: Amazon, Disney Plus, Hulu and Netflix')

# http://127.0.0.1:8000

# Welcome
@app.get('/')
async def index():
    return {"Welcome!!!"}

@app.get('/about')
async def about():
    return 'Soy Henry primer proyecto individual, tercer intento'

#Datasets load
df_plataformas = pd.read_csv('multiplataforma.csv')
df_scores = pd.read_csv('scores_data.csv')
df_final = pd.read_csv('plataformas_scores.csv')

@app.get('/get_max_duration/{anio}/{plataforma}/{dtype}')
def get_max_duration(anio: int, plataforma: str, dtype: str):
     
    dicc = {"netflix":"n","amazon":"a","hulu":"h","disney":"d"}
        
    df_temp = df_final[(df_final['id'].str[0] == dicc[plataforma])&(df_final['type'] == 'movie')&(df_final['release_year'] == anio)].sort_values(["duration_int"],ascending=[False]).reset_index(drop=True)
    
    titulo = df_temp.iloc[0,2]
    duracion = df_temp.iloc[0,9]

    return {'pelicula': titulo}

@app.get('/get_score_count/{plataforma}/{scored}/{anio}')
def get_score_count(plataforma: str, scored: float, anio: int):
   
    dicc = {"netflix":"n","amazon":"a","hulu":"h","disney":"d"}
    df_temp = df_final[(df_final["score"]>scored) & (df_final["release_year"]==anio) & (df_final.id.str[0] == dicc[plataforma]) & (df_final["type"] == "movie")]
    
    cantidad = len(df_temp.index) 

    return {'plataforma': plataforma,
            'cantidad': cantidad,
            'anio': anio,
            'score': scored}

@app.get('/get_count_platform/{plataforma}')
def get_count_platform(plataforma: str):
    dicc = {"netflix":"n","amazon":"a","hulu":"h","disney":"d"}
    df_temp = df_final[(df_final.id.str[0] == dicc[plataforma]) & (df_final["type"] == "movie")]
    
    cantidad = len(df_temp.index)
    
    return {'plataforma': plataforma, 'peliculas': cantidad}

@app.get('/get_actor/{plataforma}/{anio}')
def get_actor(plataforma: str, anio: int):
    dicc = {"netflix":"n","amazon":"a","hulu":"h","disney":"d"}
    
    by_actor = df_final.loc[(df_final.id.str[0] == dicc[plataforma]) & (df_final['release_year'] == anio), 'cast']
    all_actors = [actor.strip() for cast_list in by_actor.str.split(',') if isinstance(cast_list, list) for actor in cast_list]
    if not all_actors: #If the column is empty
        return {'platform':plataforma, "year":anio,'actor':'no information','times':0}
    else:
        #Most common actor and frequence
        most_common_actor = max(set(all_actors), key = all_actors.count)
        cantidad = all_actors.count(most_common_actor)
        return {'plataform':plataforma, "anio":anio,'actor':most_common_actor,'apariciones':cantidad}
    

@app.get('/get_contents/{rating}')
def get_contents(rating: str):
    df_temp = df_final[(df_final["rating"]== rating)]
    
    cantidad = len(df_temp.index) 

    return {'rating': rating, 'contenido': cantidad}


@app.get('/prod_per_county/{tipo}/{pais}/{anio}')
def prod_per_county(tipo: str, pais: str, anio: int):
    
        if(tipo == "pelicula"):
                df_temp = df_final[(df_final["release_year"]==anio) & 
                                   (df_final["type"] == "movie")&
                                   (df_final["country"]==pais)]
    
                cantidad = len(df_temp.index) 
                diccionario = {"pais": pais,
                               "anio": anio,
                               "peliculas":cantidad}

                return {'pais': pais, 'anio': anio, 'peliculas': cantidad}

        elif(tipo == "serie"):
                df_temp = df_final[(df_final["release_year"]==anio) & 
                                   (df_final["type"] == "tv show")&
                                   (df_final["country"]==pais)]
    
                cantidad = len(df_temp.index) 
                diccionario = {"pais": pais,
                               "anio": anio,
                               "series":cantidad}

                return {'pais': pais, 'anio': anio, 'peliculas': cantidad}


@app.get('/get_recomendation/{title}')
def get_recomendation(title: str):

    
    return {'recomendacion':"TITANIC, AVATAR Y GLADIADOR: nunca fallan, todas peliculas excelentes"}