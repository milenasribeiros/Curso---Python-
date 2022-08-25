#Crie um programa que leia o nome de uma cidade 
#diga se ela começa ou não com o nome “SANTO”.

cidade = str(input('Digite o nome de uma cidade : ')).strip()

print('Se a cidade que você digitou começa com o nome "Santo"')
print('Vai aparacer True na tela, caso não vai aparecer False')
print('------------------------------------------------------')
print (cidade[:5].upper() == 'SANTO')
