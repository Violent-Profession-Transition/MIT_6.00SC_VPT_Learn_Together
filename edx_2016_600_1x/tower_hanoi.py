def print_move(fr, to):
    print("move from ", fr, " to " ,to)

print_move(1,2)

# the key is to break the tower into two stacks, one large stack and n-1 stack
def Towers(n, fr, to, spare):
    print("moving ", n, " disks from ", fr, " to ", to, " using ", spare, " as spare")
    if n == 1:
        print_move(fr, to)
    else:
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)

#  Towers(1, "P1", "P3", "P2")
#  Towers(2, "P1", "P3", "P2")
Towers(3, "P1", "P3", "P2")
