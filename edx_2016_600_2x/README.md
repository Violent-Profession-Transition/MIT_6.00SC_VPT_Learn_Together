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
- Brute Force Algorithm (enumerate all possible combinations of items, and remove all of the combinations whose total units exceeds the allowed weight)
- Implement Brute Force with Search Tree
- Because each edge of this tree represents a decision to take or not take an item, such trees are called **decision trees**, or more often **search trees**
- Left-first, depth-first enumeration
- Computational complexity: time based on the number of nodes generated, number of levels is number of items to choose from
- **if there are n items the number of nodes is: Sum 2^0 + 2^1 + 2^2 + 2^3 ...**
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