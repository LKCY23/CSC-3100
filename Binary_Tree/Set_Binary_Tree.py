from Binary_Tree.Binary_Tree import Binary_Tree
from BST_Node import BST_Node

class Set_Binary_Tree(Binary_Tree): # (AVL_Binary_Node)
    # 初始化集合二叉树
    def __init__(self):
        super().__init__(BST_Node)

    # 迭代器，以中序遍历返回树中的所有元素
    def iter_order(self):
        # need __iter__ in Binary_Tree
        yield from self

    # 构建树，通过插入列表X中的每个元素 
    # X will be constructed to a set binary tree, but if X is sorted, it will be a binary search tree with one branch
    def build(self, X):
        for x in X:
            self.insert(x)

    # 查找最小元素
    def find_min(self):
        if self.root:
            return self.root.subtree_first().item

    # 查找最大元素
    def find_max(self):
        if self.root:
            return self.root.subtree_last().item

    # 查找键为k的元素
    def find(self, k):
        if self.root:
            node = self.root.subtree_find(k)
            if node:
                return node.item

    # 查找大于k的最小元素
    def find_next(self, k):
        if self.root:
            node = self.root.subtree_find_next(k)
            if node:
                return node.item

    # 查找小于k的最大元素
    def find_prev(self, k):
        if self.root:
            node = self.root.subtree_find_prev(k)
            if node:
                return node.item

    # 插入元素x
    def insert(self, x):
        new_node = self.Node_Type(x)
        if self.root:
            self.root.subtree_insert(new_node)
            if new_node.parent is None:
                return False
        else:
            self.root = new_node
            self.size += 1
        return True

    # 删除键为k的元素
    def delete(self, k):
        assert self.root
        node = self.root.subtree_find(k)
        assert node
        ext = node.subtree_delete()
        if ext.parent is None:
            self.root = None
        self.size -= 1
        return ext.item
