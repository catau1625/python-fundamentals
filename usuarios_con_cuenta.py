class CuentaBancaria:
    cuentas = []
    def __init__(self,interes_mensual,balance = 0):
        self.interes_mensual = interes_mensual
        self.balance = balance
        CuentaBancaria.cuentas.append(self)
        
    def deposito(self,amount):
        self.balance = self.balance + amount
        return self
    
    def retiro(self,amount):
        if CuentaBancaria.puede_retirar(self.balance,amount):
            self.balance = self.balance - amount
        else:
            print('Fondos insuficientes')
        return self
    
    def mostrar_info_cuenta(self):
        print(f'Balance: {self.balance}')
        return self
        
    def generar_interes(self):
        self.balance = self.balance * (1 + self.interes_mensual)
        return self
        
    @staticmethod
    def puede_retirar(balance, amount):
        if (balance - amount) < 0:
            return False
        else:
            return True
        
    @classmethod
    def balance_total(cls):
        suma = 0
        for i in cls.cuentas:
            print(f'Cuenta {i}, Balance: {i.balance}')
            suma = suma + i.balance
        print(f'Balance bancario: {suma}')
        return suma
    
class Usuario:
    def __init__(self,nombre,balance = 0):
        self.nombre = nombre
        self.cuenta = CuentaBancaria(0.02,balance)
        
    def retiro(self,amount):
        self.cuenta.retiro = self.cuenta.balance - amount
        return self
    
    def hacer_deposito(self,amount):
        self.cuenta.deposito = self.cuenta.balance + amount
        return self
        
    def mostrar_balance_usuario(self):
        print(f'Usuario: {self.nombre}, Balance: ${self.cuenta.balance}')
        return self
        
    def transferir_dinero(self,otro_user,amount):
        self.cuenta.balance = self.cuenta.balance - amount
        otro_user.cuenta.balance = otro_user.cuenta.balance + amount
        return self
    
if __name__ == '__main__':
    user1 = Usuario('Alondra',5000)
    user1.mostrar_balance_usuario()
        