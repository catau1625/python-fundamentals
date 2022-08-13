num1 = 42 # variable declaration, number
num2 = 2.3 # variable declaration, number
boolean = True # variable declaration, boolean
string = 'Hello World' # variable declaration, string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # composite variable, list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #composite variable, dictionary
fruit = ('blueberry', 'strawberry', 'banana') # composite variable, tuple
print(type(fruit)) # return function, argument function
print(pizza_toppings[1]) # return function, parameter function
pizza_toppings.append('Mushrooms') # return function, parameter funciton
print(person['name']) #return function, parameter function
person['name'] = 'George' # variable declaration, dictionary variable
person['eye_color'] = 'blue' # variable declaration, dictionary variable
print(fruit[2]) # return function, parameter

if num1 > 45:# parameter function
    print("It's greater")#return function
else:
    print("It's lower")

if len(string) < 5: # argument function
    print("It's a short word!")#return function
elif len(string) > 15:# argument funciton
    print("It's a long word!")# return function
else:
    print("Just right!")

for x in range(5): #parameter function
    print(x)# return function
for x in range(2,5):#parameter function
    print(x)#return function
for x in range(2,10,3):#parameter function
    print(x)#return function
x = 0#variable declaration, number
while(x < 5):#parameter function
    print(x)#return function
    x += 1#variable declaration, number

pizza_toppings.pop()#parameter function
pizza_toppings.pop(1)#parameter function

print(person)#return function
person.pop('eye_color')#parameter function
print(person)#return function

for topping in pizza_toppings:#parameter function
    if topping == 'Pepperoni':#argument function
        continue#argument function
    print('After 1st if statement')#return function
    if topping == 'Olives':#argument function
        break#argument function

def print_hello_ten_times():#return function
    for num in range(10):
        print('Hello')

print_hello_ten_times()#return function

def print_hello_x_times(x):#argument function
    for num in range(x):
        print('Hello')

print_hello_x_times(4)#return function

def print_hello_x_or_ten_times(x = 10):#parameter function
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()#return function
print_hello_x_or_ten_times(4)#return function


"""
Bonus section
"""

# print(num3) #comment, return function
# num3 = 72 #comment, variable declaration, number
# fruit[0] = 'cranberry' #comment, dictionary variable declaration
# print(person['favorite_team'])#comment, return function, dictionary variable 
# print(pizza_toppings[7])#comment, return function, list variable
#   print(boolean) #comment, index error, return function, boolean variable
# fruit.append('raspberry') #comment, argument function, list variable
# fruit.pop(1) #comment, argument function, list variable