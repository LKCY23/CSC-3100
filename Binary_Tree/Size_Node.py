from Binary_Node import Binary_Node

class Size_Node(Binary_Node):
    def __init__(self, x):
        super().__init__(x)
        self.size = 1

    def subtree_update(self):  # O(1)
        super().subtree_update()
        self.size = 1
        if self.left:
            self.size += self.left.size
        if self.right:
            self.size += self.right.size

    def subtree_at(self, i):  # O(h)
        assert 0 <= i
        if self.left:
            L_size = self.left.size
        else:
            L_size = 0
        if i < L_size:
            return self.left.subtree_at(i)
        elif i > L_size:
            return self.right.subtree_at(i - L_size - 1)
        else:
            return self