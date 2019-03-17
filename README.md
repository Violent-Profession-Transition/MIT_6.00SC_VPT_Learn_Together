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


### Lecture 13 () Notes:

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
