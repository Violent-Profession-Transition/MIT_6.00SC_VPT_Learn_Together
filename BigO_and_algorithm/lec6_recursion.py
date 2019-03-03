# recursive call to find the exponential result
def find_exponential(Num, x):
    """
    Num to the power of x
    """
    # Base case:
    if x == 1:
        return Num
    else:
        return Num * find_exponential(Num, x-1)

print(find_exponential(5, 3))
print(find_exponential(2, 5))

print(">>>>>>>>>>>>>")

# recursive call to detect for palindrome
def is_Palindrome(S):
    # Base case:
    # if S has only one character, it is palindrome
    if len(S) <= 1:
        return True
    # if the first and last char matches
    elif S[0] == S[-1]:
        # recursive case:
        return is_Palindrome(S[1:-1])
    else:
        return False

print(is_Palindrome("lala"))
# False
print(is_Palindrome("mouiuom"))
# True

print(">>>>>>>>>>>>>")

# recursive call to calculate factorial
def factorial(Num):
    # Base case:
    if Num <= 1:
        return 1
    # recursive case:
    else:
        return Num * factorial(Num -1)

print(factorial(1)) # 1
print(factorial(2)) # 2
print(factorial(3)) # 6

print(">>>>>>>>>>>>>")

# recursive call to calculate fibonacci sum
def fibonacci(N):
    """
    N is the the number of month,
    at the end of N month, what is the total number of
    female rabbits
    """
    # Base case:
    if N <= 1:
        return 1
    else:
        return fibonacci(N-1) + fibonacci(N-2)

print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))

# list fibonacci sequence recursively
def list_fibonacci(N):
    fib_array = []
    for i in range(N+1):
        fib_array.append(fibonacci(i))
    return fib_array

print(list_fibonacci(3))
print(list_fibonacci(4))
print(list_fibonacci(5))
print(list_fibonacci(6))
