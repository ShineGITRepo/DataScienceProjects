# To Perform exploratory data analysis on the netflix_data.csv data
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("/workspaces/DataScienceProjects/Netflix_Movies/netflix_data.csv")

# To find the most frequent movie duration in the 1990s
nineties_movies = netflix_df[np.logical_and(np.logical_and(netflix_df["release_year"] >= 1990 , netflix_df["release_year"] < 2000) , netflix_df["type"] == "Movie")]
duration = int(nineties_movies["duration"].mode()[0])
print("the most frequent movie duration in the 1990s? " + str(duration))

# To find the number of short action movies released in the 1990s which is less than 90 minutes
short_movies = nineties_movies[np.logical_and(nineties_movies["duration"] < 90, nineties_movies["genre"] == "Action")]
print("The number of short action movies released in the 1990s : " + str(short_movies.shape[0]))

#Plot a histogram of the duration of movies with 50 as bins
plt.hist(np.array(nineties_movies["duration"]),bins = 50)
plt.show()