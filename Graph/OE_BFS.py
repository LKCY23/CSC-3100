from collections import deque

def create_modified_graph(V, E):
    V0 = {v + suffix for v in V for suffix in ('E', 'O')}
    E0 = []
    for (u, v) in E:
        E0.append((u + 'E', v + 'O'))
        E0.append((u + 'O', v + 'E'))
    return V0, E0

def bfs(Adj, start, target):
    queue = deque([start])
    parents = {start: None}
    visited = {start}
    print(queue)
    while queue:
        current = queue.popleft()
        if current == target:
            break
        for neighbor in Adj[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                parents[neighbor] = current
                queue.append(neighbor)
    if target not in parents:
        return None
    path = []
    step = target
    while step is not None:
        path.append(step)
        step = parents[step]
    return path[::-1]

if __name__ == '__main__':

    # Example graph G
    V = {'s', 'a', 'b', 't'}
    E = {('s', 'a'), ('a', 'b'), ('b', 't'), ('s', 't')}

    # Construct G0
    V0, E0 = create_modified_graph(V, E)
    Adj = {v: [] for v in V0}
    for u, v in E0:
        Adj[u].append(v)
        Adj[v].append(u)  # Because the graph is undirected

    # Find shortest odd path from s to t
    path = bfs(Adj, 'sE', 'tO')
    print("Shortest odd path from s to t:", path)

