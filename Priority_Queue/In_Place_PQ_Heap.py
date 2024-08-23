from PQ_Heap import PQ_Heap

class PriorityQueue(PQ_Heap):
    def __init__(self, A):
        self.A = A
        self.n = 0
        # self.build_max_heap()
        
    def insert(self): # absorb element A[n] into the queue
        if not self.n < len(self.A):
            raise IndexError('insert into full priority queue')
        self.n += 1
        self.max_heapify_up(self.A, self.n, self.n - 1)

    def delete_max(self): # remove element A[n - 1] from the queue
        if self.n < 1:
            raise IndexError('pop from empty priority queue')
        self.A[0], self.A[self.n - 1] = self.A[self.n - 1], self.A[0]
        self.n -= 1 # NOT correct on its own!
        self.max_heapify_down(self.A, self.n, 0)

    @classmethod
    def sort(Queue, A):
        pq = Queue(A) # make empty priority queue
        for i in range(len(A)): # n x T_insert
            pq.insert()
        for i in range(len(A)): # n x T_delete_max
            pq.delete_max()
        return pq.A

if	__name__ == '__main__':
    class KeyData:
        def __init__(self, key, data):
            self.key = key
            self.data = data

    # Call the static method
    A = [KeyData(4, 'data1'), KeyData(10, 'data2'), KeyData(3, 'data3'), KeyData(5, 'data4'), KeyData(1, 'data5')]
    A = PriorityQueue.sort(A)
    print([item.key for item in A])  # Output: [10, 5, 3, 4, 1]