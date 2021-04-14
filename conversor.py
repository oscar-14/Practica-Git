pesos = input("¿cuantos CLP tienes?: ")
pesos = float(pesos)
valor_dolar = 708.28
mis_dolares = pesos / valor_dolar
mis_dolares = round(mis_dolares, 2)
mis_dolares = str(mis_dolares)
print("tienes $" + mis_dolares + " dolares")
