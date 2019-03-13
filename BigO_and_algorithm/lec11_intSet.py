class intSet(object):
    # An intSet is a set of integers
    def __init__(self):
        """create an empty set of integers"""
        self.num_Buckets = 47
        # value is the hash table itself
        self.value = []
        for i in range(self.num_Buckets):
            self.value.append([])

    def hash_elem(self, e):
        # Private function, should not be used outside of class
        """return a remainder from 0 - len(num_Buckets)"""
        return abs(e) % len(self.value)

    def insert(self, e):
        """assumes e is an integer and inserts e into instance"""
        if e not in self.value[self.hash_elem(e)]:
            self.value[self.hash_elem(e)].append(e)

    def member(self, e):
        """assumes e is an integer
        return True if e is in instance, and False otherwise
        """
        return e in self.value[self.hash_elem(e)]

    def __str__(self):
        """returns a string representation of self"""
        elems = []
        for bucket in self.value:
            for e in bucket:
                elems.append(e)
        elems.sort()
        return "{" + str(elems) + "}"
