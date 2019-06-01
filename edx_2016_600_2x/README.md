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
- **MemOIZation** create a table to record value
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

## Lecture 5

### Stochastic Processes
- **Casual Nondeterminism: at its most fundamental level, the behavior of the physical world cannot be predicted**
- **Predictive Nondeterminism: the world may or may not be inherently unpredictable, but our lack of knowledge does not allow us to make accurate predictions**
- However, whether the reason we cannot predict events is because they are truly unpredictable or is because we simply don't have enough information to predict them is of no practical importance. The Bohr-Einstein debate was about how to understand the lowest levels of the physical world. And honestly, except to physicists, it's not really of immediate interest to the vast majority of the world's population.
- More obviously relevant situations like horse races, spins of roulette wheels and stock market investments may be causally deterministic, but you would be very wise to treat them as non-deterministic. *Treat them as stochastic processes*
- *Deterministic, tochastic, static, dynamic, discrete, continuous models*

### Probabilities
- Pseudo-random number generators work typically by reading some unexpected value, like the number of milliseconds since Jan 1 1968, and a random.seed
- `random.seed(x)` use the same seed every time I run the program
- sample space is the **set** of all possible outcomes of that experiment, usually written as a *tree* or a *grid*
- an **event** is a subset of the sample space, it is a collection of some possible outcomes
- A standard deck of cards contains 52 cards, 13 each of four suits - diamonds, clubs, hearts, and spades. Each suit contains one of 13 cards: A (ace), 2, 3, 4, 5, 6, 7, 8, 9, 10, J (jack), Q (queen), K (king)

### Random Walks
- **Simulation models are descriptive, not prescriptvie, unlike optimization models, they *tell us what might happend, not how to make something happen!**
- Optimization models are prescriptive as they provide a prescription for reaching some goal
- So dont ever feel too confident about your simulation model. **Remember it is a model, it is not reality**
- Random walks in understanding the stock market, modeling diffusion processes
- 1827 Robert Brown
- 1900 Louis Bachelier on movement of stock prices and option prices

## Lecture 6

### Class Location, Field, and Drunk
- `Location` a place
- `Field` a collection of {Drunk: Location} in dict, a mapping of drunks to locations, allows multiple drunks
- `Drunk` not intended to be useful on its own, a base class to be inherited

### Simulating a Single Walk
- One **Walk** of `k` **steps**
- `n` such **walks**
- `class.__name__` is the class name assigned when creating the class. `Drunk.__name__` will be `"Drunk"`
- Using **`random.seed`, you create a deterministic simulation rather than a stochastic simulation**. You should never use random.seed in a real-life situation, regardless of the seed value!**
- In the ipython console, once you have initialized a program with random.seed, it is set to seed. To complete reset, you will have to **restart the kernel**
- **`random.seed` will reset the pseudo-random sequence to the same starting point**. Each seed value will correspond to a sequence of generated values for a given random number generator, if you provide the same seed twice, you get the same sequence of numbers twice
- We can plot the **distance of how far they have gone, or get the location of each walk's end**
- On average, every four steps, the ColdDrunk moves down once and up once. After the four steps, the ColdDrunk is now 0.2 steps lower than before. So on average, ColdDrunk will move down about 0.2 steps for every 4 steps he takes, PolarBearDrunk will move down about 1 step for every 4 steps


## Lecture 7

### Inferential Statistics
- Goal of Inferential Statistics: estimate some statistics about the population based on statistics about the sample
- **Key fact:** if the sample is **chosen at random**, it tends to exhibit the same properties as the population from which it is drawn
- Your belief on whether the coin is fair or not is **based on the intuition that the behavior of a sample of 100 flips is similar to the behavior of the population of all flips of your coin.**
- **Confidence in our estimates** depends on two things: **Size of the sample (100 vs 2)** and **variance**
- **As the variance grows, we need larger samples to have the same degree of confidence**
- **what is the definition of "odds"?** *the odds in favor of my team winning the game are 1 to 4 -> so we have 5 games in total, 1 of the game my team will win...* `*|****`
- **Odds are not probabilities! The odds are the ratio of something happening to something not happening (Favorable / Unfavorable)** *Odds = What you want vs What you dont want*
- The worse my team is, the odds of losing will be closer to zero, but the better my team is, the odds of winning will be up to infinity
- Odds != Odds Ratio. Odds ratio is the "ratio of odds"
- Betting odds 5/1 or 6 are expressing odds, both meaning you will get $6 for ever $1 you bet if you win
- 12/1 shows how much you will win on your bet in comparison to the amount staked, 12 = how much you will win from $1 stake, 1 = stake amount
- **American Odds: odds expression indicating return relative to 100 unit base figure. With money odds, whenever there is a minus you lay that amount to win $100, where there is a plus you win that amount for every $100 you bet**
- **Fractional Odds: historically from UK, 12 to 1, or 12/1 not including the stake or wager**
- **Decimal Odds: potential return of a bet, including the stake amount** (IMPORTANT: Decimal odds always include the stake!)
- **The MOST IMPORTANT LAW in all of statistics: Law of Large Numbers**
- **Mis-application of law of large numbers is known as gambler's fallacy** sports announcer tell you a baseball player is due for a hit because he hasnt hit any...
- **People often confuse the gambler's fallacy with regression to the mean, something that is actually correct**
- **Regression to the mean: Following an extreme random event, the next random event is likely to be less extreme** If you spin a fair roulette wheel 10 times and get 100% reds, that is an extreme event (1/1024), so it is *likely that in the next 10 spins, you will get a less extreme event* ie, fewer than 100% reds. So if you look at the average of the 20 spins, it will be closer to the expected mean of 50% reds than to the 100% in the first 10 spins
- The term regression to the mean was first used by Francis Galton 1885 for observation of children of tall parents

