import pandas as pd 
import numpy as np
from sklearn.linear_model import LinearRegression
import pickle
from formulas import valoracion_modelos
from sklearn.metrics import mean_absolute_error, mean_squared_error, mean_absolute_percentage_error, r2_score


#importamos csv test
df_test = pd.read_csv("./data/test.csv")

#separamos train-test

from sklearn.model_selection import train_test_split

x_test = df_test.drop(columns=["salario_eur"])
y_test = df_test["salario_eur"]

with open('./models/train_model.pkl', 'rb') as archivo_entrada:
    model_pretrained = pickle.load(archivo_entrada)

baseline_predictions = model_pretrained.predict(x_test)




valoracion_modelos("best_model", model_pretrained , x_test, y_test )