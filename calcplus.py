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
            
            print(linea)
            #print(operandos) lo uso o uso lineas?
            #Lo que decia sergio de hacer el for fuera
            
            resultado = int(linea[1])
            
            if linea[0] == 'suma':
                for num in linea[2:]:
                    resultado = calc.suma(resultado, int(num))
            elif linea[0] == "resta":
                for num in linea[2:]:
                    resultado = calc.resta(resultado, int(num))
            elif linea[0] == "multiplica":
                for num in linea[2:]:
                    resultado = calc.multiplica(resultado, int(num))
            elif linea[0] == "divide":
                for num in linea[2:]:
                    resultado = calc.divide(resultado, int(num))
            else:
                print('suma, resta, multiplica o divide')
                      
            print(resultado)
            
