arr = [8,3,4,5,1,7,2,9,6,0]
# Esta funcion NO FUNCIONA para arreglos con numeros repetidos
def seleccion(arr):
    i = 0
    while (i < len(arr)-1):
        var = arr[i]
        for j in arr[i:]:
            if j < var:
                var = j
        p = arr.index(var)
        arr[i], arr[p] = arr[p], arr[i]
        i += 1
        
    return arr

print(seleccion(arr))