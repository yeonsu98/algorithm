# ex03.png 그래프의

# 1. DFS 결과를 출력
def dfs(graph, node, visited):
    visited[node] = True

    print(node)

    for i in graph[node]:
        if visited[i] == False:
            dfs(graph, i, visited)

# 2. BFS 결과를 출력
def bfs(graph, node, visited):
    queue = [node]
    visited[node] = True

    while queue:
        node = queue.pop(0)
        print(node)

        for i in graph[node]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True


graph = [
    [1, 3],
    [0, 2, 5],
    [2, 3, 4, 5],
    [0, 1, 2, 4],
    [2, 3, 6],
    [1, 2],
    [1, 4]
]

visited = [False] * 7
dfs(graph, 1, visited)
print()
visited = [False] * 7
bfs(graph, 1, visited)