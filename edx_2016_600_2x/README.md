## Welcome by John Guttag:
- you will struggle less with the actual coding and maybe more with understanding the concepts that you are trying to implement
- the focus is more on the problem to be solved than on the actual programming of the solution
- computation in a more general way, problems in a more general way
- begin to learn about making productive use of data
- statistical thinking
- computational models: using computation to help understand the world in which we live, experimental devices that help us understand something that has happened or to predict the future
- physical labs are supplemented by virtual labs
- what kind of experimental devices are there?
- optimization models, statistical models, simulation models
- mostly in this course, we will look at models that involve uncertainty

## Lecture 1

### 0/1 Knapsack Problem
- optimization model: an objective function that is to be maximized or minimized, a set of constraints that must be honored
- solving optimization problems is computationally challenging
- greedy algorithm is often a practical approach to finding a good approximate solution
- two variants to knapsack Problem: 0/1 knapsack and continuous or fractional knapsack problem
- stealing picasso painting = either take the whole thing or none of it
- each item is represented by a pair `<value, weight>`
- brute force algorithm: enumerate all possible combinations of items, this is called the **power set = all subsets of the set of subjects**
- power set is big: 2^n possible different values can V have
- 0/1 knapsack problem is inherently exponential

### Greedy Algorithm
- 0/1 knapsack computationally intractable
- start NOT with a greedy algorithm, but a data abstraction, and helper function, because modularity is a very important aspect of good programs
- lambda is used to create anonymous functions
- lambda is an expression, the value of the expression is a function
- identity funciton: `f1 = lambda x: x`
- `f3 = lambda x,y: "factor" if (x%y == 0) else "not factor"`
- sequence of locally "optimal" choices don't always yield a globally optimal solution
- like climbing uphill with greedy algorithm to always go up, it will find local optimum
- greedy algorithm is easy to implement, computationally efficient, but does not always yield the best solution, and we do not even know how good the approximation is


## Lecture 2

### Brute-force Algorithms
- Brute Force Algorithm (enumerate all possible combinations of items, and remove all of the combinations whose total units exceeds the allowed weight)
- Implement Brute Force with Search Tree
- Because each edge of this tree represents a decision to take or not take an item, such trees are called **decision trees**, or more often **search trees**
- Left-first, depth-first enumeration
- Computational complexity: time based on the number of nodes generated, number of levels is number of items to choose from
- **if there are n items the number of nodes is: Sum 2^0 + 2^1 + 2^2 + 2^3 ...**

### Dynamic Programming
- Dynamic Programming is just a name. (Richard Bellman)
- **Dynamic Programming is a name that is intentionally deceptive**, it was chosen because Richard Bellman wanted to hide the maths from US Air Force
```
def fib(n):
    if n<=1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
```
the complexity is roughly O(fib**n), *growth is proportional to the growth in the value of the result*
- **Memorization** create a table to record value
- Dynamic programming can work for two cases
- **1. Optimal substructure: a globally optimal solution can be found by combining optimal solutions to local subproblems**
- **2. Overlapping subproblems: finding an optimal solution involves solving the same problem multiple times**
- For 0/1 Knapsack problem, if the items are all different, then each node is solving a different problem. No two nodes have the same contents of the knapsack or the same two items to choose from
- Search Tree: Each Node = items in knapsack, remaining items, current value, remaining weight
- Node 0: `{}, [a,b,c,d], 0, 5`, Node 1: `{a}, [b,c,d], 6, 2` ...
- **what problem is solved at each node? Given remaining weight, maximize value by choosing among remaining items**, while items in knapsack or current value does not matter!
- Computational complexity can be a very subtle notion, the running time of fastMaxVal is governed by the number of **distinct pairs to consider**
- **pseudo polynomial algorithm, most of the time runs in polynomial time, but in worse case, when there are no overlapping subproblems, it reverts to exponential time**

## Summary of Lec1&2
- Many problems of practical importance can be formulated as **optimization problems**
- Given a problem can you think of it as defining an **objective function that has to be minimized or maximized, subject to some set of constraints**?
- **First try with Greedy algorithms** often provide adequate (though not necessarily optimal) solutions (optimized locally rather than globally)
- **if cannot solve with greedy algorithms, you are stuck with** Finding an optimal solution is **exponentially hard**
- but dynamic programming often yields good performance for a subclass of optimization problems -- those with optimal substructure and overlapping subproblems, and solutions always correct and fast under the right circumstances

