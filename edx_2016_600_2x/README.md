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
