import random

# --- 1. CONFIGURACIÓN Y TABLERO ---
FILAS, COLUMNAS = 5, 5
MAX_MOVIMIENTOS = 5  # El ratón gana si sobrevive a 5 movimientos

def medir_distancia(p1, p2):
    """Distancia Manhattan: suma de diferencias de filas y columnas"""
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

# --- 2. EL ALGORITMO MINIMAX (NIVEL EXPERTO) ---
def minimax(pos_gato, pos_raton, profundidad, es_maximizador):
    """
    Simulación de predicción:
    - El Ratón quiere MAXIMIZAR la distancia.
    - El Gato quiere MINIMIZAR la distancia.
    """
    # Caso base: si llegamos al final de la profundidad o el gato atrapa al ratón
    if profundidad == 0 or pos_gato == pos_raton:
        return medir_distancia(pos_gato, pos_raton)

    f_g, c_g = pos_gato
    f_r, c_r = pos_raton
    opciones = [[-1, 0], [1, 0], [0, -1], [0, 1]] # Arriba, Abajo, Izq, Der

    if es_maximizador: # Turno simulado del RATÓN (Maximiza distancia)
        mejor_valor = -float('inf')
        for mov in opciones:
            nueva_pos = [f_r + mov[0], c_r + mov[1]]
            if 0 <= nueva_pos[0] < FILAS and 0 <= nueva_pos[1] < COLUMNAS:
                valor = minimax(pos_gato, nueva_pos, profundidad - 1, False)
                mejor_valor = max(mejor_valor, valor)
        return mejor_valor
    else: # Turno simulado del GATO (Minimiza distancia)
        mejor_valor = float('inf')
        for mov in opciones:
            nueva_pos = [f_g + mov[0], c_g + mov[1]]
            if 0 <= nueva_pos[0] < FILAS and 0 <= nueva_pos[1] < COLUMNAS:
                valor = minimax(nueva_pos, pos_raton, profundidad - 1, True)
                mejor_valor = min(mejor_valor, valor)
        return mejor_valor

def obtener_mejor_movimiento(pos_yo, pos_rival, profundidad, es_raton):
    """Busca cuál de los 4 movimientos reales devuelve el mejor valor de Minimax"""
    f, c = pos_yo
    movimientos = [[f-1, c], [f+1, c], [f, c-1], [f, c+1]]
    mejor_mov = pos_yo
    
    if es_raton:
        mejor_val = -float('inf')
        for m in movimientos:
            if 0 <= m[0] < FILAS and 0 <= m[1] < COLUMNAS:
                # El ratón evalúa su movimiento enviando 'False' porque el siguiente turno simulado es del gato
                val = minimax(pos_rival, m, profundidad, False)
                if val > mejor_val:
                    mejor_val = val
                    mejor_mov = m
    else:
        mejor_val = float('inf')
        for m in movimientos:
            if 0 <= m[0] < FILAS and 0 <= m[1] < COLUMNAS:
                # El gato evalúa su movimiento enviando 'True' porque el siguiente turno simulado es del ratón
                val = minimax(m, pos_rival, profundidad, True)
                if val < mejor_val:
                    mejor_val = val
                    mejor_mov = m
    return mejor_mov

# --- 3. EJECUCIÓN DEL DUELO IA VS IA ---

# Posiciones iniciales aleatorias
gato = [random.randint(0, 4), random.randint(0, 4)]
raton = [random.randint(0, 4), random.randint(0, 4)]

# Evitar que empiecen en la misma casilla
while gato == raton:
    raton = [random.randint(0, 4), random.randint(0, 4)]

movimientos_realizados = 0
profundidad_actual = 1 # Empezamos con profundidad baja

print("--- INICIO DEL DUELO IA vs IA ---")
print(f"Posicion inicial Gato: {gato}")
print(f"Posicion inicial Raton: {raton}")

while movimientos_realizados < MAX_MOVIMIENTOS:
    movimientos_realizados += 1
    profundidad_actual += 1 # La profundidad aumenta en cada turno
    
    print(f"\n>>> MOVIMIENTO {movimientos_realizados} (Profundidad de calculo: {profundidad_actual})")

    # Decidir quién mueve primero este turno al azar
    orden = ["gato", "raton"]
    random.shuffle(orden)

    for jugador in orden:
        if jugador == "gato":
            gato = obtener_mejor_movimiento(gato, raton, profundidad_actual, False)
            print(f"Gato se mueve a: {gato}")
        else:
            raton = obtener_mejor_movimiento(raton, gato, profundidad_actual, True)
            print(f"Raton se mueve a: {raton}")

        # Dibujar tablero simple
        for f in range(FILAS):
            for c in range(COLUMNAS):
                if [f, c] == gato: print(" G ", end="")
                elif [f, c] == raton: print(" R ", end="")
                else: print(" . ", end="")
            print()

        # Verificar si el gato atrapó al ratón
        if gato == raton:
            print("\nRESULTADO: El Gato ha ganado por captura.")
            exit()

# Si sale del bucle es porque el ratón sobrevivió
print("\nRESULTADO: El Raton ha ganado por supervivencia.")