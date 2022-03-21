from State import State
from queue import PriorityQueue
from queue import Queue
from queue import LifoQueue


""" SVP regarez également cette video (8-Puzzle Solver using BFS, DFS, UCS, GBF, A* Algorithms) sur youtube  il implemente similairement toutes ces méthodes"""

#Breadth-first Search  (Algorithme 1)

# BFS très utile pour trouver le plus court chemin sur un graph non ponderé

#  Sa complexité 0(V+E) il explore les plus voisins avant de s'en eloigner
# Il ya plusieurs versions qui marchent très bien

    
    
def BFS(given_state , n): # nous avons besoin de deux varibles n= nombre de noeuds dans le graphe et given_state represente le graphe non ponderé
    root = State(given_state, None, None, 0, 0)
    if root.test():
        return root.solution()
    frontier = Queue()
    frontier.put(root)
    explored = []
    
    while not(frontier.empty()):
        current_node = frontier.get()
        explored.append(current_node.state)
        
        children = current_node.expand(n)
        for child in children:
            if child.state not in explored:
                if child.test():
                    return child.solution(), len(explored)
                frontier.put(child)
    return





#Depth-first Search avec une profodeur limitée (Un peu similaire à BFS)

# Il ya plusieurs versions qui marchent très bien également
def DFS(given_state , n): 
    root = State(given_state, None, None, 0, 0)
    if root.test():
        return root.solution()
    frontier = LifoQueue()
    frontier.put(root)
    explored = []
    
    while not(frontier.empty()):
        current_node = frontier.get()
        max_depth = current_node.depth # profondeur actuelle
        explored.append(current_node.state)
        
        if max_depth == 30:
            continue #Aller à la branche suivante

        children = current_node.expand(n)
        for child in children:
            if child.state not in explored:
                if child.test():
                    return child.solution(), len(explored)
                frontier.put(child)
    return (("Couldn't find solution in the limited depth."), len(explored))
        
    
    
def Greedy(given_state , n):
    frontier = PriorityQueue()
    explored = []
    counter = 0
    root = State(given_state, None, None, 0, 0)
    #root.evaluation()
    evaluation = root.Manhattan_Distance(n) #we can use Misplaced_Tiles() instead.
    frontier.put((evaluation[0], counter, root)) #based on greedy evaluation

    while not frontier.empty():
        current_node = frontier.get()
        current_node = current_node[2]
        explored.append(current_node.state)
        
        if current_node.test():
            return current_node.solution(), len(explored)

        children = current_node.expand(n)
        for child in children:
            if child.state not in explored:
                counter += 1
                evaluation = child.Manhattan_Distance(n) #nous pouvons également utiliser Misplaced_Tiles() plutôt.
                frontier.put((evaluation[0], counter, child)) #basé sur l'evaluation greedy
    return


def AStar_search(given_state , n):
    frontier = PriorityQueue()
    explored = []
    counter = 0
    root = State(given_state, None, None, 0, 0)
    evaluation = root.Manhattan_Distance(n) #nous pouvons également utiliser Misplaced_Tiles() plutôt.
    frontier.put((evaluation[1], counter, root)) # basé sur l'evaluation A* 

    while not frontier.empty():
        current_node = frontier.get()
        current_node = current_node[2]
        explored.append(current_node.state)
        
        if current_node.test():
            return current_node.solution(), len(explored)

        children = current_node.expand(n)
        for child in children:
            if child.state not in explored:
                counter += 1
                evaluation = child.Manhattan_Distance(n) # on peut également utiliser Misplaced_Tiles().
                frontier.put((evaluation[1], counter, child)) #basé sur A* evaluation
    return
