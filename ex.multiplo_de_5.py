def multiplo_de_5(numero):
    if numero % 5 == 0:    
        return True
    else:
        return False

numero = int(input("digite um número"))
if multiplo_de_5(numero):
    print(f"o número {numero} e multiplo de 5")
else : 
    print(f"o número {numero} nao e multiplo de 5") 

multiplo_de_5()   