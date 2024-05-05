from random import randint
from random import randrange
from random import choices
from math import pi, pow
from math import sqrt

# Transformando a quantidade de participantes de string para inteiro
n = int(input("Digite o nº de participantes do sorteio: "))
# Sorteando um número no intervalo de 1 até a quantidade de participantes
print(f"O número sorteado foi {randint(1, n)}")


nome = input("Qual o seu nome? ")
# Gerando um token par de 1000 a 9998. O randrange tem o intervalo aberto em 10000, ou seja,
# não considera 10000 como opção de escolha (token >= 1000 e token < 10000)
token = randrange(1000, 10000, 2)

print(f"Olá, {nome}, o seu token de acesso é {token}! Seja bem-vindo(a)!")


# Lista das frutas disponíveis
frutas = ["maçã", "banana", "uva", "pêra","manga", "coco", 
          "melancia", "mamão", "laranja", "abacaxi", "kiwi", "ameixa"]

# Gerando uma lista com a escolha aleatoria de 3 frutas 
salada = choices(frutas, k=3)

# Imprimindo os itens da lista de frutas gerada
print(f"A salada surpresa é: {salada[0]}, {salada[1]} e {salada[2]}")



numeros = [2, 8, 15, 23, 91, 112, 256]
# iniciando uma lista vazia para receber as raízes
raiz = []

# laço for para calcular cada raiz da lista de números e adicionar a lista raiz
for numero in numeros:
  raiz.append(sqrt(numero))

# laço for para ler a lista raiz e exibir um texto só quando a raiz for um valor inteiro 
for i in range(len(raiz)):
  # condição para testar se um número é inteiro (Ex: 2.5 // 1 = 2 ... 2 != 2.5)
  if raiz[i] // 1 == raiz[i]:
    print(f"O número {numeros[i]} possui raiz quadrada inteira igual a {int(raiz[i])}")

# importando 2 métodos da mesma biblioteca


raio = float(input("Digite o raio da área circular em metros: "))
# Cálculo da área com os métodos da math e obtenção do custo em reais
area = pi*pow(raio,2)
valor = area * 25.00

# Exibição do cálculo e custo na tela. O round(n,2) arredonda qualquer número em 2 casas decimais
print(f"Você precisará pagar R$ {round(valor,2)} por uma área de {round(area,2)} metros de grama")
