# Buscar en subcadenas con Find

cadena = "Hola, mundo!"

indice = cadena.find("mundo")
print(f"Índice de la subcadena mundo : {indice}") # Muestra 6

indice = cadena.find("hola")
print(f"Índice de la subcadena Hola: {indice}") # Falla pues hola no es lo mismo que Hola (H no es lo mismo que h)