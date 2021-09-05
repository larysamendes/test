import unittest

from unittest import main , TestCase


class Conta():

    def __init__ (self,numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.op = []
    
    def Saque(self ,valor ):
        if valor <= self.saldo + self.limite:
            self.saldo = self.saldo - valor
            self.op.append(["saque:", valor])
    

    def deposito(self, valor):
        self.valor = valor
        self.saldo = self.saldo + self.valor
        self.op.append(["Deposito:", self.valor])
    
    def transferencia(self, conta, valor):
        self.Saque(valor)
        conta.deposito(valor)
        self.op.append(['Transferencia: ', valor])


    def entrato(self):
        return self.saldo

class BancoTestSquare(unittest.TestCase):

    def setUp(self):
        self.conta1 = Conta(1000, 'Maria', 100 , 200)
        self.conta2 = Conta(1001, "Joao", 50 , 100)
    
    def test_saque(self):
        
        expected = 70

        self.conta1.Saque(30)
        self.assertEqual(self.conta1.saldo, expected)


    def test_depositar(self):
        
        expected = 80
        
        self.conta2.deposito(30)
        self.assertEqual(self.conta2.saldo, expected)
    
    def test_transferencia(self):
        expected1 = 50
        expected2 = 100

        self.conta1.transferencia(self.conta2, 50)
        self.assertEqual(self.conta1.saldo, expected1)
        self.assertEqual(self.conta2.saldo, expected2)
    
    def test_estrato(self):

        expected = 50

        self.assertEqual(self.conta2.saldo, expected)


if __name__ == '__main__':
    main()