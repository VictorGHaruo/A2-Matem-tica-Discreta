

from collections import deque, defaultdict

def bfs (graph, mU, mV, dist, n):
    queue = deque()
    k = float('inf')
    for u in range(n):
        if mU[u] == -1:
            dist[u] = 0
            queue.append(u)
        else:
            dist[u] = float('inf')
    augmenting_path = False

    while queue:
        u = queue.popleft()
        if dist[u] < k:
            for v in graph[u]:
                if mV[v] == -1 and k == float('inf'):
                    k = dist[u] + 1
                    augmenting_path = True
                else:
                    if dist[mV[v]] == float('inf'):
                        dist[mV[v]] = dist[u] + 1
                        queue.append(mV[v])
    return augmenting_path

def dfs(graph, mU, mV, v, dist):
    for u in graph[v]:
        if mV[u] == -1:
            mU[v] = u
            mV[u] = v
            return True
        
        if dist[mV[u]] == dist[v] + 1:
            if dfs(graph, mU, mV, mV[u], dist) == True:
                mU[v] = u
                mV[u] = v
                return True
    dist[v] = float('inf')
    return False

def max_match(graph, m,n):
    dist = [0]*n 
    mU = [-1]*n
    mV = [-1]*m

    match_size = 0
    while bfs(graph, mU, mV, dist, n):
        for u in range(n):
            if mU[u] == -1 and dfs(graph, mU, mV, u, dist):
                match_size = match_size + 1
    return mU, mV, match_size

def links (mU, U, V): 
    for i,u in enumerate(U):
        if mU[i] + 1 == 0:
            print("Vértice não emparelhado")
        else:    
            print (f"{u} emparelhado com {mU[i]+1}")

if __name__ == "__main__":

    U = {
        "A": ["1", "2", "4"],
        "B": ["2", "6"],
        "C": ["2", "3"],
        "D": ["3", "5", "6"],
        "E": ["3", "4", "5", "6"],
        "F": ["2", "5"]}
    V = {
        "1": ["A"],
        "2": ["A", "B", "C", "E"],
        "3": ["C", "D", "E"],
        "4": ["A", "E"],
        "5": ["D", "E", "F"],
        "6": ["B", "D", "E"]
        }
    

    graph = defaultdict(list)
    U_keys = list(U.keys())
    V_keys = list(V.keys())
   
    for i, u in enumerate(U_keys):
        for v in U[u]:
            j = V_keys.index(v) 
            graph[i].append(j)

    n = len(U) 
    m = len(V) 

    mU, mV, match_size = max_match(graph, m, n)

    links(mU,U, V)