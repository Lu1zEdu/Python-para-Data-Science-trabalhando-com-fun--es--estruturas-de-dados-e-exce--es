from math import pow
from random import choice

import numpy as np

lista = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77]
print(f"Número escolhido: {choice(lista)}")

base = int(input("Digite a base da potência: "))
expoente = int(input("Digite o expoente da potência: "))
print(f"{base} elevado a {expoente} é igual a {pow(base, expoente)}")
