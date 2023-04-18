# Proyecto-Individual-1
Hey there! Welcome to my first individual project! It took me some time, but they say the third try is the one you make it :) On this excercise I have adopted the role of a MLOps Engineer.

# Context
The objective given by the client was for us to process the datasets provided and develop a recommendation system.

Original platform datasets and rating datasets are saved in a drive on this <a href="https://drive.google.com/drive/folders/1oPQRbG3WkTkk8uIAiQF7f6PKOc1CPRxI?usp=share_link" rel="nofollow">link</a>

# Data treatment:
[ETL_main.py](https://github.com/josefinaloyola/Proyecto-Individual-1/blob/main/ETL_main.py)

etl(support).ipynb

In order to better structure the information in the data, we proceeded to:
For files of each platform (found in the 'datasets' folder): Amazon, Disney, Hulu, and Netflix.

* A new id field was generated: Each new id is composed of the first letter of the platform name, followed by the show_id already present in the datasets (example for Amazon titles = as123).

* Null values in the 'rating' field were replaced with the string “G” ('general for all audiences').

* The format of the 'date_added' column was changed to YYYY-mm-dd.

* All fields were converted to lowercase, no exceptions.

* "Duration" field was divided into two: duration_int and duration_type. The first field is an int and the second is a string indicating the duration unit of measurement: min (minutes) or season (seasons), which were all changed to singular form in order to facilitate search.

* The "Duration" original field was eliminated

For rating files (from 1 to 8):

* A new column was added to indicate which platform each ID in the 'movieId' column belongs to.

* The 8 datasets were concatenated into a single one, the columns of esto y esto were eliminated since they didn't add any value. 

* An average score per movie was calculated, since there were multiple scores for the same movies. In this way we obtained the general score for the movie and we reduced the size of the dataset so it could be exported with a smaller size so that it could later be uploaded to GitHub 

* after being loaded, since, due to the size of the datasets, it was not possible to deploy on Render.

The concatenated csv has been saved in a drive as scores_data.csv -- agregar link

# API Development:
main.py -- agregar link

With the transformed datasets, they were made available to the client through an API built with FastAPI library, featuring various queries for the user:

* Movie (not TV Show, etc.) with the longest duration by year, platform, and duration type. Function name: get_max_duration(year, platform, duration_type). Returns the name of the movie

* Number of movies (not TV Show, etc.) by platform, with a score higher than XX in a given year. Function name: get_score_count(platform, scored, year). Returns an 'int', with the total number of movies that meet the requested criteria.

* Number of movies (not TV Show, etc.) by platform. Function name: get_count_platform(platform). Returns an int, with the total number of movies for that platform. The platforms are named: Amazon, Netflix, Hulu, and Disney.

* Actor who appears most frequently by platform and year. Function name: get_actor(platform, year). Returns the name of the actor who appears most frequently according to the given platform and year.

* Number of content/products (everything available for streaming, series, movies, etc) according to the given audience rating (for which audience the content was classified). Function name: get_contents(rating). It returns the total number of contents with that audience rating.

* The number of contents/products (all available streaming content) released by country and year. Function name: prod_per_country(content_type, country, year). It returns the number of the specified content type (movie, TV Show) per country and year in a dictionary with the variables 'country' (country name), 'year' (year), 'movie' (number of movies).

# Deployment:
The deployment was carried out through Render at the following link, with the project name: PI-MLOpsEngineer. -- hacer render y link

# Exploratory Data Analysis:
eda_mainfile.ipynb -- link

To obtain a first global overview of the datasets' structure, functions such as .shape, .dtype, .describe, .info, and .head were used. In order to observe a little more in detail, a box plot diagram was graphed, where several outliers were found in the "duration_int" column. Finally, to complement this analysis, the ProfileReport tool from pandas_profiling library was used, where it was possible to observe that there are no duplicate values. The platform "Hulu" contains the most null values, some columns such as "cast" do not contain any values. Additionally, it was observed that the movie with the lowest score was "filth" with a score of 0.5.

# Recommendation system:

I didn't know how to do this part of the project so I left the function blank. It just retunrs some excellent movies as recommendation which will be loved by any audience.


# Video explanation:
link -- hacer video y poner link
