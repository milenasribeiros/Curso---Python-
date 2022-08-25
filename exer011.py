#Faça um programa que leia a largura e a altura de uma parede em metros, 
#calcule a sua área e a quantidade de tinta necessária para pintá-la, 
#sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

larg = float(input("Digite a largura da parede: "))
alt = float (input("Digite a altura da parede: "))
área = larg * alt 
print("Sua parde tem a dimensão de {} x {} e sua área é de {} m.". format(larg, alt, área))
tinta = área / 2
print("Para pintar essa parede, você precisa de {} l de tinta.".format(tinta))
