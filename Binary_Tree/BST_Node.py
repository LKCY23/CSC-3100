from Binary_Node import Binary_Node

class BST_Node(Binary_Node):
    # 在子树中查找键值为k的节点
    def subtree_find(self, k):
        if k < self.item.key:
            if self.left:
                return self.left.subtree_find(k)
            else:
                return None
        elif k > self.item.key:
            if self.right:
                return self.right.subtree_find(k)
            else:
                return None
        else:
            return self

    # 在子树中查找下一个大于或等于k的节点
    def subtree_find_next(self, k):
        if self.item.key <= k:
            if self.right:
                return self.right.subtree_find_next(k)
            else:
                return None
        elif self.left:
            B = self.left.subtree_find_next(k)
            if B:
                return B
            else:
                return self

    # 在子树中查找上一个小于或等于k的节点
    def subtree_find_prev(self, k):
        if self.item.key >= k:
            if self.left:
                return self.left.subtree_find_prev(k)
            else:
                return None
        elif self.right:
            B = self.right.subtree_find_prev(k)
            if B:
                return B
            else:
                return self

    # 向子树中插入节点
    def subtree_insert(self, B):
        if B.item.key < self.item.key:
            if self.left:
                self.left.subtree_insert(B)
            else:
                self.subtree_insert_before(B)
        elif B.item.key > self.item.key:
            if self.right:
                self.right.subtree_insert(B)
            else:
                self.subtree_insert_after(B)
        else:
            # if key is the same, replace the item
            self.item = B.item
