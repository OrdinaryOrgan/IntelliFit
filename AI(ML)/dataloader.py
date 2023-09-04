import numpy as np
import pandas as pd

MAXHEIGHT = 220

class fitnessman:

    def __init__(self, name, height):
        self.name = name
        self.height = height

    def load_data(self, path):
        path = path + self.name + '.csv'
        data = pd.read_csv(path)
        for i in range(1, 43):
            data[data.columns[i]] = data[data.columns[i]] * (self.height/MAXHEIGHT)
        return data

def data_loader(path, fitnessman_list, fitnessman_height):
    for i in range(len(fitnessman_list)):
        person = fitnessman(fitnessman_list[i], fitnessman_height[i])
        if i == 0:
            data = person.load_data(path)
        else:
            data = pd.concat([data, person.load_data(path)], axis=0)
    data = np.array(data)
    x = data[..., 1:43]
    y = data[..., 43].astype("int")
    return x, y