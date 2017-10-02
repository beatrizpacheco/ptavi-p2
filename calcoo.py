#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


class Calculadora():

    def suma(self, valor1, valor2):
        """Sumo valor1 y valor2"""
        return valor1 + valor2

    def resta(self, valor1, valor2):
        """Sumo valor1 y valor2"""
        return valor1 - valor2

if __name__ == "__main__":

    if len(sys.argv) != 4:
        sys.exit('Úsalo así: python3 calcoo.py operando1 operador operando2')

    operador = sys.argv[2]
    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")

    calc = Calculadora()

    if operador == 'suma':
        print(calc.suma(operando1, operando2))
    elif operador == 'resta':
        print(calc.resta(operando1, operando2))
    else:
        print('Usa: suma, resta')

# instanciar es pasar de algo abstracto a algo concreto
