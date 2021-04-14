PESO_CLP = 708.28
PESO_ARG = 0.01079
PESO_COP = 0.00027

pais = ""
valor_dolar = 0.0

def conversor(pais, valor_dolar):
    pesos = input("\n"+"¿cuantos pesos " + pais + "tienes?: ")
    pesos = float(pesos)
    mis_dolares = str(round(pesos / valor_dolar, 2))
    return mis_dolares

def opciones(opcion):
    if (opcion == 1):
        valor_dolar = PESO_CLP
        pais = "chilenos"
    elif (opcion == 2):
        valor_dolar = PESO_ARG
        pais = "argentinos"
    elif (opcion == 3):
        valor_dolar = PESO_COP 
        pais = "colombianos"
    return conversor(pais, valor_dolar)        

menu = """
Bienvenido al conversor de monedas 💰

1. peso chile
2. peso argentino
3. peso colonbiano
"""
print(menu)
opcion = int(input("elija una opción: "))  
print("\n"+"tienes $" + opciones(opcion) + " dolares")
