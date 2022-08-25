#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n * n 

print('Você digitou o número {}, o dobro é {}, o triplo é {}, e a raiz quadrada é {:..2f}.'.format(n,d,t,r))
