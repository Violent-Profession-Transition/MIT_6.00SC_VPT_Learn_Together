# MIT_6.00SC_VPT_Learn_Together
as taught in 2011 MIT 6.00SC Introduction to Computer Science and Programming

[MIT OCW link](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-1/lecture-1-introduction-to-6.00/) :congratulations: 

>Programming is the most fun you can have with your clothes on... --John Guttag from Lecture 1

## Jan 12th 2019 Meetup @ NUS-ALSET

### Lecture 1 (Stored Program & Flow of control & Semantics) Notes:

**Declarative vs Imperative**
- Declarative is statements of facts :cop: :scroll:
- Imperative is "How To" step by step, like receipe :pencil2: :musical_score:

**Stored program computer vs Fixed program computer**
- Stored program computer is Turing Machine + The von Neumann architecture (i am stretching it here...)
- Fixed program is one machine built to do one thing, like the Enigma machine

Stored program computer treats data and instructions (programs) as the same thing

**Well-formed tring vs semantic meaning**

*I are big* is well-formed, but no semantic meaning*
>Syntax determines whether a string is legal, static semantics determine whether the string has meaning, and semantics assigns a meaning to a legal sentence (assuming no static semantic errors).


**Alan Turing showed that there are 6 primitive instructions each of which operated on one bit of information. And with those 6 primitive instructions you can do anything that can be done with a computer**


**Programming languages are just providing a set of primitive instructions (>= 6), a set of primitive control structures**
- set of primitive instructions
- flow of control, or mechanisms to control the order instructions are executed

**All programs are interpreted for the computer**

Compiled programs convert source code to **object code** then feed it to interpreter.

**Three types of errors of a program**
1. crash
2. run forever
3. give the wrong answer

### Lecture 2 (Operators & Variables) Notes:

**Types**

are classifications of objects. In Python, everything is an object, **even the Python code itself is an object. For stored-program computers, a program is just data, just like a number is data. Each object has a type.**

**Straight line program vs Branching program**

Straight line program goes through the program line-by-line and carries out each step. Branching program can run different sections depending on the conditions.

## Jan 16th 2019 Meetup @ NUS-ALSET

### Lecture 3 (Exhaustive Enumeration & Bisection Search) Notes:

- iteration to build programs whose execution time depends upon the size of inputs.
- search problems with brute force and bisection
- brute force and exhaustive enumeration
- approximation = find a `y` such that `y*y = x +- epsilon`, if finding exact x is too time-consuming to find
- **iterative algorithms** guess and check
- Generating guess: 1. exhaustive enumeration 2. Bisection search 3 Newton-Raphson (for root finding)

### Lecture 4 (Function & Scope) Notes:

- finding square root of numbers between 0 and 1 is tricky, since the square root will be larger than the number, eg 0.25's squart root is 0.5
- the most important thing to learn to **how to debug a program**
```python
# for number between 0 and 1
# sqrt_root will be larger than input_Number
# so guess**2 will never be greater than the top_margin
# so need to increase the search region to 1
if input_Number < 1:
    upper_bound = 1 + err_margin
    lower_bound = bottom_margin
```
- scope
- Formal parameters are the names of variables used inside a procedure; actual parameters (or arguments) are the values assigned to those names.

## Jan 26th 2019 Meetup @ NUS-SOC MR4

### Lecture 5 (Tuple,List,Dict & Aliasing & Mutability) Notes:

```python
x = 100
divisors = ()
for number in range(1,x):
    if x % number == 0:
        divisors = divisors + (number,)

print(divisors)
# (1, 2, 4, 5, 10, 20, 25, 50)
```
- mutability: A mutable object's values can be changed; we must be careful when working with mutable objects not to inadvertently change them.
- Tuples are immutable (as are strings). List and Dict are mutable.
- A dictionary is mutable, with immutable keys, and unordered.
- The usual way to access a value is `hand['a']`, where `'a'` is the key we want to find. However, this only works if the key is in the dictionary, otherwise we get a `KeyError`. To avoid this, the **safer way to access a value in dict** is to use **`hand.get('a', 0)`**. `d.get(key, default)` returns the value for `key` if `key` is in the dictionary, else `default`.
- `dict.copy()` returns a shallow copy of the dict, kind of like `s[:]`

### Lecture 6 (Recursion & Divide and Conquer) Notes:

Python2's `import string` and `string.lowercase` will strip white space and non-alphabet characters.
```python
>>> import string
>>> string.lowercase
'abcdefghijklmnopqrstuvwxyz'
```

- Base case: A base case is necessary in recursion; it determines when the procedure returns a value (or terminates), rather than continuing the recursive process.
- Recursive case: A recursive case calls the recursive procedure on a simpler version of the problem.
- Tower of Hanoi problem: you can have multiple recursive calls inside a function body, breaking down into a simplier version of the same problem, assume that can be solved, and let the recursions handle the rest


### Lecture 7 (Binary & Floating Point & Debugger) Notes:

**`repr`** can be used to show the detailed representation of the floating point before Python 2.7. Now use **`format()`**:
```python
format(0.1, ".25f")
'0.1000000000000000055511151'
```

