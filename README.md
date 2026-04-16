
Simulador Gato y Ratón (Minimax)
Objetivo: Simular una persecución en un tablero de 5x5 donde el Gato busca atrapar al Ratón y este busca escapar.
¿Qué hace el programa?
1. Representación: Crea una matriz de 5x5 (tablero) que se dibuja en consola usando bucles anidados.
2. IA (Minimax): Utiliza el algoritmo Minimax para predecir movimientos.
• Gato: Actúa como "Minimizador" (quiere distancia 0).
• Ratón: Actúa como "Maximizador" (quiere la distancia máxima).
3. Heurística: Usa la Distancia Manhattan (|x_1 - x_2| + |y_1 - y_2|) para calcular qué tan cerca están los agentes, ya que solo se mueven en horizontal y vertical.
4. Finalización: El juego termina si el Gato alcanza la posición del Ratón (captura) o si se agotan los turnos permitidos (supervivencia).
Resumen Técnico (Para tu defensa):
"Es una implementación de búsqueda adversarial en un entorno discreto, utilizando recursividad para la toma de decisiones y una matriz bidimensional para la interfaz de usuario."
