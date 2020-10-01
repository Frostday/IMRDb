from django.shortcuts import render
from .models import Movie
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from rest_framework import viewsets
from rest_framework import mixins
import pickle
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



# Create your views here.
def homepage(request):
    movies_list = Movie.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(movies_list, 48)
    # query = request.GET.get("q")
    # if query:
    #     movies = movies.filter(
    #         Q(name__icontains=query)
    #     ).distinct()
    try:
        movies = paginator.page(page)
    except PageNotAnInteger:
        movies = paginator.page(1)
    except EmptyPage:
        movies = paginator.page(paginator.num_pages)

    return render(request, 'mainpage/index.html', {'movies': movies})


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
        self.fc1 = nn.Linear(nb_movies, 20)
        self.fc2 = nn.Linear(20, 8)
        self.fc3 = nn.Linear(8, 20)
        self.fc4 = nn.Linear(20, nb_movies)
        self.activation = nn.Tanh()
    def forward(self, x):
        x = self.activation(self.fc1(x))
        x = self.activation(self.fc2(x))
        x = self.activation(self.fc3(x))
        x = self.fc4(x)
        return x


def predict():
    dataset = pd.read_csv(os.path.dirname(os.path.realpath(__file__)) + "/ratings.csv")
    movies = pd.read_csv(os.path.dirname(os.path.realpath(__file__)) + "/filtered_movies.csv")

    pivot_table = dataset.pivot_table(index = ["userId"], columns = ["movieId"], values = "rating", fill_value=0)
    table = pivot_table.to_numpy()

    data = pd.merge(dataset, movies)
    data = data.drop(["timestamp", "movieId"], axis=1)

    sel_movies = data[data["userId"]==2]
    input = table[50]  # for user 2
    print(input)
    print(len(input))
    cols = pivot_table.columns

    arr = np.array(dataset, dtype='int')
    nb_users = int(max(arr[:, 0]))
    nb_movies = len(dataset.movieId.unique())

    model = SAE(nb_movies)
    print(os.path.dirname(os.path.realpath(__file__)) + "/sae_200.pt")
    model.load_state_dict(torch.load(os.path.dirname(os.path.realpath(__file__)) + "/sae_200.pt", map_location=torch.device('cpu')))

    input = torch.FloatTensor(input)
    output = model(input)
    output = output.detach().numpy()
    output[input != 0] = 0  # make output for movies rated 0
    print(output)
    print(len(output))
    l = []
    for i in range(10):
        j = np.argmax(output)
        output[j] = 0
        l.append(j)
    # indices

    ids = []
    for i in l:
        ids.append(cols[i])
    # movie ids

    names = []
    for i in ids:
        value = movies.loc[movies.movieId == i].index
        value = movies.iat[value[0], 2]
        names.append(value)
    print(names)


