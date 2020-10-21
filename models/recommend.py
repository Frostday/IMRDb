import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.nn.parallel
import torch.optim as optim
import torch.utils.data
from torch.autograd import Variable

dataset = pd.read_csv("../data/ratings.csv")
arr = np.array(dataset, dtype='int')

nb_users = int(max(arr[:, 0]))
nb_movies = len(dataset.movieId.unique())
print(nb_movies, nb_users)


class SAE(nn.Module):

    def __init__(self, ):
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


model = SAE()
model.load_state_dict(torch.load('new_sae_200.pt'))

pivot_table = dataset.pivot_table(index=["userId"], columns=[
                                  "movieId"], values="rating", fill_value=0)
table = pivot_table.to_numpy()
inp = table[1]
# (user 2)

for i, _ in enumerate(inp):
    inp[i] = 0
inp[0] = 5
inp[5] = 5
print(inp)
inp = torch.FloatTensor(inp)
output = model(inp)
output = output.detach().numpy()
output[inp != 0] = -1  # make output for movies rated -1
print(output)
# print(len(output))

# indices
l = []
for i in range(50):
    j = np.argmax(output)
    output[j] = 0
    l.append(j)
# print(l)

# movie ids
cols = pivot_table.columns

ids = []
for i in l:
    ids.append(cols[i])
# print(ids)

movies = pd.read_csv("../data/filtered_movies.csv")

names = []
for i in ids:
    value = movies.loc[movies.movieId == i].index
    value = movies.iat[value[0], 2]
    names.append(value)
print(names)
