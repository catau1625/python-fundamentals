x = [ [5,2,3], [10,8,9] ] 
estudiantes = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0]=15
estudiantes[0]['last_name']='Bryant'
directorio_deportes['fútbol'][0]='Andrés'
z[0]['y']=30

def iterateDictionary(some_list):
    cadena = ''
    lista = []
    for i in some_list:
        cadena = 'first_name - '+i['first_name']+', last_name - '+i['last_name']
        lista.append(cadena)
    for i in lista:
        print(i)
    return lista

estudiantes = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

#iterateDictionary(estudiantes)

def iterateDictionary2(key_name, some_list):
    for i in some_list:
        print(i[key_name])

#iterateDictionary2('first_name',estudiantes)

def printInfo(some_dict):
    for i in some_dict:
        print(str(len(i))+i)
        for j in some_dict[i]:
            print(j)
    
    
dojo = {
   'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

printInfo(dojo)