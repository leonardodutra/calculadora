class Calculadora:

    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2

    def soma(self):
        soma = self.numero1 + self.numero2
        print("A soma é: " + str(soma))

    def sub(self):
        sub = self.numero1 - self.numero2
        print("A subtração é: " + str(sub))

    def mult(self):
        mul = self.numero1 * self.numero2
        print("A multiplação é: " + str(mul))


calculadora1 = Calculadora(4, 5)

calculadora1.mult()
