import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv(r'data/raw/tips.csv')

# Verificação de informações nulas
# print(df.isnull().any())

df['pct'] = round(df['tip'] / df['total_bill'], 2)
df.to_csv('data/ready/restaurant_tips.csv')

print(df.shape)
print(df.dtypes)
print(df.head())
print(f'Valor total de gorjetas: {round(df["tip"].sum(), 2)}')
print(f'Média de gorjetas oferecidas: {round(df["tip"].mean(), 2)}')
print(f'Média de gorjetas recebidas por mulheres: {round(df.groupby("sex")["tip"].mean()[0], 2)}')
print(f'Média de gorjetas recebidas por homens: {round(df.groupby("sex")["tip"].mean()[1], 2)}')

df.groupby('sex')['tip'].sum().plot.barh(title='Gorjetas x Sexo')
plt.ylabel('Sexo')
plt.xlabel('Gorjeta ($)')
plt.show()