Representation of 0.125 in decimal:
```
0.125 = 1*(10**-1) + 2*(10**-2) + 5*(10**-3)
```

Representation of 0.124 in binary:
```
0.125 = 0*(2**-1) + 0*(2**-2) + 1*(2**-3) = 0.001 base2
```

Representation of 0.1 in binray will be infinite, non-repeating decimal number:
```
0.1 = 1/10 = 1/(1010) base2 = 0.0(0011)^inf
```

- Do not test for `==` equality with floats.
- Computers use binary, floats are actually very close approximations of the actual values. Testing for equality can result in an unexpected error, so **it's better to determine whether two numbers are close enough for our purposes** rather than precisely equal.
```python
In [1]: x = 0.0

In [2]: numIters = 100000

In [3]: for i in range(numIters):
   ...:     x += 0.1

In [4]: print(x)
10000.000000018848

In [7]: def close_enough(x, y, epsilon=0.00001):
   ...:     return abs(x-y)<epsilon # True/False

In [8]: close_enough(x, 10000)
Out[8]: True
```

- If there is no integer `p` such that `num * (2^p)` is a whole number, then internal representation of `num` is always an approximation
- **Bisection search for debugging**: you can try to use binary search to locate where the bug is in your program:D


## Feb 21st 2019 Meetup @ NUS-SOC MR4

### Lecture 8 (Algorithm efficienty, Random Access Model, Big O) Notes:

- Big O notation to state algorithm complexity
- **Efficiency is about algorithms, not coding details**
- Clever algorithms are hard to invent, therefore we dont depend on clever algorithms, instead we depend on **problem reducing**
- **When confronted with a problem, we want to reduce it to a previously solved problem**
- How to turn a problem and fit it into a useful computation is usually about **how do i transform my problem to match a problem that some clever person already knows how to solve**
- **How do we think about efficiency?** We think about it in **two dimensions**: SPACE AND TIME.
- We can make a program run faster by using more memory, or use less memory at the cost of making it run more slowly.
- YOU DONT MEASURE ALGORITHM TIME COMPLEXITY BY TIMING THE PROGRAM EXECUTION!
- WE DO NOT THINK ABOUT COMPUTATIONAL COMPLEXITY IN TERMS OF HOW LONG A PROGRAM TAKES TO RUN ON A COMPUTER, because it is not a stable measure
- That is influenced by the speed of the machine, cleverness of the Python implementation, and it **depends on the input!!**
- **WE COUNT THE NUMBER OF BASIC STEPS**
- **A STEP is an operation that takes constant time**, for example, `an assignment`, `a comparison`, `an array access` etc
- To look at the computational complexity, we use RAM (**Random Access Machine**)
- in RAM, instructions are executed one after another, sequentially, we assume **constant time to access memory**
- RAM is not actually true, cos in old days memory is a tape, and in modern computers, there are memory hierarchy and parallel computing
- Best case, Worst case, Expected(average) case
- We almost never deal with expected case, because if the element is not in the list most of the time, then the query will lie near the end, for eg
- **complexity analysis almost always focus on the worst case, and it provides an UPPER BOUND**, what is the worst that can happen, so i have no surprises, and worst cases happen often
- We typically ignore the constants, we really care about **GROWTH WITH RESPECT TO SIZE**
- **HOW DOES THE RUNNING TIME GROW AS THE SIZE OF THE INPUT GROWS**
- WE DONT CARE if it is 3000 years or 9000 years, or 3000 days or 9000 days, it is too long either way. **SO WE IGNORE THE MULTIPLICATION FACTOR of N**
- Asymptotic growth and Big O notation
- O(n) means, this algorithm, the complexity, the time, grows linearly with n
- It is actually Omicron, but usually we just type **O**
- Upper bound of the asymptotic growth of the function
- Function F grows **no faster** than the quadratic polynomial x^2
- Order 1 = O(1), the time required is independent of the size of input
- Order log n
- Order n
- Order n log n (log linear)
- Order n^c (polynomial)
- Order C^n (exponetial)
- We usually want to capture the worst case as accurately as we can
- Theoriest usually write Theta for the case, but we usually write just big O for around the worst case
- O(n) where n is the number of digits of input `x`. So n = `log10(x)`
- **PEOPLE JUST WRITE O(N) AND THINK THEY ARE DONE. THEY ARE NOT!!! YOU MUST ALWAYS KNOW WHAT N MEANS!!!**, especially when your function has multiple inputs
- Have to very careful when looking at complexity, not to think you only have to look at the complexity of the program itself, like the number of recursive calls, but also **IS THERE SOMETHING THAT IS DOING INSIDE THIS FUNCTION THAT MIGHT BE MORE COMPLEX THAN YOU THINK?**

### Lecture 9 (Indirection and Linked List, Selection and Merge Sort) Notes:

