#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 
#e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
#O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep

computador = randint(0,5)
print('Vou pensar em um número de 0 a 5, número escolhido!')
jogador = int(input('Tente advinhar qual o número que foi escolhido: '))
print('Processando...')
sleep(3)
if computador == jogador:
    print('Parabéns, você acertou!')
else:
    print('Não foi dessa vez, o número era {}.'.format(computador))
