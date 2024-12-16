def calcular_promedio(numeros):
 

     suma = 0
 

     i = 0
 

     for i in range(1, 3 + 1):     

               suma = suma + numeros[i]   

               i = i + 1           
 

     promedio = suma / 3 

     return promedio 
 

 

 
def main():
 

     numero1 = 10
 

     numero2 = 20
 

     numero3 = 30
 

     lista = [10, 20, 30] 

     resultado = calcular_promedio(lista) 

     if (resultado < 50):
   

          print("El promedio no es aprobatorio: " + str(resultado))      
     else:   

          print("El promedio es aprobatorio: " + str(resultado))      
 
 

 
 

 
main()