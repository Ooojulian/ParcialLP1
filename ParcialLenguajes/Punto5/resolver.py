# script pa correr la gramatica de antlr y sacar la serie

import sys
import math
from antlr4 import *
from MaclaurinLexer import MaclaurinLexer
from MaclaurinParser import MaclaurinParser
from MaclaurinVisitor import MaclaurinVisitor

# aca sobreescribimos el visitor que genera antlr
class MiVisitor(MaclaurinVisitor):
    def visitInicio(self, ctx):
        # saco los dos numeros que entraron en la consola
        # el (0) es el primer NUM (la x) y el (1) es el segundo (la n)
        x = float(ctx.NUM(0).getText())
        n = int(ctx.NUM(1).getText())
        
        # calculo la serie de maclaurin
        # iteramos n veces
        suma_total = 0
        for i in range(n):
            # machetazo usando math.factorial pa no reinventar la rueda
            termino = (x ** i) / math.factorial(i)
            suma_total += termino
            
        print(f"\n=> calculando e^{x} con {n} terminos...")
        print(f"=> resultado de la serie: {suma_total}")
        
        # pa comparar, imprimo el valor real de e^x a ver que tan lejos quedo
        real = math.exp(x)
        print(f"=> valor real (math.exp): {real}")
        
        return suma_total

def main():
    # pido los datos por consola cruda
    print("escribe la instruccion formato calcular(x, n)")
    print("ejemplo: calcular(2, 10)")
    entrada = input("> ")
    
    # el boleo de antlr para leer el texto
    input_stream = InputStream(entrada)
    lexer = MaclaurinLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MaclaurinParser(stream)
    
    # armo el arbol y lo visito
    tree = parser.inicio()
    visitor = MiVisitor()
    visitor.visit(tree)

if __name__ == '__main__':
    main()
