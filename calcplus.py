#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

from calcoohija import CalculadoraHija
    

if __name__ == "__main__":

    if len(sys.argv) != 2:
        sys.exit('Úsalo así: python3 calcplus.py <fichero>')

    fich = open(sys.argv[1], 'r')
    calc = CalculadoraHija()
    
    for cadena in fich:
    
        linea = cadena[:-1].split(',')#El linea[:-1] es para quitar el \n
               
        print(linea)
        #print(operandos) lo uso o uso lineas?
        #No sé si hacer el for fuera o dentro
        
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
            
