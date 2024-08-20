from Binary_Tree import Binary_Tree

class Seq_Binary_Tree(Binary_Tree):
    def __init__(self):
        super().__init__(10)  # Replace 10 with the appropriate value for Size_Node)

    def build(self, X):
        A = [x for x in X]
        def build_subtree(X, i, j):
            c = (i + j) // 2
            root = self.Node_Type(A[c])
            if i < c:
                root.left = build_subtree(X, i, c - 1)
                root.left.parent = root
            if c < j:
                root.right = build_subtree(X, c + 1, j)
                root.right.parent = root
            root.subtree_update()
            return root

        self.root = build_subtree(X, 0, len(X) - 1)
        self.size = self.root.size

    def get_at(self, i):
        assert self.root
        return self.root.subtree_at(i).item

    def set_at(self, i, x):
        assert self.root
        self.root.subtree_at(i).item = x

    def insert_at(self, i, x):
        new_node = self.Node_Type(x)
        if i == 0:
            if self.root:
                node = self.root.subtree_first()
                node.subtree_insert_before(new_node)
            else:
                self.root = new_node
        else:
            node = self.root.subtree_at(i - 1)
            node.subtree_insert_after(new_node)
        self.size += 1

    def delete_at(self, i):
        assert self.root
        node = self.root.subtree_at(i)
        ext = node.subtree_delete()
        if ext.parent is None:
            self.root = None
        self.size -= 1

    def insert_first(self, x):
        self.insert_at(0, x)

    def delete_first(self):
        return self.delete_at(0)

    def insert_last(self, x):
        self.insert_at(len(self), x)

    def delete_last(self):
        return self.delete_at(len(self) - 1)
