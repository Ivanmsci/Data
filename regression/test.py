import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

df_name = input("cual es el nombre de la base de datos" )
df = pd.read_csv(df_name)
X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values

print(X)