- **Indirection**: Indirection is the ability to access something using a name or reference instead of the value itself.
- Python's list is not LINKED LIST, it is a list of locations of the objects in memory, each object is a pointer
- In constant time, you can access any object in a list, even though the objects in the list are of varying size
- Binary search only works when the list is already **sorted**
- **AMORTIZED COMPLEXITY**, if we sort the list once, and search it many times, the cost of the sort can be allocated to each of the searches
- Many algorithms depend on establishing and maintaining an **invariatn**. Invariant is something that is invariantly true
- For selection sort, the invariant = the prefix is always sorted
- Merge sort is a **divide and conquer** algorithm, invented by John Von Neumann

## Feb 23rd 2019 Meetup @ NUS-SOC MR4

### Lecture 10 (Hashing, Excetpions, and Classes) Notes:

- hashing can be used to achieve near constant time lookups
- hashing **converts the object to be hashed into an `int` that lies within a pre-defined range**
- hashing will produce **bucket**
- **Bucket: A list of items that have the same hash value.**
- hashing and **collision**
- hashing and Dictionary in Python is efficient search mechanism, but at the cost of space (memory)
- **Unhandled Exception** will cause the program to crash
- Unhandled exception can be handled, and this is a flow of control option in python.
```python
try:
    int(x)
except:
    print("i dont know what error to cath...")
```
If we do not give the `except` a specific name, it will go catch all exception. This is not encouraged because it shows the programmer did not anticipat the error
- in Python, everything is an object: **A collection of data and functions that operate on that data.**
- Class/Object is similar to **module: a module is a collection of related functions**, like `import math` and `math.log()`, and `log()` is a function related to `math` module
- The **data** of a class are called **attributes**
- **Message Passing Metaphor**: for `L.append(e)`, I am passing the message "append(e)" to the object L. And then there's a mechanism for looking up what that message means, and then the object L executes that message and does something.
- Nothing magical here, you can just think of `c.area()` as a fancy way of writing functions, you are absolutely correct
- **Method** is a **function associated with an Object**
- Class allows you to extend the language, by defining your own type!
- `Dict` and `List` are built in classes, their methods are read-only

### Lecture 11 (OOP, subclass, superclass, data hiding, inheritance) Notes:

- **class vs instance**
- **instance is the ACTUAL OBJECT built in accordance with the qualities of the class**
- **Abstract data type**: A set of objects and the operations on those objects.
- **The core of OOP is Abstract Data Type**. The fundamental notion of OOP is **Abstract data type: we extend the programming language by adding user defined types**
- Why is it called **ABSTRACT data type**? Because it is an interface - explains what the method *do*, not how they do it
- Built-in data types already provide this interface for you to use the methods without bothering with the low-level implementation
```python
class intSet(object):
    """An intSet is a set of integer."""
    def __init__(self):
        """Create an empty set of integer"""
        self.numBuckets = 47
        self.vals = []
        for i in range(self.numBuckets):
            self.vals.append([])
    def hashE(self,e):
        ...
```
`class xxx(object)` is saying xxx is a subclass of `object`, but this is redundent, as everything in Python is an object
- underbar underbar in Python has special status
- `__init__`: every time I create a new object of type `intSet`, `__init__` method of the class will be executed on that object
- **self** is a local variable in the class definition environment
- xxx is the **attributes** of the **INSTANCE** X of the **CLASS** intSet
- automatically pass an implicit object, self is referring to the object being created
- `s.insert(i)`, the `s` before the dot is actually the first argument to the method `insert`, so it is getting two arguments really
- Data hiding and abstract data type
- Data hiding: the things we are hiding is the instance variable, those are the variables associated with each instance of the class, AND class variables
- Instance variable we get a new copy each time we create a new instance of the class; Class variables are associated with the class itself, and you get only one copy of them
- It is useful to pull back and think about what abstractions would be useful, a style of programming where you organize your programs around abstract data types. Before writing the code, think about these types that would make it easy to write the code
- Subclasses can use all the functions of their superclass. They can also use any functions that are defined within the subclass; however, if the subclass uses the same name for a function which has also been used in the superclass, it will only use the subclass definition of that function
- Encapsulation means that names (of variables and methods) are stored in locations that then have to be accessed, called namespaces.
- Global variables can be replaced by class variables

## March 2nd 2019 Meetup @ NUS-SOC MR4

### Lecture 12 (Generator, Random Walk) Notes:

- `yield` is an example of a form called a **generator**
- generator is like `return`, but for `return`, when it found the first thing, it's going to give me back the value and it is done.
- generator is a function that remembers the point in the function body where it last returned, plus all the local variables
- it is going to keep track of what was the state when i did the computation, so that if i call it a second time, it goes right back to that state and continues the computation
- a **yield or Generator** does is like what you normally do when walking through a list, but it gives you some control
- **HOW DO WE BUILD COMPUTATIONAL MODELS TO SOLVE REAL PROBLEMS?**
- Analytic methods, like a mathematical function, predict behavior given some initial conditions and some parameters, like Newtonian physics, analytic models, Spring constants, things that let you predict what the system is going to do
- but sometimes you are better off with **SIMULATION METHODS**
- systems that are not mathematically tractable, successively refining a series of simulations
- simulation means giving me an estimate, rather than a prediction, give me a sense of what might happen to a system under certain conditions and doing that multiple times, actually running a model oft he system rather than trying to predict exactly what's going to happen
- simulation: build a model, give useful information about behavior of a sytem, approximation to reality
- simulation models are **descriptive, not prescriptive**, it is a good guess of what's going to happen, for the same scenario, i run the simulation multiple times and get different answers
- Einstein built a model that introduced this sort of stochastic thinking into the world of physics, Brownian motion
- Brownian motion is an example of a **random walk**
- Random walks is an **incredibly useful way of building a simulation**
- The essential idea of a random walk is, if i have a system of interacting objects, could be pollen particles, i want to model what happens in that system under the assumption that each one of those things is going to move at each time step under some random distribution
- build a set of classes that would let me build this simulation, part of the design process here is I want to try and invent classes that correspond to the types of things I expect to see happening
- Model a drunk, model a field, and to keep track of where the drunk is in the field, called location


