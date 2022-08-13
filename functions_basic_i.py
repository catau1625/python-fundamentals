#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
# imprime 5

#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
# imprime ERROR ya que la funcion number_of_days_in_a_week_silicon_or_triangle_sides no esta definida

#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
# imprime 5 ya que el primer return es con el que se queda por orden de lectura

#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
# imprime 5 ya que esa es la variable almacenada en la funcion

#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
# devuelve error ya que la funcion no tiene informacion asociada a ella

#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
# devuelve error ya que la funcion add no tiene informacion almacenada

#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
# imprime la expresion 25 de tipo string

#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
# imprime 10 ya que segun las sentencias condicionales es la que se lee primero

#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
# imprime 7
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
# imprime 14
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
# imprime 21


#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
# imprime 8

#11
b = 500
print(b)
# imprime 500
def foobar():
    b = 300
    print(b)
print(b)
# imprime 500
foobar()
# imprime 300
print(b)
# imprime 500

#12
b = 500
print(b)
# imprime 500
def foobar():
    b = 300
    print(b)
    return b
print(b)
# imprime 500
foobar()
# imprime 300
print(b)
# imprime 500

#13
b = 500
print(b)
# imprime 500
def foobar():
    b = 300
    print(b)
    return b
print(b)
# imprime 500
b=foobar()
print(b)
# imprime 300

#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
# imprime 1, 3 y 2 en ese orden

#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
# imprime 10 ya que es la variable que se asocia o almacena la funcion