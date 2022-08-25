#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

import math

valor = float(input("Digite um valor: "))
print("O número {} tem a parte inteira {}.".format (valor, math.trunc(valor)))
