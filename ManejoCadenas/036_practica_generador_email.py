# Práctica de generador de email

print("Introduzca nombre y apellidos")
nombre = str(input())
nombre = nombre.replace(" ", ".").lower

print("Introduzca el nombre de su empresa")
empresa = str(input())
empresa = empresa.replace(" ", "").lower

email = nombre + "@" + empresa + ".com"
print(email)
