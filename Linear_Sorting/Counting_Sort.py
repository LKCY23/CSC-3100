# using chain of items with the same key
def counting_sort(A):
    # Sort A assuming items have non-negative keys
    u = 1 + max([x.key for x in A])  # O(n)
    D = [[] for _ in range(u)]  # O(u)

    for x in A:
        D[x.key].append(x)

    i = 0
    for chain in D:  # O(u) read out items in order
        for x in chain:
            A[i] = x
            i += 1
    return A
# complexity: O(n + u) time, O(n + u) space

# using cumulative sums
def counting_sort(A):
    # Sort A assuming items have non-negative keys
    u = 1 + max([x.key for x in A])  # O(n) find maximum key
    D = [0] * u  # O(u) direct access array

    for x in A:
        D[x.key] += 1  # O(n) count keys

    for k in range(1, u):
        D[k] += D[k - 1]  # O(u) cumulative sums

    # Visualized example:
    # Suppose we have an array A = [2, 4, 1, 3, 2]
    # After counting the keys, D = [0, 1, 2, 1, 1, 0]
    # Then, after applying cumulative sums, D = [0, 1, 3, 4, 5, 5]
    # The cumulative sums represent the ending indices of each key in the sorted array
    # This allows us to easily determine the correct position of each element in the sorted array


    for x in list(reversed(A)): # preserve stability, because D marks the ending index of each key 
        A[D[x.key] - 1] = x  # O(n) move items into place
        D[x.key] -= 1

    return A


def radix_sort(A):
    # Sort A assuming items have non-negative keys
    n = len(A)
    u = 1 + max([x.key for x in A])  # O(n) find maximum key
    c = 1 + (u.bit_length() // n.bit_length()) # why bit_length? why not u//n?

    # import math
    # c = 1 + (math.log10(u) // math.log10(n))
    
    class Obj:
        def __init__(self, key, digits, item):
            self.key = key
            self.digits = digits
            self.item = item

    D = [Obj(None, None, None) for _ in A]

    for i in range(n):  # O(nc) make digit tuples
        D[i].digits = []
        D[i].item = A[i]
        high = A[i].key
        for j in range(c):  # O(c) make digit tuple
            high, low = divmod(high, n)
            D[i].digits.append(low)
        # the element in D[i].digits is the digit of the key of A[i] from the least significant to the most significant

    for i in range(c):  # O(nc) sort each digit
        for j in range(n):  # O(n) assign key i to tuples
            D[j].key = D[j].digits[i]
        counting_sort(D)  # O(n) sort on digit i

    for i in range(n):  # O(n) output to A
        A[i] = D[i].item

    return A



