def imprimir_tablero(tablero): #2
  for fila in tablero: #recorremos "tablero"
    print(" | ".join(fila)) #.join coge todos los elementos iterables (fila es el iterador) y los une por lo que sea que indiquemos, en este caso el simbolo "|". Osea, va a unir cada " " (string vacio) con un " | "
    print("-" * 9) #ademas vamos a imprimir 9 veces el simbolo "-" (pregunta: necesitamos indicar el número de veces? no basta con el iterador ya que él mismo va a pasar por todos los elementos hasta que acabe el bucle?)
    #se vería esto:
    #  |   |  
    #---------
    #  |   |  
    #---------
    #  |   |  
    #---------
def comprobar_ganador(tablero, jugador): #4 (tablero sencillo, "X" -> jugador_actual el 1er bucle es "X")
  for i in range(3): #iteramos i 3 veces
    if all(tablero[i][j] == jugador for j in range(3)) or all(tablero[j][i] == jugador for j in range(3)):
      return True
    #all() devuelve True si TODOS los elementos son True, si no devuelve False
    #en tablero[i][j] i representa fila, j representa columna
    #si coincide que 3 veces en una fila(i) == "X" o coincide que 3 veces en una columna(j) == "X" -> return True (porque se especifica que devuelva True si se supone que eso ya lo hace la funcion all()?)
  if all(tablero[i][i] == jugador for i in range(3)) or all(tablero[i][2-i] == jugador for i in range(3)):
    return True
  return False
#esta funcion es la que mas me cuesta ver, preguntar el paso a paso a sergio

def is_tablero_full(tablero): #5 tablero -> [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
  return all(all(casilla != " " for casilla in fila) for fila in tablero)
#2 all()
#el primero: all(casilla != " " for casilla in fila) -> dime si true o false que el iterador "casilla" no es igual a " ". (casilla mira los 3 elementos de una de las listas [' ', ' ', ' '])
#el segundo: all(all(casilla != " " for casilla in fila) for fila in tablero) -> dime si true o false que el primer all() es true o false por todo el tablero. (fila recorre todas las listas del tablero [' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' '])
#así pues, el primer all() se realiza 3 veces y devuelve (por ej: True, True, False) -> lo que querria decir que las dos primeras listas están full llenas, pero la 3a aún no.

def tres_en_linea(): #1
  tablero = [[" " for _ in range(3)] for _ in range(3)] #una lista dentro de otra lista
  #[" " for _ in range(3)] -> crear " " 3 veces en una lista []. [[" " for _ in range(3)] for _ in range(3)] -> crear " " 3 veces en una lista [], durante 3 veces y metido en otra lista [[]]
  #es decir, esto: [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
  jugador_actual = "X"

  print("Bienvenido al tres en línea")
  imprimir_tablero(tablero) #2
  #activamos la funcion "imprimir_tablero" con la variable "tablero" que es el tablero unidimensional que acabamos de crear: [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

  while True:
    print(f"Turno del jugador {jugador_actual}") #3
    #1er bucle: turno del jugador "X"
    fila = int(input("Fila (0,1,2): "))
    col = int(input("Columna (0,1,2): "))
    #imaginemos que 1er bucle escogemos fila=1 y col=0

    if tablero[fila][col] == " ": #si tablero[1][0] == " " (osea está vacio)
      tablero[fila][col] = jugador_actual #añadimos "X" (el valor de la variable "jugador_actual" en la fila 1, col 0)
      imprimir_tablero(tablero) #imprimimos el tablero que hemos creado en la funcion imprimir_tablero, no el tablero sencillo unidimensional

      #OJO: darse cuenta aqui que tecnicamente añadimos fichas al tablero-tablero, el sencillo, pero despues hacemos visible el tablero-imprimir_tablero, pero lo que es jugar jugamos sobre el sencillo.

      if comprobar_ganador(tablero, jugador_actual): #4
        #si comprobar_ganador es True
        print(f"El jugador {jugador_actual} ha ganado")
        #el jugador ha ganado
        break
      elif is_tablero_full(tablero): #5
        #si is_tablero_full es True
        print("Empate!")
        break
      #6
      #si no se da ni el if comprobar_ganador ni el if is_tablero_full, cambiamos el valor de jugador actual (osea cambiamos turno)
      jugador_actual = "O" if jugador_actual == "X" else "X"
    else: #7
      print("Casilla ocupada, inténtalo de nuevo")
    #si el tablero[fila][col] no era " " quiere decir que estaba ocupado, por lo tanto ni cambiamos de jugador ni hemos hecho nada, por lo que
    #volvemos al while True y lo volvemos a intentar.

if __name__ == "__main__": #comprueba si el script es importado o está siendo ejecutado en primer plano. Con esto podemos evitar que (en otros archivos python) se ejecuten funcionalidades que no deseamos (o algo así, aunque no entiendo muy bien porque lo hemos usado aquí)
  tres_en_linea() #1