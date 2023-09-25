"""
Ejercicios Practicos con estructuras de datos
"""

def sum_elements(colection_a, colection_b):
    """
    Escribe una funcion que tome dos listas como entrada y devuleva 
    una nueva lista que contenga la suma de los elementos 
    correspondientes de ambas listas.

    """
    result = []

    if len(collection_a) != len(collection_b):
        return False

    for i in range(0, len(collection_a)):
        result.append(collection_a[i] + collection_b[i])

    return result    


def max_min(numbers):
    """
    Escribe una función que tome una lista de números como entrada y 
    devuelva el número máximo y mínimo de la lista.
    """
    # numbers = sorted(numbers, reverse=True)

    # max = numbers[0]
    # min = numbers [-1]
    # return max, min
    return max(numbers), min(numbers) # Tuple


def remove_duplicates(elements):
    """
    Escribe una función que tome una lista como entrada y devuelva 
    una nueva lista sin elementos duplicados.
    """
    uniques = set(elements)
    return list(uniques)


def len_word(sentences):
    """
    Escribe una función que tome una lista de palabras como entrada y 
    devuelva una tupla, de un solo elemento, con las palabras más 
    largas de la lista.
    """
    max_size = 0
    max_element = None

    for element in sentences:
        if len(element) > max_size:
            max_element = element
            max_size = len(element)
    return(max_element)


def order(numbers):
    return numbers[::-1]


def media_mediana(elements):
    
    average = sum(elements) / len(elements)
    pivot = len(elements) // 2

    return average, elements[pivot]



#collection_a = ['a', 'ab', 'abc', 'cody', 'codigofacilito']
#collection_b = [10, 20, 30]
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = a[::-1]

print(
    media_mediana(a)
)
# result = order(collection_a)
# print(result)


