from Binary_Node import Binary_Node

class Binary_Tree:
    def __init__(self, Node_Type = Binary_Node):
        self.root = None
        self.size = 0
        self.Node_Type = Node_Type

    def __len__(self):
        return self.size

    def __iter__(self):
        if self.root:
            for A in self.root.subtree_iter(): # method in Binary_Node
                yield A.item
    
    def build(self, X):
        A = [x for x in X]
    
        def build_subtree(A, i, j):
            c = (i + j) // 2
            root = self.Node_Type(A[c])
            if i < c:  # 需要在左子树中存储更多元素
                root.left = build_subtree(A, i, c - 1)
                root.left.parent = root
            if c < j:  # 需要在右子树中存储更多元素
                root.right = build_subtree(A, c + 1, j)
                root.right.parent = root
            return root
        # if i > j, return c node
        # if i == j, return the node 

        self.root = build_subtree(A, 0, len(A)-1)

    def tree_iter(self):
        node = self.subtree_first()
        while node:
            yield node
            node = node.successor()
    
# 1. 基于节点的 __iter__ 方法
# 这种遍历方法通常是实现为中序遍历（In-order traversal），这样可以返回一个有序的节点序列，假设树是一个二叉搜索树（BST）。这种遍历方式的特点是：

# 有序性：对于BST来说，中序遍历会按照键的升序返回节点，这对于很多需要有序数据的操作非常重要，如范围查询、有序列表的创建等。
# 递归实现：通常使用递归来实现，代码易于理解和实现。
# 使用场景：适用于需要访问整棵树的所有节点，并且需要节点有序（如果树是BST的话）的场景。

# 2. 基于最左侧元素的 tree_iter 方法
# 这种遍历方法更类似于迭代器模式，它从树的最左侧元素开始，利用树的结构特性（如每个节点链接到其后继节点），逐个返回节点。这种方法的特点是：

# 非递归：通常不使用递归，而是利用树的物理结构和链接（如父节点和后继链接）来进行迭代，这可以避免递归带来的栈溢出风险和额外的调用开销。
# 空间效率：因为不需要递归调用栈，所以对内存的使用更加高效，特别是在处理非常大的数据集时。
# 使用场景：适用于需要从最小元素开始逐个访问节点的场景，特别是在需要顺序处理或实时处理每个元素时。

