import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_name = "/content/sample_data/california_housing_test.csv"
df = pd.read_csv(file_name)

# Definir faixas de valores para o gráfico de barras
bins = [0, 100000, 200000, 300000, 400000, 500000, np.inf]
labels = ['0-100k', '100k-200k', '200k-300k', '300k-400k', '400k-500k', '500k+']

# Criar uma nova coluna com as faixas de valor de casa
df['house_value_range'] = pd.cut(df['median_house_value'], bins=bins, labels=labels)

# Contar o número de registros por faixa
house_value_counts = df['house_value_range'].value_counts()

# Criar o gráfico de barras
plt.figure(figsize=(10,6))
sns.barplot(x=house_value_counts.index, y=house_value_counts.values, palette="Blues_d")

# Adicionar títulos e rótulos
plt.title('Quantidade de Registros por Faixa de Valor de Casa', fontsize=16)
plt.xlabel('Faixa de Valor de Casa', fontsize=12)
plt.ylabel('Quantidade de Registros', fontsize=12)
plt.xticks(rotation=45)  # Rotaciona os rótulos do eixo x para facilitar a leitura
plt.show()