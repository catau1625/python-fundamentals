class Usuario:
    def __init__(self,nombre,balance):
        self.nombre = nombre
        self.balance = balance
        
    def retiro(self,amount):
        self.balance = self.balance - amount
    
    def hacer_deposito(self,amount):
        self.balance = self.balance + amount
        
    def mostrar_balance_usuario(self):
        print(f'Usuario: {self.nombre}, Balance: ${self.balance}')
        
    def transferir_dinero(self,otro_user,amount):
        self.balance = self.balance - amount
        otro_user.balance = otro_user.balance + amount
        
if __name__ == '__main__':
    user1 = Usuario('Cata',5000)
    user2 = Usuario('Pia',500)
    user3 = Usuario('Italo',8000)
    # user1 3 depositos y 1 giro
    user1.hacer_deposito(4000)
    user1.hacer_deposito(2000)
    user1.hacer_deposito(2000)
    user1.retiro(7000)
    user1.mostrar_balance_usuario()
    # user2 2 depositos y 2 giros
    user2.hacer_deposito(300)
    user2.hacer_deposito(600)
    user2.retiro(200)
    user2.retiro(100)
    user2.mostrar_balance_usuario()
    # user3 1 deposito y 3 giros
    user3.hacer_deposito(3000)
    user3.retiro(2000)
    user3.retiro(2000)
    user3.retiro(4000)
    user3.mostrar_balance_usuario()
    # user1 transferencia a user3
    user1.transferir_dinero(user3,4000)
    user1.mostrar_balance_usuario()
    user3.mostrar_balance_usuario()