def perm(items, n):
    print("&&&&&&&& perm({}, {})".format(items, n))
    result = []
    # base case
    if n == 1:
        return [i for i in items]
    # recursive case
    else:
        for x in range(len(items)):
            for y in perm(items[:x]+items[x+1:], n-1):
                if isinstance(y, list):
                    entry = [items[x]] + y
                else:
                    entry = [items[x]] + [y]
                # de-duplicate
                if entry not in result:
                    result.append(entry)
                    print("entry added: ", entry)
        return result

def perm_yield(items, n):
    print("&&&&&&&& perm_yield({}, {})".format(items, n))
    # base case
    if n == 0:
        yield []
    # recursive case
    else:
        for x in range(len(items)):
            for y in perm_yield(items[:x]+items[x+1:], n-1):
                entry = [items[x]] + y
                print("entry added: ", entry)
                yield entry

