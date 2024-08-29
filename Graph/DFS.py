def dfs(Adj, s, parent=None, order=None):  # Adj: adjacency list, s: start
    if parent is None:  # O(1) initialize parent list
        parent = [None for v in Adj]  # O(V) (use hash if unlabeled)
    parent[s] = s  # O(1) root
    order = []  # O(1) initialize order array
    for v in Adj[s]:  # O(Adj[s]) loop over neighbors
        if parent[v] is None:  # O(1) parent not yet assigned
            parent[v] = s  # O(1) assign parent
        dfs(Adj, v, parent, order)  # Recursive call
    order.append(s)  # O(1) amortized
    return parent, order

def full_dfs(Adj):  # Adj: 邻接列表
    parent = [None for v in Adj]  # O(V)（如果未标签化，使用哈希）
    order = []  # O(1) 初始化顺序列表
    for v in range(len(Adj)):  # O(V) 遍历顶点
        if parent[v] is None:  # O(1) 父节点尚未分配
            parent[v] = v  # O(1) 分配自身为父节点（根）
            dfs(Adj, v, parent, order)  # 从v开始的DFS（也可以使用BFS）
    return parent, order

def dfs_detector(Adj, s, parent=None, ancestors=None, order=None, back_edges=None):
    if parent is None:  # 初始化父指针列表
        parent = [None] * len(Adj)
    if ancestors is None:  # 初始化祖先集合
        ancestors = set()
    if order is None:  # 初始化访问顺序列表
        order = []
    if back_edges is None:  # 初始化回边列表
        back_edges = []

    parent[s] = s  # 将起始点标为自己的父节点（根）
    ancestors.add(s)  # 将当前顶点加入祖先集合
    for v in Adj[s]:  # 遍历当前顶点的所有邻居
        if parent[v] is None:  # 如果邻居未被访问
            parent[v] = s  # 分配父节点
            dfs(Adj, v, parent, ancestors, order, back_edges)  # 递归访问
        elif v in ancestors:  # 如果邻居已在祖先集合中，标记为回边
            back_edges.append((s, v))
    order.append(s)  # 添加当前顶点到访问顺序
    ancestors.remove(s)  # 从祖先集合中移除当前顶点

    return parent, order, back_edges

def dfs_topological_sort(Adj, s, parent=None, order=None):
    if parent is None:  # 初始化父指针列表
        parent = [None] * len(Adj)
    if order is None:  # 初始化顶点顺序列表
        order = []

    parent[s] = s  # 将起始点标记为自己的父节点
    for v in Adj[s]:  # 遍历当前顶点的所有邻居
        if parent[v] is None:  # 如果邻居未被访问
            parent[v] = s  # 标记当前顶点为该邻居的父节点
            dfs_topological_sort(Adj, v, parent, order)  # 递归访问

    order.append(s)  # 在递归结束后添加当前顶点到顺序列表

def topological_sort(Adj):
    order = []  # 存储最终的拓扑排序
    parent = [None] * len(Adj)  # 跟踪每个顶点的父顶点

    for s in range(len(Adj)):  # 对每个顶点进行DFS
        if parent[s] is None:  # 如果顶点未被访问
            dfs_topological_sort(Adj, s, parent, order)

    return order[::-1]  # 逆序返回结果，因为DFS是反拓扑排序


if __name__ == "__main__":
    Adj = {}
    for i in Adj:
        print(i)
    print(full_dfs(Adj))  # Output: ([0, 0, 0, 1, 1], [1, 3, 4, 2, 0])
    print(dfs(Adj, 0))  # Output: ([1, 1, 1, 1, 1], [3, 4, 1, 2, 0])
    