### Variation in Data
- Never possible to guarantee perfect accuracy through sampling unless one samples the entire population
- **The Question we need to ask is: How much confidence should we have that our estimate is close to right?**
- **How many samples do we need to look at before we can have justified confidence on our answer?**
- Our confidence in the estimate depends on: **Variability in underlying distribution**
- **Need to think about Standard Deviation in the context of the mean, not in isolation, SD = 0.2???**
- **The standard deviation in mean to talk about how much confidence we should have that a sample mean is close to the population mean: Confidence level and intervals**
- **Confidence interval and confidence level indicate the reliability of the estimate**
- `+/- 1.96*std` is the actual number of standard deviations for 95% confidence intervals, or roughly 95% of the data will be within 2 stds of the mean
- The 95% confidence interval for a normal distribution of data with a mean of 5 and a standard deviation of 2 is 5 +/- (2x1.96)
- Two key assumptions for empirical rule: 1. on average, estimation error is zero 2. the distribution of the errors in the estimates is normally distributed around the mean

### Distributions
- We define distributions using probability distribution
- Histogram is a depiction of the frequency of a distribution, how often a random variable takes on a value within a range
- Discrete vs Continuous probability distributions (discrete vs continuous random variables)
- **Continuous probability we cannot enumerate probability for each of an INFINITE set of values, we use PDF**
- **PDF = Probability Density Functions, describes the probability of a random variable lying between two values**
- Area under Curve between two x1 x2 is the probability of the variable having a value between x1 and x2
- PDF for random.random() is flat 1, because the *probability of random.random() returning a value between 0 and 1 is indeed 100%*
- Generating Normal Distributions in pylab
```
dist = [random.gauss(0,30) for i in range(10000)]
pylab.hist(dist, 30)  # for 30 bins
```
- PDF for `1.0 / (sigma * ((2 * pylab.pi)**0.5)) X pylab.e**-(((x-mu)**2) / (2 * sigma**2))` only the Area Under Curve matters, total area is 1
- use `scipy.integrate.quad` to do integration using quadrature method (f, a, b, (y,z...)), returns you a tupe (approx result, estimate of absolute error)

## Lecture 8

### Central Limit Theorem
- One the two MOST IMPORTANT theorems in statistics: **1. Law of large numbers and 2. Central Limit Theorem (CLT)**
- CLT: 1) the means of the samples in a set of samples will be approximately normally distributed
- `hatch` in matplotlib histogram is the filling of the graph, in addition to the color, we will draw different hatch marks
- `pylab.hist(weight=?)` weight can be added to scale the histogram
- In the usual histogram, the size of each bin is determined solely by the number of elements contained in that bin. Using weight, we scale the y values to the relative rather than the absolute size of each bin.
- It does not matter what the shape of the distribution of values happens to be, **if we are trying to estimate the mean of a population using sufficiently large samples, the CLT allows us to use normal distributions and confidence intervals**

### Monte Carlo Simulation
- "Monte Carlo simulation" was first coined in 1949 by Stanislaw Ulam and Nicholas Metropolis
- Ulam invented Monte Carlo method in 1946 while thinking about Solitaire game, instead of trying to estimate by pure combinatorial calculations, for mathematical physics and more generally how to change processes described by certain differential equations into an equivalent form interpretable as a succession of random operations
- **Monte Carlo simulation and randomized algorithms in general can be used to solve problems that have nothing inherently stochastic about them, ie. for which there is no uncertainty about the outcomes**
- **Generally useful technique for Monte Carlo simulation: to estimate the area of some region R. Pick an enclosing resgion, E, such that the area of E is easy to calculate and R lies completely within E, pick a set of random points that lie within E, let F be the fraction of the points that fall within R, multiply the area of E by F**
- for integration area estimation


