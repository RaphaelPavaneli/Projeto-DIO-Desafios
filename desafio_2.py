#Leia um valor inteiro entre 1 e 12, inclusive. Correspondente a este valor, deve ser apresentado como resposta o mês do ano por extenso, 
#em inglês, com a primeira letra maiúscula.

month = int(input())

months_dict = {1:"January", 2:"February", 3:"March", 4:"April", 5:"May", 6:"June", 7:"July", 8:"August", 9:"September", 10:"Octomber", 11:"November", 12:"December"}

if month == 1:
    print(months_dict[1])
elif month == 2:    
    print(months_dict[2])
elif month == 3:
    print(months_dict[3])
elif month == 4:
    print(months_dict[4])
elif month == 5:
    print(months_dict[5])
elif month == 6:
    print(months_dict[6])
elif month == 7:
    print(months_dict[7])    
elif month == 8:
    print(months_dict[8])
elif month == 9:
    print(months_dict[9])
elif month == 10:
    print(months_dict[10])
elif month == 11:
    print(months_dict[11])
elif month == 12:
    print(months_dict[12])
else:
    print("Mês inexistente!")