#Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

numero = int(input('Digite um número? '))
antecessor = numero - 1
sucessor = numero + 1
print('O número que você digitou é {}, o seu sucessor é {} e o antecessor é {}.'.format(numero, antecessor, sucessor))