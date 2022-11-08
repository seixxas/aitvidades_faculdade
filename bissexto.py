def bisexto(ano):
    return (ano%4==0 and ano%100!=0) or (ano%400==0)
ano_comeco = int(input())
ano_fim = int(input())

qntd_bissexto = 0

for ano in range(ano_comeco, ano_fim + 1):
    if bisexto(ano):
        print(ano)
        qntd_bissexto +=1

print(f"bissextos: {qntd_bissexto}")    