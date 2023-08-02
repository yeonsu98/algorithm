
def dfs(graph, i, j):
    global n, m
    if i < 0 or j < 0 or i >= n or j >= m:
        return False
    
    if graph[i][j] == 0:
        graph[i][j] = 1     # 1로 바꾸어 방문 처리

        dfs(graph, i-1, j)  # 상
        dfs(graph, i+1, j)  # 하
        dfs(graph, i, j-1)  # 좌
        dfs(graph, i, j+1)  # 우
        return True
    return False

n, m = map(int, input().split())

graph = []
result = 0

for i in range(n):
    line = list(map(int, input().split()))
    graph.append(line)

for i in range(n):
    for j in range(m):
        if dfs(graph, i, j):
            result += 1

print(f"아이스크림의 개수는 {result}개이다")


            
            