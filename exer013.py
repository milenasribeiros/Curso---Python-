#Faça um algoritmo que leia o salário de um funcionário e 
#mostre seu novo salário, com 15% de aumento.

salario = float(input("Digite o sálario do funcionario: R$ "))
novo = salario + ( salario * 15 / 100)

print("Um funcionario que recebia R$ {:.2f}, com o aumento vai passar a receber R$ {:.2f}." . format(salario, novo))