### Lecture 13 (Non-determinism and Stochastic process) Notes:

- Random walks simulation doesnt provide us enough information to interpret it
- how do we think about the results of programs when the programs themselves are stochastic
- almost everything in the real world is stochastic
- Copenhagen Doctrine, led by physicists Bohr and Heisenberg, argued that at its most predictable and most fundamental level, the behavior of the physical world cannot be predicted. One can make probabilistic statements of the form x is highly like to occur, but not statements of the form x is certain to occur
- Einstein and Schrodinger vehemently disagreed
- The heart of the debate **was the validity of casual-non-determinism**
- Causal means caused by previous events
- Causal non-determinism was the belief that not every event is caused by previous events
- Predictive non-determinism: **our inability to make accurate measurements about the physical world makes it impossible to make precise predictions about the future**
- from Einstein: "*the essentially statistical character of contemporary theory is solely to be ascribed to the fact that this theory operates with an incomplete description of physical systems*"
- ie. things are not unpredictable, they just look unpredictable, because we dont know enough about the initial states
- We have to assume that the world is non-deterministic, because we cant actually predict it
- **Stochastic processes: a process is stochastic if its next state depends on BOTH the previous states and some random element**
- random.choice... that function and almost all of the other functions in python that involve randomness are implemented using **random.random**
- random.random generates a random float that is 0-1
- in a stochastic process, two events are independent if the outcome of one event has no influence on the outcome of the other
```python
import matplotlib.pyplot as plt
```
- All plots should have informative titles, and all axes should be labeled


## March 9th 2019 Meetup @ NUS-SOC MR4

### Revision on testing, OOP, generator
- classes of tests and defensive programming
- unit testing: testing each function separately
- regression testing: catch re-introduced errors that were previously fixed
- integration testing: does the overall program work?
- black box testing: designed without looking at the code
- glass box testing: use code directly to test, path-complete if all potential paths through code is tested at least once
- `c.distance(origin)` and `Coordinate.distance(c, origin)` are the same
- `c.distance((origin)`, c iis object on which to call method, distance is name of method, origin is parameter (not including self, self is impled to be c)
- `Coordinate.distance(c, origin)`, Coordinate is name of class, distance is name of method, (c, origin) are parameters, including an object on which to call the method, representing self
- use `isinstance(x, type)` to check if an object is of certain class/type


## March 16th 2019 Meetup @ NUS-SOC MR4

### Revision on OOP:
- `Animal.__str__(cat)` to still use the superclass method
- `class D(C, B)` the order of the superclasses. Class D inherits from class C first then from class B. This means if a method is found in C, B won't be searched anymore.
- dont mix up what is done in the constructor (or more specifically the __init__ method) and inheritance.
- class variable is defined inside class BUT OUTSIDE ANY CLASS METHODS, like outside `__init__`, and it is shared among all objects/instances of that class
- `zfill(3)` fill up the number with 0
- p4 < p1 is equivalent to `p4.__lt__(p1)` which means we use the `__lt__` method associated with the type of p4, the specific object calling `__lt__` is the one that is going to define the type and therefore the method
- Be careful when overriding methods in a subclass. **substitution principle**: important behaviors of superclass should be supported by all subclasses

## March 23rd 2019 Penang Break
## March 30th 2019 KL break

## April 6th 2019 Meetup @ Johor Bahru R&F Part 1

