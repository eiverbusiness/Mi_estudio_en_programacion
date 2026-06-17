import os
os.system('cls')


class Cuentabancaria:


    def __init__(self, saldo):
        self.saldo_inicial = saldo

    def depositar(self, monto):
        self.saldo_inicial += monto
        print(f"Deposito exitoso {monto}. su saldo es {self.saldo_inicial}")
    
    def retirar(self, monto):
        if monto <= self.saldo_inicial:
            self.saldo_inicial -= monto
            print(f"retiro exitoso de {monto}, saldo actual : {self.saldo_inicial}")
        else:
            print(f"Retiro denegado {monto}, Saldo insuficiente! {self.saldo_inicial}")

cuenta = Cuentabancaria(1000)

cuenta.depositar(100)
cuenta.retirar(150)
cuenta.retirar(1000)