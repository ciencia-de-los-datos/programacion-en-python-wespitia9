"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""

import csv
def pregunta_01():
    """Retorne la suma de la segunda columna. Rta/214"""
    with open('data.csv', 'r') as file:
        lines = file.readlines()

        suma_segunda_columna = 0

        for line in lines:
            # Dividir la línea en columnas
            columns = line.strip().split('\t')
        
            # Obtener el valor de la segunda columna y convertirlo a entero
            valor_segunda_columna = int(columns[1])

            suma_segunda_columna += valor_segunda_columna

    return suma_segunda_columna


def pregunta_02():
    """Retorne la cantidad de registros por cada letra de la primera columna como la lista
       de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    # Diccionario para contar la cantidad de registros por letra
    cantidad_por_letra = {}

    # Abrir CSV y leer las líneas
    with open('data.csv', 'r') as file:
        lines = file.readlines()

    for line in lines:
        # Dividir la línea en columnas
        columns = line.strip().split('\t')
        
        # Obtener la letra de la primera columna
        letra = columns[0]

        # Actualizar el contador para esa letra
        if letra in cantidad_por_letra:
            cantidad_por_letra[letra] += 1
        else:
            cantidad_por_letra[letra] = 1

    # Convertir diccionario en lista de tuplas y ordenar alfabéticamente
    lista_resultado = sorted(cantidad_por_letra.items())

    return lista_resultado

#resultado = pregunta_02()
#print(resultado)


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    suma_por_letra = {}

    with open ('data.csv', 'r') as file:
        lines = file.readlines()
    
    for line in lines:
        columns = line.strip().split('\t')

        letra = columns[0]
        valor_segunda_columna = int(columns[1])

        if letra in suma_por_letra:
            suma_por_letra[letra] += valor_segunda_columna
        else:
            suma_por_letra[letra] = valor_segunda_columna
    
    lista_resultado = sorted(suma_por_letra.items())

    return lista_resultado

resultado = pregunta_03()
print(resultado)


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    registros_por_mes = {}

    with open('data.csv', 'r') as file:
        lines = file.readlines()
    
    for line in lines:
        columns = line.strip().split('\t')

        fecha = columns[2]
        mes = fecha.split('-')[1]

        if mes in registros_por_mes:
            registros_por_mes[mes] += 1
        else:
            registros_por_mes[mes] = 1

    lista_resultado_04 = sorted(registros_por_mes.items())

    return lista_resultado_04

resultado = pregunta_04()
print(resultado)


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    valores_por_letra = {}

    with open('data.csv', 'r') as file:
        lines = file.readlines()

    for line in lines:
        columns = line.strip().split('\t')

        letra = columns[0]
        valor_segunda_columna = int(columns[1])

        if letra in valores_por_letra:
            maximo = max(valores_por_letra[letra][0], valor_segunda_columna)
            minimo = min(valores_por_letra[letra][1], valor_segunda_columna)
            valores_por_letra[letra] = (maximo, minimo)
        else:
            valores_por_letra[letra] = (valor_segunda_columna, valor_segunda_columna)

    lista_resultado_05 = sorted([(letra, maximo, minimo) for letra, (maximo, minimo) in valores_por_letra.items()])

    return lista_resultado_05

resultado = pregunta_05()
print(resultado)

def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    valores_por_clave = {}

    with open('data.csv', 'r') as file:
        lines = file.readlines()

    for line in lines:
        columns = line.strip().split('\t')

        valores = columns[4].split(',')

        for par in valores:
            clave, valor = par.split(':')
            valor = int(valor)

            if clave in valores_por_clave:
                minimo = min(valores_por_clave[clave][0], valor)
                maximo = max(valores_por_clave[clave][1], valor)
                valores_por_clave[clave] = (minimo, maximo)
            else:
                valores_por_clave[clave] = (valor, valor)

    lista_resultado = sorted([(clave, minimo, maximo) for clave, (minimo, maximo) in valores_por_clave.items()])

    return lista_resultado

resultado = pregunta_06()
print(resultado)


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    letras_por_valor = {}

    with open('data.csv', 'r') as file:
        lines = file.readlines()

    for line in lines:
        columns = line.strip().split('\t')

        valor_segunda_columna = int(columns[1])
        letra = columns[0]

        if valor_segunda_columna in letras_por_valor:
            letras_por_valor[valor_segunda_columna].append(letra)
        else:
            letras_por_valor[valor_segunda_columna] = [letra]    

    lista_resultado_07 = sorted([(valor, letras) for valor, letras in letras_por_valor.items()])
    
    return lista_resultado_07

resultado = pregunta_07()
print(resultado)


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    letras_por_valor = {}

    with open('data.csv', 'r') as file:
        lines = file.readlines()

    for line in lines:
        columns = line.strip().split('\t')

        valor_segunda_columna = int(columns[1])
        letra = columns[0]

        if valor_segunda_columna in letras_por_valor:
            letras_por_valor[valor_segunda_columna].append(letra)
        else:
            letras_por_valor[valor_segunda_columna] = [letra]

    for valor, letras in letras_por_valor.items():
        letras_por_valor[valor] = sorted(list(set(letras)))

    lista_resultado = sorted([(valor, letras) for valor, letras in letras_por_valor.items()])

    return lista_resultado

resultado = pregunta_08()
print(resultado)


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    registros_por_clave = {}

    with open('data.csv', 'r') as file:
        lines = file.readlines()

    for line in lines:
        # Dividir la línea en columnas
        columns = line.strip().split('\t')
        
        # Obtener los valores de la quinta columna y dividir por comas
        valores = columns[4].split(',')
        
        # Iterar sobre cada par clave-valor
        for par in valores:
            clave, _ = par.split(':')
            
            # Actualizar el contador para esa clave
            if clave in registros_por_clave:
                registros_por_clave[clave] += 1
            else:
                registros_por_clave[clave] = 1

    return registros_por_clave

resultado = pregunta_09()
print(resultado)


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    lista_tuplas = []

    with open('data.csv', 'r') as file:
        lines = file.readlines()

    for line in lines:
        # Dividir la línea en columnas
        columns = line.strip().split('\t')
        
        # Obtener la letra de la primera columna y las columnas 4 y 5
        letra = columns[0]
        column_4 = len(columns[3].split(','))
        column_5 = len(columns[4].split(','))

        # Agregar la tupla a la lista
        lista_tuplas.append((letra, column_4, column_5))

    return lista_tuplas

resultado = pregunta_10()
print(resultado)

def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    suma_por_letra = {}

    with open('data.csv', 'r') as file:
        lines = file.readlines()

    for line in lines:
        # Dividir la línea en columnas
        columns = line.strip().split('\t')
        
        # Obtener la letra de la cuarta columna y el valor de la segunda columna
        letras = columns[3].split(',')
        valor_segunda_columna = int(columns[1])

        # Iterar sobre cada letra y actualizar la suma
        for letra in letras:
            if letra in suma_por_letra:
                suma_por_letra[letra] += valor_segunda_columna
            else:
                suma_por_letra[letra] = valor_segunda_columna

    suma_por_letra_ordenada = {letra: suma_por_letra[letra] for letra in sorted(suma_por_letra)}    

    return suma_por_letra_ordenada

resultado = pregunta_11()
print(resultado)

def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    return
