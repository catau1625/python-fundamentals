class Usuario:
    def __init__(self,nombre,balance):
        self.nombre = nombre
        self.balance = balance
        
    def retiro(self,amount):
        self.balance = self.balance - amount
        return self
    
    def hacer_deposito(self,amount):
        self.balance = self.balance + amount
        return self
        
    def mostrar_balance_usuario(self):
        print(f'Usuario: {self.nombre}, Balance: ${self.balance}')
        return self
        
    def transferir_dinero(self,otro_user,amount):
        self.balance = self.balance - amount
        otro_user.balance = otro_user.balance + amount
        return self
        
if __name__ == '__main__':
    user1 = Usuario('Cata',5000)
    user2 = Usuario('Pia',500)
    user3 = Usuario('Italo',8000)
    # user1 3 depositos y 1 giro
    user1.hacer_deposito(4000).hacer_deposito(2000).hacer_deposito(2000).retiro(7000).transferir_dinero(user3,4000).mostrar_balance_usuario()
    user2.hacer_deposito(300).hacer_deposito(600).retiro(200).retiro(100).mostrar_balance_usuario()
    user3.hacer_deposito(3000).retiro(2000).retiro(2000).retiro(4000).mostrar_balance_usuario()