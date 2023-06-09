# Proyecto-Individual-1
Hey there! Welcome to my first individual project! It took me some time, but they say the third try is the one you make it :) On this excercise I have adopted the role of a MLOps Engineer.

# Context
The objective given by the client was for us to process the datasets provided and develop a recommendation system.

Original platform datasets and rating datasets are saved in a drive on this <a href="https://drive.google.com/drive/folders/1oPQRbG3WkTkk8uIAiQF7f6PKOc1CPRxI?usp=share_link" rel="nofollow">link</a>

# Data treatment:
[ETL_soporte.ipynb](https://github.com/josefinaloyola/Proyecto-Individual-1/blob/main/ETL_soporte.ipynb)

In order to better structure the information in the data, we proceeded to:

For files of each platform: Amazon, Disney, Hulu, and Netflix.

* A new id field was generated: Each new id is composed of the first letter of the platform name, followed by the show_id already present in the datasets (example for Amazon titles = as123).

* Null values in the 'rating' field were replaced with the string “G” ('general for all audiences').

* The format of the 'date_added' column was changed to YYYY-mm-dd.

* All fields were converted to lowercase, no exceptions.

* "Duration" field was divided into two: duration_int and duration_type. The first field is an int and the second is a string indicating the duration unit of measurement: min (minutes) or season (seasons), which were all changed to singular form in order to facilitate search.

* The "Duration" original field was eliminated

For rating files (from 1 to 8) in this link [ETL_ratings.ipynb](https://github.com/josefinaloyola/Proyecto-Individual-1/blob/main/ETL_ratings.ipynb)

* The 8 datasets were concatenated into a single one, the columns of userId and timestamp were eliminated since they didn't add any value. 

* An average score per movie was calculated, since there were multiple scores for the same movies. In this way we obtained the general score for the movie and we reduced the size of the dataset so it could be exported with a smaller size so that it could later be uploaded to GitHub 

The ratings csv has been saved in my git repository [scores_data.csv](https://github.com/josefinaloyola/Proyecto-Individual-1/blob/main/scores_data.csv)

The multiplatform csv has been saved in my git repository [multiplataforma.csv](https://github.com/josefinaloyola/Proyecto-Individual-1/blob/main/multiplataforma.csv)

The scores + platforms csv has been saved in my git repository [plataformas_scores.csv](https://raw.githubusercontent.com/josefinaloyola/Proyecto-Individual-1/main/plataformas_scores.csv)

# API Development:
[main.py](https://github.com/josefinaloyola/Proyecto-Individual-1/blob/main/main.py)

With the transformed datasets, that were made available to the client through an API built with FastAPI library, featuring various queries for the user:

* Movie (not TV Show, etc.) with the longest duration by year, platform, and duration type. Function name: get_max_duration(year, platform, duration_type). Returns the name of the movie

* Number of movies (not TV Show, etc.) by platform, with a score higher than XX in a given year. Function name: get_score_count(platform, scored, year). Returns an 'int', with the total number of movies that meet the requested criteria.

* Number of movies (not TV Show, etc.) by platform. Function name: get_count_platform(platform). Returns an int, with the total number of movies for that platform. The platforms are named: Amazon, Netflix, Hulu, and Disney.

* Actor who appears most frequently by platform and year. Function name: get_actor(platform, year). Returns the name of the actor who appears most frequently according to the given platform and year.

* Number of content/products (everything available for streaming, series, movies, etc) according to the given audience rating (for which audience the content was classified). Function name: get_contents(rating). It returns the total number of contents with that audience rating.

* The number of contents/products (all available streaming content) released by country and year. Function name: prod_per_country(content_type, country, year). It returns the number of the specified content type (movie, TV Show) per country and year in a dictionary with the variables 'country' (country name), 'year' (year), 'movie' (number of movies).

# Deployment:
The deployment was carried out through Render at the following link, with the project name:[Proyecto Individual I](https://proyecto-individual-1-7eio.onrender.com)

# Recommendation system:

I didn't know how to do this part of the project so I left the function blank. It just retunrs some excellent movies as recommendation which will be loved by any audience.


# Video explanation:
[link video](https://youtu.be/PllOOqe4FnY)
