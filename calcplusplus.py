#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import csv

from calcoohija import CalculadoraHija

if __name__ == "__main__":

    if len(sys.argv) != 2:
        sys.exit("You writte: 'python3 calcplusplus.py <fichero>'")

    path = sys.argv[1]
    calc = CalculadoraHija()

    with open(path, 'r') as fich:
        entrada = csv.reader(fich)
        for linea in entrada:

            operandos = linea[1:]
            try:
                operandos_int = [float(i) for i in operandos]
            except ValueError:
                sys.exit("Error: Non numerical parameters")

            if len(linea) >= 2:
                resultado = operandos_int[0]
            else:
                resultado = 0

            if linea[0] == 'suma':
                for num in operandos_int[1:]:
                    resultado = calc.suma(resultado, num)
            elif linea[0] == "resta":
                for num in operandos_int[1:]:
                    resultado = calc.resta(resultado, num)
            elif linea[0] == "multiplica":
                for num in operandos_int[1:]:
                    resultado = calc.multiplica(resultado, num)
            elif linea[0] == "divide":
                for num in operandos_int[1:]:
                    resultado = calc.divide(resultado, num)
            else:
                print("You writte: 'suma, resta, multiplica o divide'")

            print(resultado)
