# IMRDb
Internet Movie Recommender Database made using HTML, CSS and Django. An autoencoder was used for making the actual recommendation. It was trained on the ml-25m dataset and Pytorch framework was used for making the neural network..

# Creators 
Dhruv Garg(Frostday)
Sanchit Jain(sanchjain)

# Setting up the server

1. Go in the repo and setup virtual environment using <br>
```python -m virtualenv venv``` 

2. Then activate the environment using <br>
    On Windows: <br>
```source venv/Scripts/activate``` <br>
    On MacOS/Linux: <br>
```source venv/bin/actiavte```

3. Go into the imrdb/ directory and install all requirements using <br>
```pip install -r requirements.txt```

4. After the above setup, run \
```python manage.py makemigrations```\
```python manage.py migrate```

5. Start the backend server\
    ```python manage.py runserver```\
    Runs the backend server at default port ```8000```.\
    Open [http://localhost:8000](http://localhost:8000) to view it in the browser.

The page will reload if you make edits.<br />


If you want to access the admin panel, create a user using: <br>
```python manage.py createsuperuser```

Create a user, and login with the created user at [http://localhost:8000/admin](http://localhost:8000/admin).