### Lecture 14 (Monte Carlo and Inferential Statistics) Notes:
- Pascal is considered the founder of probability theory
- "is it profitable to bet that given 24 rolls of a pair of fair dice, you would roll a 6,6?"
```python
import random
def rollDie():
    """returns a random int between 1 and 6"""
    return random.choice([1,2,3,4,5,6])
def testRoll(n=10):
    result = ''
    for i in range(n):
        print(rollDie())
def checkPascal(numTrials=10000):
    doubleSix = 0.0
    for i in range(numTrials):
        for j in range(24):
            d1 = rollDie()
            d2 = rollDie()
            if d1 == 6 and d2 == 6:
                doubleSix += 1
                break
    print("probability of getting doubleSix = ", doubleSix / numTrials)
    # probability of getting doubleSix =  0.4892
```
- in practice, write simulation and do probabilities at the same time (figure out the answer analytically) code vs math
- **Monte Carlo Simulation** is the most popular kind of simulation: **A simulation which arrives at an approximation of a probability by running many, many trials.**
- Monte Carlo was coined in 1949 by Stanislaw Ulam and Nicholas Metropolis
- from Ulam: "...1946, ...pure combinatorial calculations, a more practical method than 'abstract thinking', lay it out 100 times and simply observe and count the number of successful plays... and more generally, how to change processes described by certain differential equations into an equivalent form interpretable as a succession of random operations"
- as early as 1946, people were thinking about the question of moving away from solving systems of equations, to **using randomized techniques to simulate things and try to find out what the actual answer was**
- Monte Carlo technique was used during the Manhattan project to predict what would happen during nuclear fission and worked
- Monte Carlo simulations are an example of **inferential statistics**
- **random sample tends to exhibit the same properties as the population from which it is drawn.** **(always ask yourself: DOES THIS ASSUMPTION HOLD?!)**
- will 1000000 times of throwing a dice representative of all possible throws of the dice, the infinite number possible throws?
- we have to think about the number of tests and how close the answer is to what you would get if you did things at random **(null hypothesis is what you get with a random event)**
- when you do a simulation, if you get something that is far from the null hypothesis, or when you sample a population, you get something that is distant from the null hypothesis, you can assume that maybe you are seeing something real
- the **law of large numbers (Bernoulli's law)** underlies the inferential statistics: repeated **independent** tests
- law of large numbers does not imply that if i start out with deviations from the expected behavior, those deviations are likely to be "evened out" by opposite deviations in the future **(independent means memoryless)**
- **gambler's fallacy**: The belief that random numbers will even out constantly (e.g. that after a string of heads, it's “time for” the coin to come up tails.)
- you can never get absolute certainty from sampling, "i am certain within the following range that i have the right answer"


### Lecture 15 (statistical thinking, SD, SE, variance) Notes:
- **just because we have the right answer doesn't mean our thinking is any good**
- how many samples are needed to have confidence in result?
- at the root of it, is **variance**: meausre of how much spread in the possible outcomes
- **having multiple trials** is more important absolute number of flipping of coins
- each **trial** will give a separate **outcome**, then we can look at **the outcomes of the different trials** for **variance**
- **standard deviation**: measuring the fraction of values distant/close to the mean
- relationship between the number of samples we've looked at and how much confidence we should have in the answer
- As you flip more coins, the variance between trials should get smaller because randomness is playing less a role
- **it is not good enough to get lucky and get the correct answer, you have to have evidence that can convince somebody that really is the answer, and the evidence here is the small standard deviation**
- standard deviation is **relative**, **it should be relatively small!! (100 vs 1 is meaningless, it should be relative to the MEAN!!!!!)**
- **coefficient of variation** is **more useful than standard deviation**
- **WARNING1: when mean is near 0, small changes in the mean are going to lead to large changes in the coefficient of variation** (dont use when mean is near 0)
- **WARNING2: coefficient of variation cannot be used for confidence intervals**
```
y = [1,1,2,2,3,3,3,4]
pylab.hist(y, bins=20) # for histogram
```
- **results with smaller SD is more credible, not more accurate, but more believable**
- show things side-by-side, axis need to be same units, otherwise deceptive
- normal distribution peaks at mean, falls off symmetrically
- normal distribution: 1. **nice mathematical properties** 2. many naturally occurring examples
- **mathematically characterized by 2 characters: mean and standard deviation**, knowing these two is the same as knowing the whole distribution
- mean and sd can be used to compute **confidence interval**
- *So instead of estimating an unknown parameter, and typically we estimate it by a single value, the mean of a set of trials*, a **confidence interval instead allows us to estimate the unknown paramter by providing a range that is likely to contain the unknown value**, and a **confidence level** that the *unknown value* lies within that range
- empirical rules for normal distribution (68% within 1sd ...)
- Another trick, **standard error** is an estimate of the standard deviation, **you can only do this under the assumption that the errors are normally distributed and also that the sample population is small relative to the actual population**
- from polls experience, the results are indeed typically normally distributed, so not a bad assumption
- If for example, a pollster sample 1000 voters, 46% say they will vote for XYZ, and the Standard Error is 1.58%. We would interpret this to mean that in 95% of the time, the true percentage of votes for XYZ is within 2 SE of 46%.
- SE = `((p*(100-p)/n))**0.5`
- 1.58% SE calculated from formula is pretty close to 1.6% from simulations. SE is an attempt to just use a formula to estimate what the SD is going to be (because the differences are normally distributed, the distribution is normal, the standard error is a very good approximation to the actual SD) *that is what pollsters rely on*
- many random variables have an approximately normal distribution
- **many experimental setups have normally distributed measurement errors**, first discovered by 1800s by Gauss, who assumed a normal distribution of measurement errors in his analysis of astronomical data
- the mistakes you make in measurement is likely to be normally distributed, *most of science assumes normal distributions of measurement errors in reaching conclusions about the validity of their data*

