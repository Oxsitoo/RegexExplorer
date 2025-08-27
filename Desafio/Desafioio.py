import re

# Presentacion
print("""Escriba su informacion:
Nombre completo, edad, esta trabajando, cuanto gana al mes, su estatura, ponga una lista de 3 digitos primos
Ejemplo:
\"Fabian Samuel Garcia Hurtado\", 18 años, False, 0 pesos, 1.63 cm, [3, 5, 9]""")
info = input()

name = r'"(.*?)"'
nombre = re.findall(name, info)

age =  r"(?<![\[\d,\.])\b-?\d+\b(?![\],\.])" 
edad = re.findall(age, info)

work = r"\b(True|False)\b"
trabajo = re.findall(work, info)

weight = r"\b-?\d+\.\d+\b"
peso = re.findall(weight, info)

height = r"\b-?\d+\.\d+\b"
altura = re.findall(height, info)

liist = r"\[\s*\d+(?:\s*,\s*\d+)*\s*\]"
lista = re.findall(liist, info)

print("String encontrado:", nombre)
print("Entero encontrado:", edad)
print("Booleano encontrado:", trabajo)
print("Flotantes encontrados:", peso, altura)
print("Lista encontrado:", lista)