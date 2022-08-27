
'''
Reubica el elemento que se encuentra en la posicion p de la lista
dentro del rango (0:p-1), un requisito de esta funcion es que p debe 
ser una posicion valida de la lista
'''

def reubicar(lista,p):
    # v es el valor a reubicar
    v = lista[p]
    
    # recorremos el segmento [0:p-1] de derecha a izquierda hasta
    # encontrar la posicion j tal que lista[j-1] <= v < lista[j]
    j = p
    while j > 0 and v < lista[j-1]:
        lista[j] = lista[j-1]
        # desplaza los elementos hacia la derecha, dejando lugar para el elemento v
        j -= 1 # nos movemos un lugar a la izquierda
        
    lista[j] = v # ubicamos a v en la nueva posicion
    return lista


'''
Ordena una lista de elementos segun el metodo de insercion, 
un requisito de la lista es que los elementos deben ser comparables
'''
def ordenamiento(lista):
    # i va desde la primera hasta la penultima posicion de la lista
    for i in range(len(lista)-1):
        # si i+1 esta desordenado respecto al anterior, se reubica en el segmento [0:i]
        if lista[i+1] < lista[i]:
            reubicar(lista, i+1)
    return lista

arr = [4,5,6,2,3,4,1]

print(ordenamiento(arr))

'''
Codigo extraido de:
https://uniwebsidad.com/libros/algoritmos-python/capitulo-19/ordenamiento-por-insercion
'''