"""1 - Crie um programa que imprima os números de 1 a 10 usando um laço for"""

for number in range(1,11):
    print(number)

"""2 - Crie um programa que imprima os números de 1 a 10 usando um laço while """

number = 1
while number != 11:
    print(number)
    number += 1

"""3 - Crie uma função que receba dois números e retorne a soma deles."""

a = int(input("Informe o primeiro numero: "))
b = int(input("Informe o segundo numero: "))
print(f"Soma: {a + b}")

"""4 - Escreva um programa que leia um número e informe se ele é positivo, negativo ou zero."""

number = int(input("informe o numero par ser verificado"))
if number > 0:
    print("Positivo")
elif number < 0:
    print("Negativo")
else:
    print("Zero")

"""5 - Crie um programa que peça um nome e exiba uma saudação personalizada."""

nome = str(input("Informe seu nome: "))
print (f"Bem vindo {nome}")

"""6 - Faça um programa que calcule a média de três notas informadas pelo usuário."""

a = int(input("informe o primeiro numero: "))
b = int(input("informe o segundo numero: "))
c = int(input("informe o terceiro numero: "))

media = (a + b + c)/3
print(media)

"""7 - Crie um programa que converta temperatura de Celsius para Fahrenheit."""

celcius = int(input("Informe quantos Celcius esta fazendo: "))

fahrenheit = (celcius * 9/5) + 32

print(f"Em fahrenheitm esta fazendo {fahrenheit}")

"""8 - Escreva um programa que leia um número e exiba sua tabuada de 1 a 10."""

tabuada = int(input("informe o numero na qual será feito à tabuada: "))
for number in range(1,11):
    print(f"{tabuada} * {number} = {tabuada * number}")

"""9 - Crie uma função que receba um número e retorne True se ele for primo e False caso contrário."""

num_primo = int(input("Informe o numero para verificação: "))
def e_primo(num):
    if num < 2:
        return False
    if num in [2,3,5,7,11,13]:
        return True
    if num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0 or num % 11 == 0 or num % 13 == 0:
        return False

print(e_primo(num_primo))


"""10 - Faça um programa que peça um número e imprima todos os divisores dele."""
numero = int(input("Digite um número: "))

divisores = []

for i in range(1, numero + 1):
    if numero % i == 0:
        divisores.append(i)

print(f"Os divisores de {numero} são: {divisores}")

"""11 - Crie um programa que leia um numero e imprima se ele é par ou impar"""
try:
    number = int(input("Digite um numero: "))
    if number % 2 == 0:
        print("Par")
    else:
        print("Impar")

except ValueError:
    print("Erro: Digite um valor valido")

"""12 - Escreva uma função que verifique se uma string é um palíndromo."""
def verificar_palindromo(texto):
    texto = texto.replace(" ", "").lower()
    return texto == texto[::-1]


entrada = input("Digite uma palavra ou frase: ")
if verificar_palindromo(entrada):
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")

"""13 - Peça dois números ao usuário e imprima o maior deles."""

a = int(input("Informe o primeiro numero: "))
b = int(input("Informe o segundo numero: "))

if a > b:
    print("o primeiro numero é maior")
elif a < b:
    print("o segundo numero é maior")
else:
    print("os numeros são iguais")

"""14 - Crie um programa que gere e imprima 10 números aleatórios entre 1 e 100."""

import random
for number in range(10):
    num1_100 = random.randint(1,100)
    print(num1_100)

"""15 - Escreva um programa que peça o nome do usuário e imprima as iniciais em maiúsculas."""

nome_maiusculo = input("informe seu nome usando letras minusculas ").title()

print(nome_maiusculo)