### Lecture 16 (randomness in physical modeling, monte carlo for pi) Notes:
- One of the interesting things about a Gaussian is it can be fully characterized by its mean and its standard deviation. This concept of being able to take a curve and characterize it with a small number of parameters is a very important way of looking at **modeling physical systems (how do we construct computational models that will help us understand the real world?)**
- When we can, we love to model distributions as Gaussian, becuase they are so nicely characterized, nice rules that tell us how close things lie to the mean et cetera. However, it is important to understand that if something is not actually Gaussian distributed, and we pretend it otherwise, we can get very misleading results out of our model (not all distributions are normal, for instance)
- Gaussian/Normal distribution (symmetric and can be fully characterized by its mean and standard deviation);
- Uniform distribution **eg roll dice** (each outcome has the same probability. The distribution can be fully characterized with a single parameter, the range);
- Exponential distribution **eg plan highway systems to model inter-arrival times, how much time there is between each car entering a checkpoint** (the *only* continuous memory-less distribution, meaning that the probability of any outcome at a point in time is independent of the outcome at any previous time)
- Assume that at each time step, each molecule has a probability `p` of being cleared by the body, the system is memoryless in the sense that at each step the probability of a particular molecule being clearred is independent of what happened at the previous steps
- analytic model vs simulation model
- **Evaluating a model, ask two things: 1. fidelity to the actual physical situation (credibility, and reasoning) and 2. utility (what questions are answerable with the model)**
- not easy to write a simple closed-form formula in analytic model but easy to produce a simulation model
- **Monty Hall Problem**: Monty opens a door that he knows does not contain the prize, the choice of doors is NOT independent of choice of player, *because Monty will never choose the door that the player has initially picked*
- From probability point of view, things can be based upon whether decisions are independent of previous decisions (not independent), monty is choosing based on what he knows
- These kind of simulations are very useful for tackling problems in which predictive non-determinism plays a role, when there is some inherent randomness in the problem, and hard to model analytically, and use randomness in the code
- BUT using randomized algorithms to solve problems in which randomness plays no role! The ability to use randomization to solve problems that are not random   
- in the 1700s, French mathematicians Buffon and Laplace proposed finding pi using stochastic simulation in needle-dropping
- There is no guarantee that by running a bigger trial, you will get a more accurate result. There is a guarantee that I can have more confidence in the result. Since the SD is small, and the numbers are normally distributed, you can be pretty sure the true value of PI is 3.1407 et cetera, plus or minus 0.0002, with a 95% confidence
- **1. A problem that had nothing to do with randomness, the value of pi is not a random number. Yet we use randomness to solve it. 2. And we use simple statistics to know whether or not we should believe our solution**
- Same technique can be used to do **integration (area under curve)**
- You can draw a curve, drop your needles, you count how many fall under the curve, how many dont fall under the curve in some larger area
- this kind of simulation is NOT good way for solving **single integrals**, it is much better to use something like *Simpson's rule*
- but it is very useful for double and triple integration using Monte Carlo simulation

### Lecture 17 (linear regression and curve fitting) Notes:
- key assumption is that simulation is a model of reality. **statistics test are about the simulation, not about the reality itself**
- **Before believing the results of any simulation, we have to have confidence that our conceptual model is correct AND we have correctly implemented that conceptual model**
- scientists always run some experiments to see whether their derived result is actually at least plausibly correct
- **statistics are good to show we have got the little details right at the end, bu we have got to do a sanity check FIRST**
- statistical test is not about truth
- **physical reality VS theoretical model VS computationl models**
```python
xVals = pylab.array(xVals)
yVals = pylab.array(yVals)
```
- type conversion from list to array. this is a type implemented by a class supplied by PyLab, which is built on top of NumPy
- array similar to list, but has point-wise operations, array useful for math
- **C/Pascal array is NOT THE SAME as array in python and Matlab**
- **need objective function to tell us how good is a particular fit, measure of the goodness of the fit**
- least square fit is the most commonly used **objective function for measuring how good any curve fits a set of points**
- polyfit in Pylab (observed X, observed Y, degree of polynomial)
- **Linear regression does not mean it is for LINEAR LINES ONLY, it can be used to find polynomials other than lines!**
- *why are we building a model? so we can better understand the physical reality*
- *one of the things we often do with models is use them to predict values that we have not been able to run in our experiments*. Simulation model to predict what would happen in an experiemtn you cant run.
- model can have very bad predictive value
- if you are willing to get a high enough degree polynomial, you can get a pretty good fit to almost any data, BUT IT DOES NOT PROVE ANYTHING, IT IS NOT USEFUL!
- look at the raw data
- **How do we know which line (linear vs cubic) is a better representation of physical reality, a better model?** Cos I can just delete all the points except two, and get a line that was a perfect fit with mean squared error of 0! **So we have a question here that CANNOT be answered by statistics**
- it is not just a question of how good my fit is, **i have to go back to the theory**. What the Hooke theory tells me is that it should be linear, and i have a theoretical justification of discarding the last six points, it is plausible that i exceeded the limit. I dont have a theoretical justification of deleting six arbitrary points somewhere in the middle that I didnt happen to like because they didnt fit the data.
- interplay the physical reality and computational model
- **How do we measure which FIT is better? Polyfit is minimizing the mean square error, so one way to compare two fits would be to say what is the mean square error of the line vs parabola**
- in fact, computing the **mean square error is a good way to compare the fit of two different curves**. BUT!!! it is **not useful for goodness of the fit in absolute terms, just comparison**
- instead, we use **coefficient of determination R^2 = 1 – (estimated error)/(variance of the actual data)**

