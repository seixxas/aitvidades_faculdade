dia_compra = input()
dia_entrega = int(input())
dias_semana = ['domingo', 'segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado' ]

data_compra = dias_semana.index(dia_compra)
entrega = dias_semana[(data_compra + dia_entrega) % len(dias_semana)]


if(dia_entrega == 0):
    print('chega hoje!')
else:
    print(f'sera entregue {entrega}')