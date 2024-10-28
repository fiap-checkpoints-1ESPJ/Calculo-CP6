import numpy as np
import matplotlib.pyplot as plt
import random
from scipy.optimize import minimize_scalar

# Função Custo Base
def C(x):
    return 250 * x**2 + 30 * x + 50

# Função Receita
def R(x):
    return 70 * x

# Função Lucro Base
def P(x):
    return R(x) - C(x)

# Função Custo com imposto variável (exemplo adicional)
def C_with_tax(x, tax_rate):
    base_cost = 250 * x**2 + 30 * x + 50
    return base_cost * (1 + tax_rate)

# Gerando valores de x
x_values = np.linspace(0, 100, 1000)  # Gera valores de x entre 0 e 100

# Calculando as funções para o exemplo base
custo_values = C(x_values)
receita_values = R(x_values)
lucro_values = P(x_values)

# Encontrando o ponto ótimo de produção para o exemplo base (maximização do lucro)
resultado = minimize_scalar(lambda x: -P(x), bounds=(0, 100), method='bounded')
ponto_otimo = resultado.x
lucro_maximo = P(ponto_otimo)

# Cálculo dos exemplos adicionais com impostos aleatórios
tax_rates = [random.uniform(0.01, 0.99) for _ in range(3)]  # Três taxas de imposto aleatórias
lucro_values_with_tax = []

for i, tax_rate in enumerate(tax_rates):
    # Calcula os valores de lucro com o imposto aleatório
    lucro_taxado = [R(x) - C_with_tax(x, tax_rate) for x in x_values]
    lucro_values_with_tax.append((lucro_taxado, tax_rate))

# Plotando os gráficos
plt.plot(x_values, custo_values, label='Custo Base C(x)', color='red')
plt.plot(x_values, receita_values, label='Receita R(x)', color='blue')
plt.plot(x_values, lucro_values, label='Lucro Base P(x)', color='green')

# Marcando o ponto ótimo de produção do exemplo base
plt.scatter(ponto_otimo, lucro_maximo, color='orange', zorder=5, label=f'Ponto ótimo base (x={ponto_otimo:.2f}, P={lucro_maximo:.2f})')

# Plotando os três exemplos adicionais com impostos aleatórios
for i, (lucro_taxado, tax_rate) in enumerate(lucro_values_with_tax):
    plt.plot(x_values, lucro_taxado, label=f'Lucro com imposto (taxa={tax_rate:.2f})', linestyle='--')

# Configurações do gráfico
plt.xlabel('Unidades Produzidas (x)')
plt.ylabel('Valor')
plt.title('Custo, Receita e Lucro em Função da Produção com Variações de Imposto')
plt.legend()
plt.grid(True)
plt.show()

# Exibindo o ponto ótimo de produção base
print(f'O ponto ótimo de produção base é x = {ponto_otimo:.2f}, com um lucro máximo de P(x) = {lucro_maximo:.2f}')
