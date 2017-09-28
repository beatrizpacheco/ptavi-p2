#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import csv

from calcoohija import CalculadoraHija

if __name__ == "__main__":
  
   

    if len(sys.argv) != 2:
        sys.exit('Úsalo así: python3 calcplus.py <fichero>')

    fich = sys.argv[1]
    calc = CalculadoraHija()
    
    with open(fich) as csvarchivo:
        entrada = csv.reader(csvarchivo)
        for linea in entrada:
            operandos = linea[1:]
            print(linea)
            print(operandos)
            op1 = int(operandos[0])
            op2 = int(operandos[1])
            if linea[0] == 'suma':
                resultado = calc.suma(op1, op2)
            elif linea[0] == "resta":
                resultado = calc.resta(op1, op2)
            elif linea[0] == "multiplica":
                resultado = calc.multiplica(op1, op2)
            elif linea[0] == "divide":
                resultado = calc.divide(op1, op2)
            else:
                print('suma, resta, multiplica o divide')
                      
            print(resultado)
            
