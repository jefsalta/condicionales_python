# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

from email import message_from_string


texto_1 = '7'
texto_2 = '5'

# 1-Verifique cual de los dos textos es mayor alfabéticamente
# La comparación alfabética es aquella que se logra cuando
# se utiliza el operador mayor o menor con Strings (textos)
# Imprima en pantalla según corresponda
if texto_1 > texto_2:
    print("Texto_1: {} es mayor que texto_2: {}".format(texto_1,texto_2))
else:
    if texto_2 > texto_1:
        print("texto_2: {} es mayor que texto_1: {}".format(texto_2,texto_1))
    else:
        print("Ambos textos son iguales. (Texto= {})".format(texto_1))


# 2-Transforma esas variables tipo texto en variables numéricas con (int)
# y almacénalas en nuevas variables.
# Compare las nuevas variables para ver cual es mayor o menor
# utilizando los operadores correspondientes
# ¿Cuál de las nuevas variables es mayor?
# Imprima en pantalla según corresponda
numero_1= int(texto_1)
numero_2= int(texto_2)
if numero_1 > numero_2:
    print("número_1: {} es mayor que número_2: {}".format(numero_1,numero_2))
else:
    if numero_2 > numero_1:
        print("número_2: {} es mayor que número_1: {}".format(numero_2,numero_1))
    else:
        print("Ambos números son iguales. (número= {})".format(numero_1))

# Para pensar!
# ¿Por qué cree que texto_2 es mayor a texto_1?
# Siendo números tiene sentido, pero son caracteres, texto,
# aún así el operador arroja el mismo resultado que con las
# variables numéricas, cierto? ¿Por qué creen que es así?
'''Arroja el mismo resultado, porque la comparación de textos se hace usando la posición de los
dígitos según su ubicación en el código ASCII y el texto 5 se encuentra en la posición 53 
mientras que el texto 7 se encuentra en la posición 55, por tanto '5' es menor que '7' 
(por la posición que ocupa cada uno)'''
# Esta pregunta estará repetida en el Campus para que puedan
# responder.
# NOTA: La respuesta no se encuentra en el apunte, sino en Google ;)
