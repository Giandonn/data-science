import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_name = "/content/sample_data/california_housing_test.csv"
df = pd.read_csv(file_name)
print(f"Colunas: {df.shape[0]}, Linhas: {df.shape[1]}\n")

print(f"Quantidade de valores nulos: {df.isnull().sum().sum()}\n")

print(f"Média: {df.mean()}\n")

print(f"Mediana: {df.median()}\n")

print(f"Mínimo: {df.min()}\n")

print(f"Máximo: {df.max()}\n")