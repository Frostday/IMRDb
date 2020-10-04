import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.nn.parallel
import torch.optim as optim
import torch.utils.data
from torch.autograd import Variable
import os

dataset = pd.read_csv("mainpage/ratings.csv")

pivot_table = dataset.pivot_table(index = ["userId"], columns = ["movieId"], values = "rating", fill_value=0)
table = pivot_table.to_numpy()

inp = table[50]  # for user 2
# print(inp)
# print(len(inp))
cols = pivot_table.columns
# print(pivot_table)
# print(cols)
# print(len(cols))

d = {
    #id : rating(float)
    1: 4.0,
    6: 3.0
}

arr = np.zeros((9724), dtype=np.float32)

for i,value in enumerate(cols):
    if value in d.keys():
        print(d[value])
        arr[i] = d[value]

print(arr)
    