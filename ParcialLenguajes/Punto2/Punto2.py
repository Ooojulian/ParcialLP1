# defino el abecedario y los numeros a mano pa no enredarme
alfabeto = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
nums = "0123456789"

# mapeo de columnas para la matriz
# la col 0 es para letras y la col 1 para numeros
cols = {}
for l in alfabeto:
    cols[l] = 0
for n in nums:
    cols[n] = 1

# matriz de transiciones del automata
# filas = estado actual (0 es inicio, 1 es aceptado, 2 es error/trampa)
# columnas = lo que entra (0:letra, 1:numero, 2:cualquier otra cosa)
matriz = [
    [1, 2, 2],  # est 0: arranca con letra bien (1), sino paila al error (2)
    [1, 1, 2],  # est 1: si llegan mas letras o numeros sigue en 1
    [2, 2, 2]   # est 2: estado trampa, de aca no sale
]

def revisar_id(texto):
    estado = 0
    
    for c in texto:
        # el .get me salva de usar ifs. si mandan un simbolo raro asume la col 1
        columna = cols.get(c, 2)
        
        # salto de estado buscando directo en la matriz
        estado = matriz[estado][columna]
    # arreglo para la salida sin usar condicionales
    # el indice es el estado en el que quedo al final
    # est 0 = vacio, est 1 = bien, est 2 = error
    salida = ["NO ACEPTA", "ACEPTA", "NO ACEPTA"]
    
    return salida[estado]

# --- pruebas del punto 2 ---

print("--- las que tienen q pasar (ACEPTA) ---")
print("prueba 1 (varX):", revisar_id("varX"))
print("prueba 2 (x1):", revisar_id("x1"))
print("prueba 3 (contador):", revisar_id("contador"))

print("\n--- las que fallan (NO ACEPTA) ---")
print("prueba 4 (123numero):", revisar_id("123numero")) # arranca con numero mal
print("prueba 5 (mi-id):", revisar_id("mi-id")) # tiene guion