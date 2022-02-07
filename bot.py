import json
visited = []  # Lista nodos visitados
queue = []    # Inicializar una cola
def bfs(visited, graph, node): #funcion para el BFS
  # Se agrega el nodo a la lista de visitados
  # tambien es agregado a la cola
  visited.append(node)
  queue.append(node)
  while queue:          # Crear el bucle para recorrer cada nodo
    m = queue.pop(0)    # y extrae el elemento de la cola
    print (m, end = " ")
    # Comprobar si el nodo vecino a sido visitado
    # en caso de no ser visitado agregar a las
    # listas respectivas
    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)
# Menu principal
if __name__ == "__main__":
  #Cargamos la base de conocimiento en nuestro grafo
    with open("bk/bk1.json", "r") as f:
        graph = json.load(f)
    print("Recorrido por BFS:")
    print( bfs(visited,graph, "A"))