class Underscore:
    def __init__(self):
        self.resultado = 0
    
    def map(self,iterable,callback):
        result = []
        for i in iterable:
            result.append(callback(i))
        self.resultado = result
        return self
    
    def find(self,iterable,callback):
        for i in iterable:
            if callback(i) == True:
                self.resultado = i
                break
        return self
    
    def filter(self,iterable,callback):
        result = []
        for i in iterable:
            if callback(i) == True:
                result.append(i)
        self.resultado = result
        return self
    
    def reject(self,iterable,callback):
        result = []
        for i in iterable:
            if callback(i) == False:
                result.append(i)
        self.resultado = result
        return self
    
clase = Underscore()
test1 = clase.map([1,2,3,4,5,6],lambda x: x * x)
print(test1.resultado)