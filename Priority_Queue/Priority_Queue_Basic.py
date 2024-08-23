class PriorityQueue:
    def __init__(self):
        self.A = []
        self.n = 0

    def insert(self, *args):
        for i in args:
            self.A.append(i)
            self.n += 1

    def delete_max(self):
        if len(self.A) < 1:
            raise IndexError('pop from empty priority queue')
        return self.A.pop() # NOT correct on its own!

    @classmethod # class method. No need to create an instance of the class to use this method.
    def sort(Queue, A):
        pq = Queue() # make empty priority queue
        for x in A: # n x T_insert
            pq.insert(x)
        out = [pq.delete_max() for _ in A] # n x T_delete_max
        out.reverse()
        return out