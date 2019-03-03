- big-O notation in the analysis of algorithms to describe an algorithm’s usage of computational resources, in a way that is independent of computer architecture or clock rate.
- In 6.00 we generally seek to analyze the worst-case running time. However it is not unusual to see a big-O analysis of memory usage.
- The worst case running time, or memory usage, of an algorithm is often expressed as a function of the SIZE of its input using big O notation
- big O notation only provides an upper bound, However, we generally seek to provide the tightest possible bound, if it is O(n^2) and also O(n^3), we say it is O(n^2)
- big-O notation allows us to compare different approaches for solving problems, and predict how long it might take to run an algorithm
on a very large input.
- With big-O notation we are particularly concerned with the scalability of our functions
- This is particularly important in the realm of scientific computing: for example, doing analysis on the human genome or data from Hubble involves input (arrays or lists) of size well into the tens of millions (of base pairs, pixels, etc).
- O(1) constant, not dependent on the size of the input
- O(lgn) fastest time bound for search
- O(n) something you need to examine every item of your input
- O(n lgn) fastest time bound we can currently achieve for sorting a list of elements
- O(n^2) for nested loop
- big O is concerned with the long-term or limiting behavior of functions, how our algorithm behaves for very large values of n, when n is big enough, n^3 term will always dominate the n^2 term
```python
def multiply(x, y):
    result = 0
    for i in range(y):
        result += x
    return result
```
this funciton is O(y), dependent on the size of input y
- recursion is analyzed with tree
