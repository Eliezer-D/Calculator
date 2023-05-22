#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math

class Calculator:
    def __init__(self):
        self.operations = {
            '+': self.addition,
            '-': self.subtraction,
            '*': self.multiplication,
            '/': self.division
        }

    def add_operation(self, symbol, function):
        self.operations[symbol] = function

    def calculate(self, num1, symbol, num2):
        if symbol not in self.operations:
            print("Opération invalide.")
            return
#Code d'instance à ecrire
        if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
            print("Les valeurs doivent être des nombres.")
            return

        try:
            result = self.operations[symbol](num1, num2)
            print("Résultat :", result)
        except Exception as e:
            print("Une erreur s'est produite :", str(e))

    def addition(self, num1, num2):
        return num1 + num2

    def subtraction(self, num1, num2):
        return num1 - num2

    def multiplication(self, num1, num2):
        return num1 * num2

    def division(self, num1, num2):
        if num2 == 0:
            raise ZeroDivisionError("La division par zéro est impossible.")
        return num1 / num2

    def exponentiation(self, num1, num2):
        return num1 ** num2

    def square_root(self, num):
        return math.sqrt(num)

    def logarithm(self, num):
        return math.log(num)


# Programme principal
calculator = Calculator()

# Ajout des opérations mathématiques avancées
calculator.add_operation('^', calculator.exponentiation)
calculator.add_operation('sqrt', calculator.square_root)
calculator.add_operation('log', calculator.logarithm)

# Boucle de calcul
while True:
    num1 = input("Entrez le premier nombre (ou 'q' pour quitter) : ")
    if num1 == 'q':
        break

    operation = input("Entrez l'opération : ")
    num2 = input("Entrez le deuxième nombre : ")

    if num2 == 'q':
        break

    try:
        num1 = float(num1)
        num2 = float(num2)
        calculator.calculate(num1, operation, num2)
    except ValueError:
        print("Les valeurs doivent être des nombres.")

print("Fin du programme.")


# In[ ]:




