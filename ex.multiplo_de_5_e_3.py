def multiplo_de_5_e_3(numero):
    if numero % 5 == 0 and numero % 3 == 0:    
        return True
    else:
        return False

    

numero = int(input("digite um número"))
if multiplo_de_5_e_3(numero):
    print(f"o número {numero} e multiplo de 5 e 3")
else : 
    print(f"o número {numero} nao e multiplo de 5 e 3") 





