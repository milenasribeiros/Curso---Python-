#Um professor quer sortear um dos seus quatro alunos para 
#apagar o quadro. Faça um programa que ajude ele, lendo o nome
#dos alunos e escrevendo na tela o nome do escolhido.

import random
from typing import List

nome1 = str(input('Primeiro aluno: '))
nome2 = str(input('Segundo aluno: '))
nome3 = str(input('Terceiro aluno:'))
nome4 = str(input('Quarto aluno:'))

lista = [nome1, nome2, nome3, nome4]
escolhido = random.choice(lista)
print('O escolhido é {}'.format(escolhido))
