import numpy as np
import matplotlib.pyplot as plt
import random
from scipy.optimize import minimize_scalar

def C(x):
    return 250 * x**2 + 30 * x + 50

def R(x):
    return 70 * x

def P(x):
    return R(x) - C(x)

def C_with_tax(x, tax_rate):
    base_cost = 250 * x**2 + 30 * x + 50
    return base_cost * (1 + tax_rate)

x_values = np.linspace(0, 100, 1000)
custo_values = C(x_values)
receita_values = R(x_values)
lucro_values = P(x_values)
resultado = minimize_scalar(lambda x: -P(x), bounds=(0, 100), method='bounded')
ponto_otimo = resultado.x
lucro_maximo = P(ponto_otimo)
tax_rates = [random.uniform(0.01, 0.99) for _ in range(3)]
lucro_values_with_tax = []
for i, tax_rate in enumerate(tax_rates):
    lucro_taxado = [R(x) - C_with_tax(x, tax_rate) for x in x_values]
    lucro_values_with_tax.append((lucro_taxado, tax_rate))
plt.plot(x_values, custo_values, label='Custo Base C(x)', color='red')
plt.plot(x_values, receita_values, label='Receita R(x)', color='blue')
plt.plot(x_values, lucro_values, label='Lucro Base P(x)', color='green')
plt.scatter(ponto_otimo, lucro_maximo, color='orange', zorder=5, label=f'Ponto ótimo base (x={ponto_otimo:.2f}, P={lucro_maximo:.2f})')
for i, (lucro_taxado, tax_rate) in enumerate(lucro_values_with_tax):
    plt.plot(x_values, lucro_taxado, label=f'Lucro com imposto (taxa={tax_rate:.2f})', linestyle='--')

plt.xlabel('Unidades Produzidas (x)')
plt.ylabel('Valor')
plt.title('Custo, Receita e Lucro em Função da Produção com Variações de Imposto')
plt.legend()
plt.grid(True)
plt.show()
print(f'O ponto ótimo de produção base é x = {ponto_otimo:.2f}, com um lucro máximo de P(x) = {lucro_maximo:.2f}')
