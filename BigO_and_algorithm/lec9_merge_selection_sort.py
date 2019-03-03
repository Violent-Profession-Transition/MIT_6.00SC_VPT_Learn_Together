# selection sort
def find_min(L):
    curr_min = L[0]
    for item in L:
        if item < curr_min:
            curr_min = item
    return curr_min

assert(find_min([2,4,5,1,7]) == 1)
assert(find_min([5,1,7]) == 1)

def selection_sort(L):
    for i in range(len(L)-1):
        print("### new i ###")
        print("now i is: ", i)
        print("finding min in ", L[i:])
        curr_min = find_min(L[i:])
        curr_min_index = L.index(curr_min)
        L[i], L[curr_min_index] = L[curr_min_index], L[i]
        print("now L is: ", L)
    return L

print(selection_sort([3,2,4,1,5]))

print(">>>>>>>>>now merge sort<<<<<<<<<<<<<")

# merge sort
def merge_list(L1, L2):
    print("merge_list called, merging {} and {}".format(L1, L2))
    merge_list = []
    i, j = 0, 0
    # compare between two lists
    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            merge_list.append(L1[i])
            i += 1
        else:
            merge_list.append(L2[j])
            j += 1
        print("now merge_list is: ", merge_list)
    # append the remaining L1, if any
    while i < len(L1):
        merge_list.append(L1[i])
        i += 1
        print("now merge_list is: ", merge_list)
    # append the remaining L2, if any
    while j < len(L2):
        merge_list.append(L2[j])
        j += 1
        print("now merge_list is: ", merge_list)
    return merge_list

print(merge_list([1,3,5], [2,4,6]))
print(merge_list([7], [2,3]))
print(merge_list([3,5], [6]))

def merge_sort(L):
    print("merge_sort called, sorting ", L)
    # Base case
    if len(L) <= 1:
        #  print("single L: ", L)
        return L
    # recursive case
    else:
        mid = len(L) // 2 # slice need integer
        print("processing the left side...")
        left = merge_sort(L[:mid])
        print("processing the right side...")
        right = merge_sort(L[mid:])
        return merge_list(left, right)

print(merge_sort([7,3,2,6,5,1,4,10,18,7,9,2,0,13,8,5]))
