import random
mylist = []

for i in range(random.randint(1, 10)):
    random.seed(0)
    if random.randint(1, 10) > 3:
        number = random.randint(1, 10)
        mylist.append(number)
print(mylist)
# a list of 7s of random length


print("*** Random Seed = 0")
random.seed(0)
for i in range(5):
    print(random.randint(1,10))
print("-----")
print("*** Random Seed = 0")
random.seed(0)
for i in range(5):
    print(random.randint(1,10))
print("-----")
print("*** Random Seed = 0")
random.seed(0)
for i in range(10):
    print(random.randint(1,10))

print("*** Random Seed = 1")
random.seed(1)
for i in range(5):
    print(random.randint(1,10))
print("-----")
print("*** Random Seed = 1")
random.seed(1)
for i in range(5):
    print(random.randint(1,10))

