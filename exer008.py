#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

valor = float(input('Digite uma distancia em metros: '))
centimetros = valor * 100
milimetros = valor * 1000

print('A medida de {:.2f} m, corresponde a {:.2f} cm, e {:.2f} mm.'.format(valor, centimetros, milimetros))
