#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
#A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = float(input('Qual a velocidade do seu carro? '))
if velocidade >= 80:
    print('Você foi multado! Excedeu o limite que é de 80km/h')
    multa = (velocidade - 80) * 7
    print('Valor da multa R${:.2f}.'.format(multa)) 
print('Tenha um bom dia! Dirija com segurança.')
