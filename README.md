# IMRDb

Internet Movie Recommender Database made using HTML, CSS and Django. An autoencoder was used for making the actual recommendation. It was trained on the ml-25m dataset and Pytorch framework was used for making the neural network.

# Creators
 
- Dhruv Garg(Frostday)
- Sanchit Jain(sanchjain)

# Setting up and running the project

1. Fork the repo and clone it.

2. Go in the repo and setup virtualenvironment using ```python -m virtualenv venv```

3. Then activate the environment using:
- ```source venv/Scripts/activate``` on Windows
- ```source venv/bin/activate``` on MacOS/Linux

4. Move into the /imrdb directory using ```cd imrdb/```

5. Install all requirements using ```pip install -r requirements.txt```

6. After the above setup, run ```python manage.py makemigrations``` and ```python manage.py migrate```

7. Start the backend server using ```python manage.py runserver```

Default port: 8000

Open http://localhost:8000 to view it in the browser.
