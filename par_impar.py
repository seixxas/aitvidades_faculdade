numero = int(input())


if(numero % 2 == 0 ):
    par = numero + 2 
    impar = numero - 1
    
else:
    par = numero + 1
    impar = numero - 2
    
print(f"{impar} {par} ")
    