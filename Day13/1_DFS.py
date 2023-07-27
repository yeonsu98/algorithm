# 자료 구조 stack 사용

def dfs(graph, node, visited):
    visited[node]=True      # 현재 받은 노드는 바로 방문처리
    print(node, end=" ")

    for i in graph[node]: # 현재 노드의 인접한 노드를 순서대로 반복
        if visited[i] == False:     # 현재 인접 노드가 방문한 적이 없으면 
            dfs(graph, i, visited)  # 재귀로 진입한다. 

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

dfs(graph, 8, visited) # 그래프, 시작노드

# 81276345