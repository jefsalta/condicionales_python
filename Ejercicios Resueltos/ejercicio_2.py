# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Comparadores
# Ingrese dos palabras cualesquiera y realice las sigueintes
# comparaciones entre ellas
texto_1 = str(input('Ingrese la primera palabra:\n'))

texto_2 = str(input('Ingrese la segunda palabra:\n'))

# Compare cual de las dos palabras es mayor (alfabéticamente)
# Imprima en pantalla según corresponda
# En la resolución se hace la distinción entre mayúsculas y minúsculas, según el código ASCII
if texto_1 > texto_2:
    print("La palabra {} es mayor que {}".format(texto_1,texto_2))
elif texto_1 < texto_2:
    print("La palabra {} es mayor que {}".format(texto_2,texto_1))
else:
    print("Ambas palabras son iguales")
    
# Compare cual de las dos palabras tiene mayor
# cantidad de letras
# Imprima en pantalla según corresponda
if len(texto_1) > len(texto_2):
    print("La palabra {} tiene más letras que la palabra {}".format(texto_1,texto_2))
elif len(texto_1) < len(texto_2):
    print("La palabra {} tiene más letras que la palabra {}".format(texto_2,texto_1))
else:
    print("Las dos palabras tienen la misma cantidad de letras ({} - letras)".format(len(texto_1)))

# Verifique si la primera letra de la primera palabra
# es mayor a la primera letra de la segunda palabra
# Imprima en pantalla según corresponda
# En la resolución no se distingue entre mayusculas y minusculas
if texto_1[0].upper() > texto_2[0].upper():
    print("La primera letra de la palabra {} es mayor que la primera letra de la palabra {}".format(texto_1,texto_2))
elif texto_1[0].upper() < texto_2[0].upper():
    print("La primera letra de la palabra {} es mayor que la primera letra de la palabra {}".format(texto_2,texto_1))
else:
    print("Las dos palabras comienzan con la misma letra ({})".format(texto_1[0].upper()))

copia_texto_1 = texto_1  # Copia de la variable texto_1

# Verifique que copia_texto_1 es igual a texto_1
# Imprima en pantalla según corresponda
if texto_1 == copia_texto_1:
    print("El contenido de texto_1 y copia_texto_1 son iguales. ({})".format(copia_texto_1))
else:
    print("El contenido de texto_1 y copia_texto_1 NO coinciden")

# Verifique que copia_texto_1 es distinta a texto_2
# Imprima en pantalla según corresponda
if texto_2 != copia_texto_1:
    print("El contenido de texto_2: ""{}"" y copia_texto_1: ""{}"" son distintos".format(texto_2,copia_texto_1))
else:
    print("El contenido de texto_2 y copia_texto_1 son iguales ({})".format(texto_2))
