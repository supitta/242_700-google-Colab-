# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1fQQCSYFPUkjRVkzseo9jX2asTblhOdJn
"""

import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('insurance (2).csv')
df.head()

df.columns

df.dropna(inplace = True)

index (['age','sex','bmi','children','smoker','region','charges'], dtype='object')

input_columns = ['age','bmi','children']
output_columns = ['charges']

from sklearn.model_selection import train_test_split
X_train,X_test, y_train = train_test_split(X,y,test_size=.20, random_state=1,)

print(model1.intercept_)
print(madel.coef_)





X_quiz = [[30,35,1],[19,25,0],[41,23,2]]
y_quiz = model1.predict(X_quiz)
print(y_quiz)