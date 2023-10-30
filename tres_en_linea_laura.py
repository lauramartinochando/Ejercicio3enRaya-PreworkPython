juego = True

#falta comprobar si hay ganador

def comprobar_ganador(tablero, tablero2, jugador):

  for item in range(len(tablero)):
    winner = set(tablero[item])
    winner2 = set(tablero2[item])

    if len(winner) >= 2 or len(winner2) >=2:
      return False
    else:
      if winner == jugador or winner2 == jugador:
        return True
    return False

def tres_en_linea():
  
  contador_turnos = 0
  jugador_actual = "X"
  tablero = [["_","_","_"],["_","_","_"],["_","_","_"]]
  print(tablero)
  tablero_traspuesto = [["_","_","_"],["_","_","_"],["_","_","_"]]
  turno = True
  while turno:

    if contador_turnos == 9:
      print("Tablero lleno")
      break

    print(f"turno nº: {contador_turnos}")
    fila = int(input("Selecciona una fila (0,1,2): "))
    columna = int(input("Selecciona una columna (0,1,2): "))


    #comprobamos el turno para saber si el tablero está lleno

    #comprobamos casilla ocupada
    if tablero[fila][columna] == "_":
      contador_turnos += 1
      tablero[fila][columna] = jugador_actual
      tablero_traspuesto[columna][fila] = jugador_actual
      print(tablero)

      if comprobar_ganador(tablero, tablero_traspuesto, jugador_actual):
       print(f"El ganador es jugador: {jugador_actual}")
       break
      
      #si el jugador ha podido dejar ficha, cambiamos de jugador
      if jugador_actual == "X":
        jugador_actual = "O"
      else:
        jugador_actual = "X"

  else:
    print("Casilla ocupada, inténtalo otra vez")
      

while juego: 
  tres_en_linea()