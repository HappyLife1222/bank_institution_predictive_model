# -*- coding: utf-8 -*-
"""Data.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16zAVgZormt7RFGic6NsSIyGrRbHs-jM1
"""

from sklearn.model_selection import train_test_split

def data_loader(data):
  X=data.drop(['y'],axis=1)
  y=data['y']

  return X,y