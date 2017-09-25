#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Clase(ClaseMadre):
  """Esto es un ejemplo de clase que hereda de ClaseMadre"""

  def __init__(self, valor1, valor2):
    """Esto es el método iniciliazador"""
    self.valor1 = valor1
    self.valor2 = valor2
    
  def suma(self):
    """Sumo valor1 y valor2"""
    res = self.valor1 + self.valor2

if __name__ == "__main__":
  objeto = Clase("pepe", "48544682K")   # Creo un objeto de la clase Clase
                                        # y le paso el valor pepe para su
                                        # atributo en la inicialización
                                        
                                        #Le paso valor1 y valor2
  
  objeto2 = Clase("maria", "4873736976L")
  objeto2.suma()
                         
                         
                         
                         
                         
                         
#instanciar es pasar de algo abstracto a algo concreto
