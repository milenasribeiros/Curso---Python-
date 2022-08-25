#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e 
# mostre quantos dólares ela pode comprar

valor = float(input("Quanto você tem na sua carteira ? R$ "))
dolar = valor / 3.27
print("Com R$ {:.2f}, você pode comprar US$ {:.2f}".format(valor, dolar))
