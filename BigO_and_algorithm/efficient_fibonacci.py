# the inefficient fibonacci
def inefficient_fib(N):
    if N == 0 or N == 1:
        return 1
    else:
        return inefficient_fib(N-1) + inefficient_fib(N-2)

print(inefficient_fib(5))

# since we already know the values of fib(2), fib(1) etc
# we should store them in dict for reuse
# do a lookup first
def efficient_fib(N, lookup_table):
    print("now lookup_table is: ", lookup_table)
    if N in lookup_table:
        return lookup_table[N]
    else:
        ans = efficient_fib(N-1, lookup_table) + efficient_fib(N-2, lookup_table)
        # store ans in lookup_table
        lookup_table[N] = ans
        return ans

base_case = {0:1, 1:1}

print(efficient_fib(0, base_case)
print(efficient_fib(5, base_case)
