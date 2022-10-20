from operator import indexOf


nota_trabalho = float(input())
nota2 = float(input())

media = (nota_trabalho + nota2) / 2
print(media)
if(media >= 6):
    print('aprovado')
elif(media <= 6 and nota_trabalho >= 2):
    print('talvez com a sub')
else:
    print('reprovado')