## Lecture 3

### Graph
- Computational models: programs that help us understand the world and solve practical problems
- Knapsack: map the informal problem of choosing what to eat into an optimization problem and how we can design a program to solve it
- Modeling the knapsak problem is relatively easy! Because we **did not have to capture any relationship among the items**
- **Graph = set of nodes(vertices) + set of edges(arcs) each consisting of a pair of nodes**
- undirected graph = graph
- directed graph (di-graph) with source and destination nodes
- unweighted or weighted edges
- **Graphs are useful to capture relationships among entities, almost any kind of relationship can be modeled by a graph**
- **TREES are an important special case of a GRAPH**
- **TREE** is a directed graph in which each pair of nodes is connected by a single path
- We often speak of interconnected entities or relationships as forming a network
- computer networks, transportation networks, financial networks, sewer networks, political networks, criminal networks, social networks etc
- First use of graph theory: Leonhard Euler 1735
- graph models **abstracts away irrelevant details like size of land mass, length of bridges**
- each node except the 1st and last must have an even number of edges
- **Dense (there are a lot of edges relative to the number of nodes)** Digraphs are commonly represented as **Adjacency matrix: rows = source nodes, columns = destination nodes**
- **Simpler: Adjacency List**: associate with each node a list of destination nodes
- Why is Graph a subclass of DiGraph?
- **Substitution Rule**: if client code works correctly using an instance of the supertype, it should also work correctly when an instance of the subtype is substituted for the instance of the supertype **(any program that works with a digraph will also work with a graph!)**
- Classic Graph Optimization Problem: *Shorest path (shortest sequence of edges)*,*Shortest weighted path (minimize sum of weights of the edges in the path)
- the presence of cycles or the possible presence of cycles complicates solving the shortest path problem
- We didnt have to worry about cycles when we looked at **search tree**, because **trees dont have cycles**

### Depth-First Search (DFS)
- similar to the left-first, depth-first method of enumerating a search tree
- think of it as a way of **enumerating all paths from starting node to the ending node, and once we have got them all, we pick one of the shortest**
- but graph may have **cycles**, so we must keep track of what nodes we have visited!
- DFS begins by **choosing one child of the start node, it then chooses one child of that node, and so on... going deeper and deeper, until it either reaches the goal node or a node with no children**
- DFS's **backtracking plays an important role**

### Breadth-First Search (BFS)
- BFS code is abit more complicated than DFS, because it **is exploring many paths in paralle, not one at a time**
- BFS only finds one solution, as soon as it finds a solution, it returns it
- **Explore all path with n hops before exploring any path with more than n hops**
- BFS explores the path **in length order**, the first path it finds is **a** shortest path, there may be another path that is equally short, but it will not be shorter
- **When we want to do a weighted shortest path, ie minimize the sum of weights of the edges, not the n hops or number of edges, DFS can be easily modified to do this, but BFS cannot**
- BFS cannot easily find weighted shortest path, since shortest **weighted path** may have more than the minimum number of hops

### Graph summary
- graphs are COOL
- graphs are often the best way to create a model of many things, it capture **relationships among objects**
- many important problems can be posed as graph optimization problems we already know how to solve, like DFS and BFS
- A clique is an unweighted graph where each node connects to all other nodes.
- After knowing our source and destination, we must travel through 2 additional nodes without touching any node twice. For the first node, we have (n-2) choices, and for the second, we have (n-3) choices
- BFS begins by checking all the paths of length 1. In its worst case, it must check the paths to every node from the source to find the destination. This is at most (n-1) checks.
- Shortest Path DFS must always explore every path from the source to the destination to ensure that it has found the shortest path. Once BFS has found a path, it knows that it is the shortest, and does not have to explore any other paths.
- Weighted un-directed graph, you dont weight two directions of an edge differently
- Dijkstra's algorithm is a general method to find the shortest distances from a node to all other nodes in a graph