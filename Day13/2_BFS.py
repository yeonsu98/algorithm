# BFS : Breadth-First Search
# - 너비 우선 탐색
# - 가까운 노드부터 우선 탐색
# - 길 찾기 같은 구문에 많이 사용
# - 자료구조 Queue를 사용

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
    [],             # 0번 노드는 없어서 비운다
    [2, 3, 8],      # 1번 노드
    [1, 7],         # 2번 노드
    [1, 4, 5],      # 3번 노드
    [3, 5],         # 4번 노드
    [3, 4],         # 5번 노드
    [7],            # 6번 노드
    [2, 6, 8],      # 7번 노드
    [1, 7]          # 8번 노드
]

visited = [False] * 9
bfs(graph, 2, visited)

