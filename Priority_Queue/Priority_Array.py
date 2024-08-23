from Priority_Queue_Basic import PriorityQueue

class PQ_Array(PriorityQueue): # selection sort
    # PriorityQueue.insert already correct: appends to end of self.A
    def delete_max(self): # O(n)
        n, A, m = len(self.A), self.A, 0
        for i in range(1, n):
            if A[m].key < A[i].key:
                m = i
        A[m], A[n] = A[n], A[m] # swap max with end of array
        return super().delete_max() # pop from end of array

class PQ_SortedArray(PriorityQueue): # insertion sort
    # PriorityQueue.delete_max already correct: pop from end of self.A
    def insert(self, *args): # O(n)
        super().insert(*args) # append to end of array
        i, A = len(self.A) - 1, self.A # restore array ordering
        while 0 < i and A[i + 1].key < A[i].key:
            A[i + 1], A[i] = A[i], A[i + 1]
            i -= 1
