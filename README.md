# MIT_6.00SC_VPT_Learn_Together
as taiught in 2011 MIT 6.00SC Introduction to Computer Science and Programming

[MIT OCW link](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-1/lecture-1-introduction-to-6.00/) :congratulations: 

>Programming is the most fun you can have with your clothes on... --John Guttag from Lecture 1

## Jan 12th 2019 Meetup @ NUS-ALSET

### Lecture 1 Notes:

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

### Lecture 2 Notes:

**Types**

are classifications of objects. In Python, everything is an object, **even the Python code itself is an object. For stored-program computers, a program is just data, just like a number is data. Each object has a type.**

**Straight line program vs Branching program**

Straight line program goes through the program line-by-line and carries out each step. Branching program can run different sections depending on the conditions.

## Jan 16th 2019 Meetup @ NUS-ALSET

### Lecture 3 Notes:

- iteration to build programs whose execution time depends upon the size of inputs.
- search problems with brute force and bisection
- brute force and exhaustive enumeration
- approximation = find a `y` such that `y*y = x +- epsilon`, if finding exact x is too time-consuming to find

### Lecture 4 Notes:

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

### Lecture 5 Notes:

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

