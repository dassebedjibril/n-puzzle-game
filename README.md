# n-puzzle-game
## We will implement and compare different algorithms for this game.


The teaser game is a puzzle that was created around 1870, since then it has attracted the interest of many mathematicians for its value as a combinatorial problem. The game is composed of n*m−1 small tiles numbered starting from 1 which slide in a frame of the format n×m leaving an empty box allowing to modify the configuration of the tiles. The game consists of putting these boxes back in order from any initial configuration. The game is often known in 3×3 or 4×4 formats, hence the 8-puzzle or 15-puzzle respectively. The Rubik's Cube is considered one of the teaser's descendants. 


### Complexity

The teaser game is the biggest problem of its kind that can be solved completely (one can find all the solutions that exist for a given problem). It is simply defined but the problem is NP-hard (Reinefeld 1993). The problem is combinatorially large and requires a guided resolution in order to reach before exhausting the resources (time and memory).

The state space has size (n⋅m)!/2 which is 181,440 for the 3×3 variant. Indeed, there exists (n⋅m)! permutations of the tiles, one permutation out of two is solvable, we can evoke the parity argument which was presented in (Johnson and Storey 1879) in order to show that half of the initial configurations can never reach the goal state by defining an invariant function of tile movement which defines two equivalence classes of accessible and non-accessible states.

### The Goal 

The goal of the project is to solve a real problem using logic programming. We chose the teaser game because it is interesting as an Artificial Intelligence problem, and adapts well to logic programming.
In this project we will present this problem mathematically and propose algorithms of various resolutions, a prolog implementation of these algorithms, and finally a study of the results.

### Formulation of the problem

The problem is best represented by a related graph. We define the state space E by all the solvable configurations of the problem. 
Part of the teaser graph. We consider two adjacent states if we can go from one to the other by dragging a single neighboring tile to the empty space. The empty space has at least 2 neighboring tiles (if it is in a corner), and at most 4 (left, right, top, bottom). Ideally, we seek the shortest path to reach the goal from the initial state, which is a classic problem of finding paths in a graph.

### Algorithms

Ils existent de nombreux algorithmes pour la recherche d’un chemin dans un graphe, nous avons implémenté quelques algorithmes qui correspondent bien à notre problème et qui s’adaptent bien aux principes de la programmation logique.


#### Depth First Search (DFS)

#### Heuristic 

#### Manathan distance 

#### Greedy algorithm

#### A* Algorithm