### Lecture 18 (Coefficient of Determination, computational model & Optimzation problem) Notes:
- R^2 = 1 - (EE/MV) = 0, ie Estimate-measured = 0, explains all the variability of the data
- R^2 = 0, the model is worthless
- model, theory, and computation and relavance of data
- accurary vs precision (138.62 is precise, but you can compute it as precisely as you want, but that does not mean it is actually accurate)
- start with experiment -> used computation to find and evaluate a model -> use theory and analysis and computation to derive a consequence of the model
- **optimization problem: 1. objective function you are minimizing or maximizing 2. a set of constriants to be satisfied that must be obeyed**
- classic optimization problem and map their solutions
- **problem reduction**
- knapsack and greedy algorithm
- **greedy** algorithm is **iterative**, at each step, choose locally optimal solution
- greedy efficient algorithm complexity O(nlgn)
- **Brute Force way**: enumerate all possibilities and then choose best that meets constraint

## April 6th 2019 Meetup @ Johor Bahru R&F Part2

### Lecture 19 (power set knapsack and machine learning) Notes:
- power set, smallest subset is empty set, largest subset is all the items
- use decimalToBinary function, map the powersets to all the binary digits, **now we have the set of all possible items one might take, irrespective of whether they obey the constraint of not weighting too much**
- will find at least one optimal answer
- greedy algorithm only choose locally optimal
- global optimum
- inherently exponential
- **Machine Learning**, superficially you can say ML is build programs that learn. However, every program we write learns something. Newton's methond is "learning" the roots of the polynomial, fitting curves to data, we were learning a model of the data, that is what regression is.
- **A major focus of machine learning research is to *automatically learn to recognize complex patterns* and *make intelligent decisions based on data***
- **inductive inference**: the program observes examples that represent an incomplete information about some **statistical phenomena** and then tries to **generate a model**, just like curve fitting, that **summarizes some statistical properties** of that data and can be used to predict the future, for example, give you information about unseen data
- two approaches to ML: **supervised learning and unsupervised learning**
- supervised learning: associate a label with each example in a training set
- if the label is discrete, it is **classification problem** (discrete value, boolean, etc)
- if the label is real value, it is **regression problem** (curve fitting)
- *Based on the examples from the training set, the goal is to build a program that can predict the answer for other cases before they were explicitly observed*. So we are trying to **generalize from statistical properties of the training set to be able to make predictions about things we havent seen**
- **Key Question for Supervised Learning 1: Are labels accurate?** maybe some of the real-world labels are wrong
- **Key Question for Supervised Learning 2: Is past representative of future?** you can hit some singularity and the past is not a good predictor of the future
- **Key Question for Supervised Learning 3: Do you have enough training data to generalize?**
- **Key Question for Supervised Learning 4: Feature extraction**
- **Key Question for Supervised Learning 5: How tight should the fit be?** if your objective function is to minimize training error, you might have overfitting training data will not generalize well for future data. the goal is to *predict future points*. A big problem in ML is if you overfit to your training data, it might not generalize well and might give you bogus answers going forward
- **Unsupervised learning has training data, but no labels**
- in unsupervised learning, you are learning **regularities of data**, is to **discover the structure**
- **The dominant form of unsupervised learning is clustering**
- **Key Question for Unsupervised Learning 1: What does clustering mean? It is the process of organizing the objects or the points into groups whose members are similar in some way**
- **Key Question for Unsupervised Learning 2: What do we mean by similar?**
- clustering algorithm Walmart beer and diapers
- clustering algorithm Amazon books
- clustering algorithm in insurance companies, biology, netflix
- clustering is **optimization problem**
- good clustering should have **low intra-cluster dissimilarity, high inter-cluster dissimilarity**
- model dissimilarity using **variance**
- **Objective function of the optimization problem:** find a set of clusters C such that the "badness" of C is minimized?? single item as each cluster
- **Constraints of the optimization problem**: at most K clusters OR max distance between clusters
- **solving clustering problem is computationally prohibitive, so in practice people resort to greedy algorithm**
- **Two most common greedy algorithms for clustering:** 1. k-means (exactly k clusters) 2. hierarchical
- Hierarchical clustering or **agglomerative clustering: Clustering that merges clusters iteratively.**
```python
# a set of N items to be clusters
# NxN Distance Matrix
# 1) Assign each item to own cluster
# 2) Find the MOST similar pair of clusters and merge them
```
- **Linkage criteria:** 1. **single-linkage or connectiveness or minimum method** (best case), 2. **complete-linkage or diameter or maximum method** (furthest)
- n^2 complexity, and only finding local opimum
- **A big issue in deciding to get these clusters was my *choice of features***
- **The Most Important Issue in ML is if we are going to say which points are similar to each other, we need to understand out *feature space***
- multi-dimensional data need feature vector that incorporates multiple features
- In real-world problems, we go from large number of features associated with objects or things in the real world, to feature vectors that allow us to automatically deduce which things are quote "most similar"

