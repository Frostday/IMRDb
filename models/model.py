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

pivot_table = dataset.pivot_table(index = ["userId"], columns = ["movieId"], values = "rating", fill_value=0)
data = pivot_table.to_numpy()
data = torch.FloatTensor(data)

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


sae = SAE()
criterion = nn.MSELoss()
optimizer = optim.RMSprop(sae.parameters(), lr=0.01, weight_decay=0.5)

if torch.cuda.is_available():
    device = torch.device("cuda:0")
    print("running on the gpu")
else:
    device = torch.device("cpu")
    print("running on the cpu")

sae.to(device)

nb_epoch = 200
for epoch in range(1, nb_epoch + 1):
    train_loss = 0
    s = 0.
    for user_id in range(nb_users):
        input = Variable(data[user_id]).unsqueeze(0).to(device)
        target = input.clone()
        if torch.sum(target.data > 0) > 0:
            output = sae(input)
            target.require_grad = False
            target = target.to(device)
            output[target == 0] = 0
            loss = criterion(output, target)
            mean_corrector = nb_movies / float(torch.sum(target.data > 0) + 1e-10)
            loss.backward()
            train_loss += np.sqrt(loss.data.cpu() * mean_corrector)
            s += 1
            optimizer.step()
    print('epoch: ' + str(epoch) + '  loss: ' + str(train_loss / s))

torch.save(sae.state_dict(), 'new_sae_200.pt')