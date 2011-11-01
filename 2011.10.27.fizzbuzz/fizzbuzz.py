def fizzbuzz(numero):
    if numero % 3 == 0 and numero % 5 == 0:
        return "fizzbuzz"    
    elif numero % 3 == 0: 
         return "fizz"
    else:
         if numero % 5 == 0:
             return "buzz"
         else:    
             return numero
            

