print ("Hola a todos, este es el segundo archivo de prueba")

def suma(numero1, numero2):
    return numero1 + numero2

def resta(numero1, numero2):    
    return numero1 - numero2

def multiplicacion(numero1, numero2):
    return numero1*numero2

def division(numero1, numero2):

    if numero2 == 0:
        print("No se puede realizar la division por cero")
    else:
        return numero1/numero2    

numero1 = 10
numero2 = 5

print("Suma de " + str(numero1) + " y " + str(numero2) + " = ", suma(numero1, numero2))
print("Resta de " + str(numero1) + " y " + str(numero2) + " = ", resta(numero1, numero2))
print("Multiplicacion de " + str(numero1) + " y " + str(numero2) + " = ", multiplicacion(numero1, numero2))
print("Division de " + str(numero1) + " y " + str(numero2) + " = ", division(numero1, numero2))
