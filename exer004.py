#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo 
#e todas as informações possíveis sobre ele.

objeto = input('Digite algo?')
print('O tipo primitivo é ', type(objeto))
print('Só tem espaços? ', objeto.isspace())
print('É um número? ', objeto.isnumeric())
print('É alfabético? ', objeto.isalpha())
print('É alfanúmerico? ', objeto.isalnum())
print('Esta em letras maiúscula? ', objeto.isupper())
print('Está em letras minúsculas? ', objeto.islower())
print('Esta capitalizada? ', objeto.istitle())