## Lecture 12

### Machine Learning
- Most useful programs learn something
- Linear regression to model data, Newton method to learn the roots of polynomial
- **"ML is field of study that gives computers the ability to learn without being explicitly programmed" --Arthur Samuel**
- **Modern statistics meets optimization**
- Traditional programming: Data + Program = Output
- ML: Data + Output = Program, then new Data + Program = Predicted Output
- **Basic paradigm in ML**: observe a set of examples (training data), try to generalize from these examples, they provide some information about a **statistical phenomenom**, then we infer something about the **process that generated those examples**
- Old warhorses like regression and k-means clustering
- New hot technique like deep-learning
- **But ALL ML methods require: 1. Representation of the features (descriptions of our training data) 2. Distance metric for feature vectors 3. Objective function and constraints 4. Optimization method for learning the model 5. Evaluation method (to tune/choose the parameters of the learning method)**
- **Supervised Learning** (feature vector, value) pairs, the value associated with the feature vector. find a model that predicts a value for a previously unseen feature vector
- Regression predicts infinite number of possible outputs of a regression model
- Classification predicts finite set of labels
- **Unsupervised Learning** goal is to **uncover some latent structure in the set of feature vectors** (some structure that we did not previously know was there)
- Clustering define some metric about how similar one feature vector is to another, and group objects based on this metric
- Depending on what you choose as features, different structure emerges from the data
- **In reality, we can never build a set of features that fully describe the examples or provide *all* the information we need to make good predictions**
- **Feature engineering**: represent examples by feature vectors that are pertinent to the task and will facilitate generalization
- Some features surely helpful: grade on midterm, did they do the problem set etc
- Other might cause overfit: birth month...
- **Maximize ratio of useful input to irrelevant input: Signal to Noise ratio**

### k-nearest neighbor
- Commonly used distance metric: Minkowski metric
- Euclidean and Manhattan metric depends on the application
- `pylab.table()` to produce table using pylab
- The simplest classification algorithm is **nearest neighbor**, predict the label of a new example by find the nearest example in the training data
- **Advantage of KNN**: learning is just memorization of all the training data, no explicit training, no theory required, easy to explain
- **Disadvantage of KNN**: Memory intensive and almost brute force, **no model to shed light on the process that generated data**
- Another method for classification **logistic regression**
- Classification of animals, number of legs 0-4 vs cold-blooded 0-1 has a **bigger dynamic range**, so when we calculate the Euclidean distance, the number of legs gets **disproportionate weight** (because it happens to have bigger numbers)
- **Scaling/Normalization**: general approaches **1. z-scaling 2. interpolation**
```python
def zScaleFeatures(vals):
    """each feature has a mean of 0 and std of 1"""
    result = pylab.array(vals)
    mean = float(sum(result))/len(result)
    result = result - mean
    return result/stdDev(result)

def iScaleFeatures(vals):
    """min 0, max 1, linearly interpolate"""
    minVal, maxVal = min(vals), max(vals)
    fit = pylab.polyfit([minVal, maxVal], [0, 1], 1)
    return pylab.polyval(fit, vals)
```

### Clustering
- Uncover some latent structure in the data
- Partition examples into groups/clusters such that examples in a group are more similar to each other than examples in other groups
- no "right answer", answer dictated by **feature vectors**, **distance metric**, and not by a ground truth label
- **Optimization problem** objective function on minimize variability(c) and dissimilarity(C). Variability for a *single cluster*, dissimilarity for *all the clusters in the clustering*
- **Variability is not VARIANCE!**, **DONOT DIVIDE BY THE SIZE OF THE CLUSTER**, because we want the objective function to penalize big incoherent clusters more than it penalizes small incoherent clusters
- **Constrain to avoid trivial put each point in its own cluster: minimum distance between clusters and minimum number of clusters**
- **k-means clustering = exactly k non-empty clusters** (use a greedy algorithm to find an approximation to minimizing objective function)
- randomly chose k examples as initial centroids, while True: 1) create k clusters by assigning each example to closest centroid 2) compute k new centroids by averaging examples in each cluster 3) if centroids dont change break
- *Only in the very first 0th iteration do we expect the centroids to actually represent real points*
- **K-means does not always work wo well**, it depends on the random choice of initial centroids
- To avoid get stuck in local optimum, the usual solution is to run k-means multiple times to **minimize dependence on initial centroids**
```python
best = kMeans(points)
for t in range(numTrials):
    C = kMeans(points)
    if dissimilarity(C) < dissimilarity(best):
        best = C
return best
```
