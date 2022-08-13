def cuenta_regresiva(num):
    list = []
    for i in range(num,-1,-1):
        list.append(i)
    return list

def imprimir_devolver(lista):
    if len(lista) == 2:
        print(lista[0])
        return lista[1]
    else:
        print('ERROR!! Debe ingresar una lista con 2 elementos')    
        
def mas_longitud(lista):
    suma = len(lista) + lista[0]
    return suma

def valores_mayores(lista):
    if len(lista) >= 2:
        lista_nueva = []
        for i in range(len(lista)):
            if lista[i] > lista[1]:
                lista_nueva.append(lista[i])
        print(len(lista_nueva))
        return lista_nueva
    else:
        return False
    
def longitud_valor(tamaño,valor):
    lista = []
    for i in range(tamaño):
        lista.append(valor)
    return lista
if __name__ == "__main__":
    print(cuenta_regresiva(5))
    lista1 = [1,2,3]
    lista2 = [3,2] 
    imprimir_devolver(lista1)
    imprimir_devolver(lista2)
    print(imprimir_devolver(lista2))
    print(mas_longitud(lista1))
    print(valores_mayores(lista1))
    print(longitud_valor(6,2))