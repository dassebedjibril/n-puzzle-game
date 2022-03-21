from Search_Algorithms import BFS, DFS, Greedy, AStar_search

#Etat initial 
n = int(input("Entrer la valeur de n\n"))
print("Entrez votre" ,n,"*",n, "puzzle carré")
root = []
for i in range(0,n*n):
    p = int(input())
    root.append(p)

print("L'etat donné est:", root)



#compter le nombre d'inversions       
def inv_num(puzzle):
    inv = 0
    for i in range(len(puzzle)-1):
        for j in range(i+1 , len(puzzle)):
            if (( puzzle[i] > puzzle[j]) and puzzle[i] and puzzle[j]):
                inv += 1
    return inv

def solvable(puzzle): #vérifier si le puzzle de l'état initial est résolvable : le nombre d'inversions doit être pair.
    inv_counter = inv_num(puzzle)
    if (inv_counter %2 ==0):
        return True
    return False


#1,8,2,0,4,3,7,6,5 resolvable
#2,1,3,4,5,6,7,8,0 pas resolvable

from time import time

if solvable(root):
    print("Possible de resoudre, Svp patientez... \n")
    
    time1 = time()
    BFS_solution = BFS(root, n)
    BFS_time = time() - time1
    print('La Solution pour BFS est:', BFS_solution[0])
    print('Le nombre de nœuds explorés est ', BFS_solution[1])    
    print('BFS Time:', BFS_time , "\n")
          
    time2 = time()
    DFS_solution = DFS(root, n)
    DFS_time = time() - time2
    print('La Solution pour DFS est:', DFS_solution[0])
    print('Le nombre de nœuds explorés est ', DFS_solution[1])
    print('DFS Time:', DFS_time, "\n")  
    
    time3 = time()
    Greedy_solution = Greedy(root, n)
    Greedy_time = time() - time3
    print('La Solution pour Greedy est:', Greedy_solution[0])
    print('Le nombre de nœuds explorés est ', Greedy_solution[1])   
    print('Greedy Time:', Greedy_time , "\n")
    
    time4 = time()
    AStar_solution = AStar_search(root, n)
    AStar_time = time() - time4
    print('La Solution pour A* est:', AStar_solution[0])
    print('Le nombre de nœuds explorés est ', AStar_solution[1])   
    print('A* Time:', AStar_time)
    
    
else:
    print("Impossible de resoudre")



     