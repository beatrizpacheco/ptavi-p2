#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

from calcoo import Calculadora


class CalculadoraHija(Calculadora):

    def divide(self, valor1, valor2):
        """Divide valor1 y valor2"""
        try:
            return valor1 / valor2

        except ZeroDivisionError:
            sys.exit('Division by zero is not allowed')

    def multiplica(self, valor1, valor2):
        """Multiplica valor1 y valor2"""
        return valor1 * valor2

if __name__ == "__main__":

    if len(sys.argv) != 4:
        msg = "You writte: 'python3 calcoohija.py num1 operación num2'"
        sys.exit(msg)

    operador = sys.argv[2]
    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")

    calc = CalculadoraHija()

    if operador == 'suma':
        print(calc.suma(operando1, operando2))
    elif operador == 'resta':
        print(calc.resta(operando1, operando2))
    elif operador == 'multiplica':
        print(calc.multiplica(operando1, operando2))
    elif operador == 'divide':
        print(calc.divide(operando1, operando2))
    else:
        print("You writte: 'suma, resta, multiplica, divide'")
