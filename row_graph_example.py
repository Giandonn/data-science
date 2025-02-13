import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_name = "/content/sample_data/california_housing_test.csv"
df = pd.read_csv(file_name)

# Agrupar o DataFrame pela idade das casas e calcular a média do valor da casa
avg_house_value_by_age = df.groupby('housing_median_age')['median_house_value'].mean().reset_index()

# Criar o gráfico de linha
plt.figure(figsize=(12,6))
sns.lineplot(x='housing_median_age', y='median_house_value', data=avg_house_value_by_age, marker='o', color='g')

# Adicionar títulos e rótulos
plt.title('Evolução do Valor Médio da Casa ao Longo da Idade das Casas', fontsize=16)
plt.xlabel('Idade das Casas', fontsize=12)
plt.ylabel('Valor Médio da Casa (em dólares)', fontsize=12)
plt.grid(True)
plt.show()