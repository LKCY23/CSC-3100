from Priority_Queue_Basic import PriorityQueue

class PQ_Heap(PriorityQueue):
    def insert(self, *args): # O(log n)
        super().insert(*args) # 在数组末尾添加元素
        n, A = self.n, self.A
        PQ_Heap.max_heapify_down(A, n, 0)

    def delete_max(self): # O(log n)
        n, A = self.n, self.A
        A[0], A[n] = A[n], A[0]
        PQ_Heap.max_heapify_down(A, n, 0)
        return super().delete_max() # 从数组末尾弹出元素

    @staticmethod
    def parent(i):
        p = (i - 1) // 2
        return p if 0 < i else i

    @staticmethod
    def left(i, n):
        l = 2 * i + 1
        return l if l < n else i

    @staticmethod
    def right(i, n):
        r = 2 * i + 2
        return r if r < n else i

    @staticmethod
    def max_heapify_up(A, n, c): # T(c) = O(log c)
        p = PQ_Heap.parent(c) # 获取父节点索引
        if A[p].key < A[c].key: # 比较
            A[c], A[p] = A[p], A[c] # 交换父节点
            PQ_Heap.max_heapify_up(A, n, p) # 递归向上调整

    @staticmethod # down is more powerful than up
    def max_heapify_down(A, n, p): # T(p) = O(log n - log p)
        l, r = PQ_Heap.left(p, n), PQ_Heap.right(p, n) # 获取子节点索引
        c = l if A[r].key < A[l].key else r # 选择较大的子节点
        if A[p].key < A[c].key: # 比较
            A[c], A[p] = A[p], A[c] # 交换子节点
            PQ_Heap.max_heapify_down(A, n, c) # 递归向下调整

    @staticmethod
    def build_max_heap(A):
        n = len(A)
        for i in range(n // 2, -1, -1): # O(n) loop backward over array
            PQ_Heap.max_heapify_down(A, n, i) # O(log n - log i)) fix max heap property

if __name__ == '__main__':
    class KeyData:
        def __init__(self, key, data):
            self.key = key
            self.data = data

    # Call the static method
    A = [KeyData(4, 'data1'), KeyData(10, 'data2'), KeyData(3, 'data3'), KeyData(5, 'data4'), KeyData(1, 'data5')]
    PQ_Heap.build_max_heap(A)
    print([item.key for item in A])  # Output: [10, 5, 3, 4, 1]

    pqheap = PQ_Heap()  # Create a PQ_Heap object
    pqheap.A = A  # Set pqheap's A attribute to A
    pqheap.n = len(A)  # Set pqheap's n attribute to the length of A
    pqheap.insert(*A)  # Insert all elements from A into pqheap using the insert method
    print([item.key for item in pqheap.A])  # Output: [10, 5, 3, 4, 1, 7]
    print(pqheap.n)