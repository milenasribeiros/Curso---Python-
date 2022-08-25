#Faça um programa que leia três números e mostre 
#qual é o maior e qual é o menor.

numeroum = int(input('Digite o primeiro valor: '))
numerodois = int(input('Digite o segundo valor: '))
numerotres = int(input('Digite o terceiro valor: '))
#verificar menor
menor = numeroum
if numerodois < numeroum and numerodois < numerotres:
    menor = numerodois
if numerotres < numeroum and numerotres < numerodois:
    menor = numerotres
#verificar maior
maior = numeroum
if numerodois > numeroum and numerodois > numerotres:
    maior = numerodois
if numerotres > numeroum and numerotres > numerodois:
    maior = numerotres
print('O menor valor digitado é {}.'.format(menor))
print('O maior valor digitado é {}.'.format(maior))
