preco_mercadoria = float(input())
quantidade = int(input())

preco_sem_desconto = preco_mercadoria * quantidade
desconto = quantidade + 10
desconto_total = desconto * preco_sem_desconto / 100
preco_com_desconto = preco_sem_desconto - desconto_total

print(f"{preco_sem_desconto:.2f}")
print(f"{preco_com_desconto:.2f}")