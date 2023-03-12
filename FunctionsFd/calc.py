# funcion 
def sumar (a,b):
    """Suma dos valores recibidos"""  # DOCUMENTACION
    return a+b

def calcular (a,b):    
    """Suma, resta, multiplica y divide dos valores recibidos

       Recibe dos valores y realiza cuantro operaciones

       1. Suma de los valores
       2. Resta del primer valor menos el segundo
       3. Multiplica los valores
       4. Divide el primer valor entre el segundo

       Args:
         a (int) primer valor

         b (int) segundo valor

       Returns:
         res1 (any): suma de los valores  
         res2 (any): resta de los valores  
         res3 (any): multiplicacion de los valores  
         res4 (any): division de los valores           
    """
    return a+b,a-b,a*b,a/b