def es_primo(numero):
 

     if (numero <= 1):
   

          return False      
 

     i = 2
 

     for i in range(numero - 1):
     

               if (numero % i == 0):
       

                    return False                
   

               i = i + 1           
 

     return True 
 

 
 

 

 
 

 
def main():
 

     numero = 7
 

     resultado = es_primo(numero) 

     if (resultado):
   

          print(str(numero) + " es un número primo.")      
     else:   

          print(str(numero) + " no es un número primo.")      
 
 

 
 

 
main()