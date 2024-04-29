#instalar pip si esta mal
# ejecutar cmd modo admin: py -m ensurepip --upgrade
#para instalar pandasejecutar
#py -m pip install pandas
#py -m pip install sklearn

import pandas as pd
import numpy as np
#ip install -U scikit-learn

from sklearn.impute import SimpleImputer
# from sklearn.preprocessing import Imputer
from sklearn.preprocessing import OneHotEncoder,LabelEncoder
# from sklearn.compose import ColumnTransformer
# from sklearn.compose import ColumnTransformer, make_column_transformer

df = pd.read_csv('datos\\data.csv')
print (df)

# Reemplazar cada valor faltante por las siguientes posibilidades:
# mean, median, mode. Axis = 0 es rows, 1 es column

# imputer = Imputer(missing_values='NaN', strategy='mean', axis = 0)
imputer = SimpleImputer(missing_values=np.nan, strategy='median')
df.iloc[:, 1:3] = imputer.fit_transform(df.iloc[:, 1:3])
df


# Label Encoder reemplazará cada variable categórica con un número. Útil para reemplazar si por 1, no por 0.
# One Hot Encoder creará una columna separada para cada variable y dará un valor de 1 en caso que variable está presente
enc = LabelEncoder()
temp = df.copy()
temp.iloc[:, 0]=enc.fit_transform(df.iloc[:, 0])
# temp.iloc[:, 3]=enc.fit_transform(df.iloc[:, 3])
temp.head()


# puedes pasar una serie de índices de características categóricas a one-hot
one_hot_encoder = OneHotEncoder()
b=np.expand_dims(temp.iloc [:, 0].values, axis=1)
temp1=pd.DataFrame(data=one_hot_encoder.fit_transform(b).toarray())
temp1 = pd.concat([temp1, temp.drop(['Pais'], axis=1)], axis=1)
# temp1 = pd.concat([temp1, temp], axis=1)
print(temp1)


# puedes lograr lo mismo usando get_dummies
# print(df.head())
# print(df.iloc[:, :-1])
# pd.get_dummies(df.iloc[:, :-1])
pd.get_dummies(df.iloc[:, :])


from sklearn.datasets import load_iris

iris_dataset = load_iris()
X = iris_dataset.data
y = iris_dataset.target
feature_names = iris_dataset.feature_names

X[:, 1]

from sklearn.preprocessing import Binarizer
X[:, 1:2] = Binarizer(threshold=X[:, 1].mean()).fit_transform(X[:, 1].reshape(-1, 1))


print('Terminamos')