### Lecture 20 (more clustering) Notes:
- Generalizing **from a feature being a single number to the notion of a feature vector**
- Features used to describe an object are now represented by a vector, typically of numbers
- If the vectors are all in the same physical units, we could easily imagine how we can compare two vectors, BUT how can you compare distance value to temperature value?!
- **How to scale the elements of the vector?** Temp vs distance
- **Feature selection and scaling is critical**, it is the **thinking**, and then the rest gets to be fairly mechanical
- what features to use and how to scale? **DOMAIN KNOWLEDGE**. So we have to think about the objects that we are trying to learn about and what the objectives of the learning are.
- **Distance**: **Minkowski Metric** (Euclidean distance vs Manhattan distance)
- Manhattan is grid-like, metric (for genes eg)
- **Nominal categories things that have names rather than numbers**
- nominal categories, that have names, we convert them to a number
- domain knowledge and judgement people have to make **sorts of things that are not mathematical questions bu judgements that people have to make**
- **Scaling == Normalization**, every feature between 0-1
- Clusteirng mammals have **unbounded number of features**, the choice of features and weighting will have an enormous impact on what clusters you get!
- *How should you choose which features you want? You have to begin by thinking about the reason you are doing the clustering in the first place!* **What is it that you are trying to learn about the mammals?** For example, choose the objective of eating habits, cluster mammals based on what they eat. Hypothesis: you can infer mammals' eating habits from their teeth.
- Typically when we are using ML, we are trying to learn about something that we have limisted or no data.
- **Scaling really matters**
- **What is a better answer? It is not a meaningful question. It depends on what I am trying to infer, what we hope to learn from the clustering.** By using different kinds of scaling or different kinds of features, we can learn different things about the counties.
- **k-means** is very efficient, much faster than hierarchical clustering
```python
# k-means mechanism
# step 1: choose k, k is the total number of clusters you want to have when you are done
# step 2: choose k points as initial centroids, randomly chosen
# step 3: assign each point to the nearest centroid
# step 4: for each of the k clusters, choose a new centroid
# step 5: assign each point to the nearest NEW centroid
# step 6: repeat 4&5 until change is "small"
```
- So each time I do step5, i can keep track of how many points I have moved from one cluster to another
- Or each time I do step4, how much have I moved the centroids
- Each of those gives me a measure of how much change the new iteration has produced
- For the **complexity**, each iteration is O(kN), k=number of cluster, N=number of points, and do some number of iterations
- **typically for k-means, we dont need a lot of iterations to get an answer, typically not proportional to N**
- centroid is the "average point", it needs not be any of the points in the cluster

## April 12th 2019 Meetup @ Johor Bahru Pinnicle Part 1

### Lecture 21 (K-means, graph) Notes:
- **unlike hierarchical clustering, where we could run it and get what's called a dendrogram and stop at any level and see what we liked, k-means involves knowing in advance how many clusters we want**
- When I am done clustering using k-means, I am going to get **some statistics about the clusters**. **Keep track of the number of iterations and the maximum diameter of a cluster**, *the cluster in which things are least tightly grouped, and this will give me an indication of how good a clustering I have*
- Because the initial cluster is chosen at random, you can get different results each time you run it. So you can run it many times and choose the "best clustering". What metric are you using for best clustering? It is a **min-max metric: choosing the minumum of the maximum diameters**. Finding the worst cluster and trying to make it as good as it can.
- We always scale and normalize so we dont get fooled by wide dynamic range
- **The name of the game here is we are trying to see whether we can infer something interesting by clustering (unsupervised learning). So one of the questions we should ask is how different is what we are getting here from if we chose something at random**
- Now remember we did not cluster things based on income, I happen to plot income here just because I was curious as to how this clustering related to income. Suppose we had just chosen at random and split the counties at *random* into 100 different clusters, what would the histogram to look like?
- supervised and unsupervised (**interestingly, unsupervised learning is probably used more often in the sciences than supervised**)
- supervised learning: training set with labels, infer relationship between features and labels
- unsupervised learning: all unlabelled data, relationship among points, infer relationship among points (features)
- Be wary of overfitting, if trainning set data is small
- Features matter, which, normalized, weight
- **FEUATURES MATTER**
- Graph theoretic model
- A graph is a set of nodes (vertices) connected by set of edges (arcs)
- digraph or directed graph if edges uni-directional
- first graph problem by Euler, 7-bridge problem
- Euler's Model o fthe problem
- edges can have weights
- WWW weighted directed graph in Google
- Graph subset of digraph
- adjacency matrix NxN matrix
- adjacency list

## April 13th 2019 Meetup @ Johor Bahru Pinnicle Part 2

### Lecture 22 (Graph) Notes:
- 

### Lecture 23 (Dynamic Programming) Notes:
- optimal substructure and overlapping subproblem
- merge sort has optimal substructure
- merge sort does not have overlapping subproblem
- shortest path has both properties, so can use 