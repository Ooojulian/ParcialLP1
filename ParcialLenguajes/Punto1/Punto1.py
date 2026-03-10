# parcial 1 lenguajes - punto 1
# julian david cristancho bustos 
# ciencias de la computacion e IA - sergio arboleda

# defino las letras minusculas y numeros a mano pa la matriz
minusculas = "abcdefghijklmnopqrstuvwxyz"
nums = "0123456789"

# armo el diccionario pa las columnas de la matriz
# 0: letras min, 1: numeros, 2: '-', 3: '>', 4: 'X', 5: espacio, 6: cualquier otra joda
cols = {}
for l in minusculas: cols[l] = 0
for n in nums: cols[n] = 1
cols['-'] = 2
cols['>'] = 3
cols['X'] = 4
cols[' '] = 5

# matriz gigante de transiciones (10 estados, 7 columnas)
# est 9 es el de error/trampa (paila)
# est 7 y 8 son los de aceptacion (cuando termina bien)
matriz = [
    # min  num  -  >  X esp otro
    [  1,   9,  9, 9, 9,  9,  9 ], # est 0: inicio (espera minuscula)
    [  1,   9,  2, 9, 9,  4,  9 ], # est 1: despues de letra origen (espera -, espacio o mas letras)
    [  9,   9,  9, 3, 9,  9,  9 ], # est 2: leyo el guion (espera >)
    [  7,   9,  9, 9, 9,  9,  9 ], # est 3: flecha lista (espera letra destino)
    [  9,   9,  9, 9, 5,  9,  9 ], # est 4: leyo el primer espacio (espera X mayuscula)
    [  9,   9,  9, 9, 9,  6,  9 ], # est 5: leyo la X (espera el segundo espacio)
    [  7,   9,  9, 9, 9,  9,  9 ], # est 6: leyo el segundo espacio (espera letra destino)
    [  7,   8,  9, 9, 9,  9,  9 ], # est 7: letras destino (ACEPTA) o salta a numero
    [  9,   8,  9, 9, 9,  9,  9 ], # est 8: numeros destino (ACEPTA)
    [  9,   9,  9, 9, 9,  9,  9 ]  # est 9: trampa, murio ahi
]

def validar_movimiento(texto):
    estado = 0
    
    for c in texto:
        # si mandan una mayuscula rara o un simbolo que no esta, asume la col 6
        columna = cols.get(c, 6)
        
        # salto de estado sin usar ni un solo if
        estado = matriz[estado][columna]
        
    # arreglo de 10 posiciones pa las respuestas
    # solo la pos 7 y 8 dicen ACEPTA, el resto paila
    respuestas = ["NO ACEPTA"] * 10
    respuestas[7] = "ACEPTA"
    respuestas[8] = "ACEPTA"
    
    return respuestas[estado]


# --- pruebas del profe ---

print("--- ACEPTADAS ---")
print("p->k4 :", validar_movimiento("p->k4"))
print("kbp X qn :", validar_movimiento("kbp X qn"))
print("q->h :", validar_movimiento("q->h"))

print("\n--- RECHAZADAS ---")
print("P->k4 :", validar_movimiento("P->k4")) # mayuscula al inicio mal
print("p-k4 :", validar_movimiento("p-k4"))   # falta la >
print("p Xk4 :", validar_movimiento("p Xk4")) # falta espacio despues de X