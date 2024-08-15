def direct_access_sort(A):
    """Sort A assuming items have distinct non-negative keys"""
    u = 1 + max([x.key for x in A])  # O(n) find maximum key
    D = [None] * u  # O(u) direct access array
    for x in A:  # O(n) insert items
        D[x.key] = x
    i = 0
    for key in range(u):  # O(u) read out items in order
        if D[key] is not None:
            A[i] = D[key]
            i += 1
    return A
# complexity: O(n + u) time, O(u) space