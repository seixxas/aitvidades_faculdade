divida = int(input())
ramon = int(input())

pagamentos = 0
while divida != 0:
    pagamentos += 1 
    print(f"pagamento: {pagamentos}")
    print(f"antes = {divida}")
    divida -= ramon
    if divida < 0:
        divida = 0
    print(f"depois = {divida}")
    print("-----")