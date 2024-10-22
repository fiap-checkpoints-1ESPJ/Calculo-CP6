import numpy as np
import matplotlib.pyplot as plt
import random
from scipy.optimize import minimize_scalar

# Função Custo
def C(x):
    return 250 * x**2 + 30 * x + 50

# Função Receita
def R(x):
    return 70 * x

# Função Lucro
def P(x):
    return R(x) - C(x)

# Função Custo com imposto
def C_with_tax(x):
    tax_rate = random.uniform(0.01, 0.99)  # Taxa de imposto aleatória entre 0.01 e 0.99
    base_cost = 250 * x**2 + 30 * x + 50
    return base_cost * (1 + tax_rate)

# Plotando as funções
x_values = np.linspace(0, 100, 1000)  # Gera valores de x entre 0 e 100

# Calculando as funções
custo_values = C(x_values)
receita_values = R(x_values)
lucro_values = P(x_values)

# Encontrando o ponto ótimo de produção (maximização do lucro)
resultado = minimize_scalar(lambda x: -P(x), bounds=(0, 100), method='bounded')
ponto_otimo = resultado.x
lucro_maximo = P(ponto_otimo)

# Plotando os gráficos
plt.plot(x_values, custo_values, label='Custo C(x)', color='red')
plt.plot(x_values, receita_values, label='Receita R(x)', color='blue')
plt.plot(x_values, lucro_values, label='Lucro P(x)', color='green')

# Marcando o ponto ótimo de produção em laranja
plt.scatter(ponto_otimo, lucro_maximo, color='orange', zorder=5, label=f'Ponto ótimo (x={ponto_otimo:.2f}, P={lucro_maximo:.2f})')

# Configurações do gráfico
plt.xlabel('Unidades Produzidas (x)')
plt.ylabel('Valor')
plt.title('Custo, Receita e Lucro em Função da Produção')
plt.legend()
plt.grid(True)
plt.show()

# Exibindo o ponto ótimo de produção
print(f'O ponto ótimo de produção é x = {ponto_otimo:.2f}, com um lucro máximo de P(x) = {lucro_maximo:.2f}')
