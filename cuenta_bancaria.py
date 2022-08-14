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
if __name__ == '__main__':
    cuenta1 = CuentaBancaria(0.02,5000)
    cuenta2 = CuentaBancaria(0.03,6000)
    cuenta1.deposito(4000).deposito(3000).deposito(1000).generar_interes().mostrar_info_cuenta()
    cuenta2.deposito(5000).deposito(5000).retiro(3000).retiro(6000).retiro(1000).retiro(2000).generar_interes().mostrar_info_cuenta()
    cuenta1.balance_total()