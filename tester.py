import pickle
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

import pandas as pd
import os

def brain(inin):
    AVGs = []
    model = pickle.load(open("brain.pkl", 'rb'))
    vect = pickle.load(open("vectorizer.pkl", 'rb'))

    length = len(inin) # Number of remedies entered
    temp = []

    for i in range(length):
        length_articles = len(inin[i])

        temp_avg = []
        for j in range(length_articles):
            arr = inin[i][j]

            t_matrix = vect.transform(arr)
            predictions = model.predict(t_matrix)

            for item in predictions:
                if item == 'pos':
                    temp.append(1)
                else:
                    temp.append(0)

            sum = 0

            for item in temp:
                sum += item

            avg = sum / len(temp)
            temp_avg.append(avg)

        SUM = 0
        for item in temp_avg:
            SUM += item

        AVGs.append(SUM / len(temp_avg))
    return AVGs

