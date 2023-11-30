def numero_primo(numero):
    if numero == 1 or numero == 0:
        return False
    
    for divisor in range(2,numero):
        if numero% divisor == 0:
            return False
         return True


