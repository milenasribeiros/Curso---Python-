#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5 % de desconto.


valor = float(input("Digite o valor do produto: R$ "))
desconto = valor - (valor * 5/100)

print("O produto que custa R$ {:.2f}, na promoção com desconto fica de R$ {:.2f}." .format(valor, desconto))
