def basico(num1,num2):
    for i in range(num1,num2+1):
        print(i)

def multiplos(num1,num2,multiplo):
    for i in range(num1,num2+1):
        if i%5 == 0:
            print(i)

def dojo_count(num1,num2):
    for i in range(num1,num2+1):
        if i%10 == 0:
            print('Coding Dojo')
        elif i%5 == 0:
            print('Coding')
        else:
            print(i)

def whoa(num1,num2):
    sum = 0
    for i in range(num1,num2+1):
        if i%2 != 0:
            sum = sum + i
        else:
            pass
    print(sum)

def cuenta_regresiva(num1,num2,space):
    for i in range(num1,num2,space):
        print(i)

def contador_flexible(lowNum,highNum,mult):
    for i in range(lowNum,highNum+1):
        if i%mult == 0:
            print(i)

if __name__ == "__main__":
    print('BASICO')
    basico(0,150)
    print('*******************')
    print('MULTIPLOS')
    multiplos(5,1000,5)
    print('*******************')
    print('DOJO COUNT')
    dojo_count(1,100)
    print('*******************')
    print('WHOA')
    whoa(0,500000)
    print('*******************')
    print('CUENTA REGRESIVA')
    cuenta_regresiva(2018,0,-4)
    print('*******************')
    print('CONTADOR FLEXIBLE')
    contador_flexible(2,9,3)
    print('FIN DEL PROGRAMA')