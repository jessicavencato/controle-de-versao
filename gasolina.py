import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carrega os dados do arquivo CSV
gasolina_df = pd.read_csv('gasolina.csv')

# Cria o gráfico de linha
plt.figure(figsize=(10, 5))
sns.lineplot(x='dia', y='venda', data=gasolina_df)
plt.title('Preço da Gasolina em São Paulo - Julho de 2021')
plt.xlabel('Dia')
plt.ylabel('Preço (R$)')
plt.grid(True)

# Salva o gráfico em um arquivo PNG
plt.savefig('gasolina.png')

# Mostra o gráfico (opcional)
plt.show()
