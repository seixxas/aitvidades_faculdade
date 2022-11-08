inicio = int(input())
fim = int(input())
cont = 0

for num in range(inicio,fim + 1):
    if num > 1:
        for i in range(2,num):
            if(num % i) == 0:
                break
        else:
            print(num)
            cont +=1
print(f"primos: {cont}")