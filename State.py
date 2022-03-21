class State:
    goal = [1, 2, 3, 4, 5, 6, 7, 8, 0] 
    #ceci devrait être modifié manuellement en fonction de n 
    #EX: ca serait [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0] si n is 4.
    
    greedy_evaluation = None
    AStar_evaluation = None
    heuristic = None
    def __init__(self, state, parent, direction, depth, cost):
        self.state = state
        self.parent = parent
        self.direction = direction
        self.depth = depth

        if parent:
            self.cost = parent.cost + cost

        else:
            self.cost = cost

            
            
    def test(self): #vérifier si l'état donné est le but visé ou état final
        if self.state == self.goal:
            return True
        return False
        
    #fonction heuristique basée sur la distance de Manhattan
    def Manhattan_Distance(self ,n): 
        self.heuristic = 0
        for i in range(1 , n*n):
            distance = abs(self.state.index(i) - self.goal.index(i))
            
            #distance de manhattan entre l'état actuel et l'état du but visé
            self.heuristic = self.heuristic + distance/n + distance%n

        self.greedy_evaluation = self.heuristic    
        self.AStar_evaluation = self.heuristic + self.cost
        
        return( self.greedy_evaluation, self.AStar_evaluation)


    #fonction heuristique basée sur le nombre de tuiles (ou carreaux) mal placées
    def Misplaced_Tiles(self,n): 
        counter = 0;
        self.heuristic = 0
        for i in range(n*n):
            for j in range(n*n):
                if (self.state[i] != self.goal[j]):
                    counter += 1
                self.heuristic = self.heuristic + counter

        self.greedy_evaluation = self.heuristic    
        self.AStar_evaluation = self.heuristic + self.cost

        return( self.greedy_evaluation, self.AStar_evaluation)                
                    


    @staticmethod
    
    #ceci devrait supprimer les mouvements illégaux pour un état donné
    def available_moves(x,n): 
        moves = ['Gauche', 'Droite', 'Haut', 'Bas']
        if x % n == 0:
            moves.remove('Gauche')
        if x % n == n-1:
            moves.remove('Droite')
        if x - n < 0:
            moves.remove('Haut')
        if x + n > n*n - 1:
            moves.remove('Bas')

        return moves

    #produit des enfants d'un état donné
    def expand(self , n): 
        x = self.state.index(0)
        moves = self.available_moves(x,n)
        
        children = []
        for direction in moves:
            temp = self.state.copy()
            if direction == 'Gauche':
                temp[x], temp[x - 1] = temp[x - 1], temp[x]
            elif direction == 'Droite':
                temp[x], temp[x + 1] = temp[x + 1], temp[x]
            elif direction == 'Haut':
                temp[x], temp[x - n] = temp[x - n], temp[x]
            elif direction == 'Bas':
                temp[x], temp[x + n] = temp[x + n], temp[x]
        
        
            children.append(State(temp, self, direction, self.depth + 1, 1)) #la profondeur doit être modifiée au fur et à mesure que les enfants se prod
        return children

    
   #obtient l'état donné et renvoie sa direction + la direction du parent jusqu'à ce qu'il n'y ait plus de parent
    def solution(self):
        solution = []
        solution.append(self.direction)
        path = self
        while path.parent != None:
            path = path.parent
            solution.append(path.direction)
        solution = solution[:-1]
        solution.reverse()
        return solution
         