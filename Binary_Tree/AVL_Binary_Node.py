class Binary_Node:
    def __init__(self, x):
        self.item = x
        self.left = None
        self.right = None
        self.parent = None
        self.height_value = 0
        self.subtree_update()

    def height(self): # O(1)
        if self:
            return self.height_value
        else:
            return -1

    def subtree_update(self): # O(1)
        self.height_value = 1 + max(self.left.height(), self.right.height())

    def skew(self): # O(1)
        return self.right.height() - self.left.height()

    def subtree_iter(self): # O(n)
        if self.left:
            yield from self.left.subtree_iter()
        yield self
        if self.right:
            yield from self.right.subtree_iter()

    def subtree_first(self): # O(logn)
        if self.left:
            return self.left.subtree_first()
        else:
            return self

    def subtree_last(self): # O(logn)
        if self.right:
            return self.right.subtree_last()
        else:
            return self

    def successor(self): # O(logn)
        if self.right:
            return self.right.subtree_first()
        while self.parent and (self is self.parent.right):
            self = self.parent
        return self.parent

    def predecessor(self): # O(logn)
        if self.left:
            return self.left.subtree_last()
        while self.parent and (self is self.parent.left):
            self = self.parent
        return self.parent

    def subtree_insert_before(self, B): # O(logn)
        if self.left:
            self = self.left.subtree_last()
            self.right, B.parent = B, self
        else:
            self.left, B.parent = B, self
        self.maintain()

    def subtree_insert_after(self, B): # O(logn)
        if self.right:
            self = self.right.subtree_first()
            self.left, B.parent = B, self
        else:
            self.right, B.parent = B, self
        self.maintain()

    def subtree_delete(self): # O(logn)
        if self.left or self.right:
            if self.left:
                B = self.predecessor()
            else:
                B = self.successor()
            self.item, B.item = B.item, self.item
            return B.subtree_delete()
        if self.parent:
            if self.parent.left is self:
                self.parent.left = None
            else:
                self.parent.right = None
            self.parent.maintain()
        return self

    def subtree_rotate_right(self): # O(1)
        assert self.left
        B, E = self.left, self.right
        A, C = B.left, B.right
        self, B = B, self
        self.item, B.item = B.item, self.item
        B.left, B.right = A, self
        self.left, self.right = C, E
        if A: A.parent = B
        if E: E.parent = self
        B.subtree_update()
        self.subtree_update()

    def subtree_rotate_left(self):
        assert self.right
        A, D = self.left, self.right
        C, E = D.left, D.right
        self, D = D, self
        self.item, D.item = D.item, self.item
        D.left, D.right = self, E
        self.left, self.right = A, C
        if A: A.parent = self
        if E: E.parent = D
        self.subtree_update()
        D.subtree_update()

    def rebalance(self):
        if self.skew() == 2:
            if self.right.skew() < 0:
                self.right.subtree_rotate_right()
            self.subtree_rotate_left()
        elif self.skew() == -2:
            if self.left.skew() > 0:
                self.left.subtree_rotate_left()
            self.subtree_rotate_right()

    def maintain(self):
        self.rebalance()
        self.subtree_update()
        if self.parent:
            self.parent.maintain()
