#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

nota01 = float(input('Digite sua primeira nota:'))
nota02 = float(input('Digite sua segunda nota:'))
media = (nota01 + nota02) / 2

print('A media entre {:.1f} e {:.1f}, é {:.1f}.'.format(nota01, nota02, media))
