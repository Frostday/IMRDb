from django.shortcuts import render
from .models import Movie
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
import pickle
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from star_ratings.models import UserRating
from django.http import HttpResponse



# Create your views here.
def homepage(request):
    movies_list = Movie.objects.all()
    page = request.GET.get('page', 1)
    query = request.GET.get("q")
    if query:
        movies_list = movies_list.filter(
            Q(name__icontains=query)
        ).distinct()

    paginator = Paginator(movies_list, 48)
    try:
        movies = paginator.page(page)
    except PageNotAnInteger:
        movies = paginator.page(1)
    except EmptyPage:
        movies = paginator.page(paginator.num_pages)

    if request.method == "POST":
        ids = predict()
        l = []
        for id in ids:
            l.append(Movie.objects.get(movie_id=id))
        return render(request, 'mainpage/results.html', {'results': l})
    else:
        return render(request, 'mainpage/index.html', {'movies': movies})

def ratedpage(request):
    user_ratings = UserRating.objects.all()
    d = {}
    for index in user_ratings:
        movie = Movie.objects.get(id=index.rating.object_id)
        d[movie.name] = index.score
    print(d)
    return render(request, 'mainpage/rated.html', {'dict': d})


import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.nn.parallel
import torch.optim as optim
import torch.utils.data
from torch.autograd import Variable
import os


class SAE(nn.Module):
    def __init__(self, nb_movies):
        super(SAE, self).__init__()
        self.fc1 = nn.Linear(nb_movies, 500)
        self.fc2 = nn.Linear(500, 20)
        self.fc3 = nn.Linear(20, 8)
        self.fc4 = nn.Linear(8, 20)
        self.fc5 = nn.Linear(20, 500)
        self.fc6 = nn.Linear(500, nb_movies)
        self.activation = nn.Tanh()

    def forward(self, x):
        x = self.activation(self.fc1(x))
        x = self.activation(self.fc2(x))
        x = self.activation(self.fc3(x))
        x = self.activation(self.fc4(x))
        x = self.activation(self.fc5(x))
        x = self.fc6(x)
        return x



def predict():
    print("called")

    user_ratings = UserRating.objects.all()
    dataset = pd.read_csv(os.path.dirname(os.path.realpath(__file__)) + "/ratings.csv")
    movies = pd.read_csv(os.path.dirname(os.path.realpath(__file__)) + "/filtered_movies.csv")

    pivot_table = dataset.pivot_table(index = ["userId"], columns = ["movieId"], values = "rating", fill_value=0)
    table = pivot_table.to_numpy()
    cols = pivot_table.columns
    print(user_ratings)

    d = {}
    for index in user_ratings:
        movie = Movie.objects.get(id=index.rating.object_id)
        d[movie.movie_id] = index.score
    # d = {
    #     1: 5,
    #     2: 5,
    # }

    print(d)
    arr = np.zeros((9724), dtype=np.float32)
    print(arr)
    for i,value in enumerate(cols):
        if value in d.keys():
            print(d[value])
            arr[i] = d[value]
    
    a = np.array(dataset, dtype='int')
    nb_users = int(max(a[:, 0]))
    nb_movies = len(dataset.movieId.unique())

    model = SAE(nb_movies)
    print(os.path.dirname(os.path.realpath(__file__)) + "/new_sae_200.pt")
    model.load_state_dict(torch.load(os.path.dirname(os.path.realpath(__file__)) + "/new_sae_200.pt", map_location=torch.device('cpu')))

    arr = torch.FloatTensor(arr)
    print(arr)
    output = model(arr)
    output = output.detach().numpy()
    print(output)
    print(len(output))

    output[arr!=0] = -1
    # print(arr)
    # print(output)
    l = []
    for i in range(50):
        j = np.argmax(output)
        output[j] = -1
        l.append(j)
    # indices

    ids = []
    for i in l:
        ids.append(cols[i])
    # movie ids
    print(ids)

    names = []
    for i in ids:
        value = movies.loc[movies.movieId == i].index
        value = movies.iat[value[0], 2]
        names.append(value)
    print(names)

    return ids


