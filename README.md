# IMRDb
<center><img src="assets/logo.png" alt="logo"></center>
Internet Movie Recommender Database is a website made using HTML, CSS and Django which uses deep learning to recommend movies to users according to their preferences. An autoencoder was used for making the actual recommendation. It was trained on the ml-25m(small version) dataset.

## Creators
 
- Dhruv Garg(Frostday)
- Sanchit Jain(sanchjain)

## Setting up and running the project

1. Fork the repo and clone it.
```
git clone https://github.com/Frostday/IMRDb.git
```
2. Activate your virtual/conda environment and move into the imrdb folder.
```
cd imrdb
```
3. To download the required packages run the commands below 
```
pip install -r requirements.txt
```
4. After the above setup, run the following commands
```
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata movies
```
5. Start the backend server using 
```
python manage.py runserver
```
6. Open the url below to view it in the browser.
```
http://localhost:8000
```

## Dataset

We used MovieLens Latest Small Dataset(generated on September 26, 2018) available at this link - http://files.grouplens.org/datasets/movielens/ml-latest-small.zip for this project. The dataset contains 100,836 ratings and 3,683 tag applications applied to 9,742 movies by 610 users. More details regarding the dataset are available here - http://files.grouplens.org/datasets/movielens/ml-latest-small-README.html.

## Preview

![](assets/imrdb-final.gif)

Short Version:

![](assets/imrdb-short-final.gif)