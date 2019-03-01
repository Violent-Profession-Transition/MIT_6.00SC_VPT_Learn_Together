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


### Lecture 7 (Binary & Floating Point & Debugger) Notes:

**`repr`** can be used to show the detailed representation of the floating point before Python 2.7. Now use **`format()`**:
```python
format(0.1, ".25f")
'0.1000000000000000055511151'
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
- **Message Passing Metaphor**
- **Method** is a **function associated with an Object**
- Class allows you to extend the language, by defining your own type!
- `Dict` and `List` are built in classes, their methods are read-only


