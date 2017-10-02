#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

from calcoohija import CalculadoraHija
    

if __name__ == "__main__":

    if len(sys.argv) != 2:
        sys.exit('Úsalo así: python3 calcplus.py <fichero>')

    path = sys.argv[1]
    calc = CalculadoraHija()
    
    with open(path, 'r') as fich:
    
        for cadena in fich:
        
            linea = cadena[:-1].split(',')#El cadena[:-1] es para quitar el \n
                   
            print(linea)
            operandos = linea[1:]
            try:
                operandos_int = [int(i) for i in operandos]
            except ValueError:
                sys.exit("Error: Non numerical parameters")
            #print(operandos) lo uso o uso lineas?
            #No sé si hacer el for fuera o dentro
            
            if len(linea) >= 2:
                resultado = operandos_int[0]
            else:
                resultado = 0
                print('Empty list')
            
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
                print('suma, resta, multiplica o divide')
                      
            print(resultado)
                
