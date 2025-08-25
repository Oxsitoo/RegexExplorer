# Reto 3: Buscar valores booleanos en un texto usando regex
# Paso a paso:
# 1. Leer el texto de entrada.
# 2. Definir una expresión regular para encontrar valores booleanos (True/False).
# 3. Buscar todos los booleanos en el texto.
# 4. Imprimir los resultados.

import re

texto = "La respuesta es True, pero a veces es False, pero mi amor por el es True"

# Expresión regular para booleanos (True o False, case-insensitive)
# patron = r"\\b(True|False)\\b"

patron = r"\b(True|False)\b"

# Buscar todos los booleanos
booleans = re.findall(patron, texto, re.IGNORECASE)

print("Booleanos encontrados:", booleans)
# Paso a paso:
# 1. Cambia el texto de prueba.
# 2. Modifica la expresión regular si es necesario.
# 3. Ejecuta el script y observa los resultados.
