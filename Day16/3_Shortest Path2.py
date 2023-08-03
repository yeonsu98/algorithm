INF = 987654321     # 무한 비용

def getSmall(dp, visited, n) :
    minValue = INF
    index = 0       # 찾은 노드 위치

    for i in range(1, n) :      # 1 ~ 6노드를 반복
        if dp[i] < minValue and not visited[i] :
            minValue = dp[i]
            index = i

    return index

def dijkstra(graph, start, n) :
    visited = [False] * n       # 방문 테이블
    dp = [INF] * n              # DP 테이블 (= 최소 비용을 저장)

    dp[start] = 0
    visited[start] = True

    for fri in graph[start] :   #   0     1
        dp[fri[0]] = fri[1]     # (노드, 비용)

    for i in range(n - 2) :             # 시작 노드를 제외한 나머지 노드 처리
        now = getSmall(dp, visited, n)  # 방문하지 않은 노드 중 최소 비용의 노드
        visited[now] = True

        for j in graph[now] :
            cost = dp[now] + j[1]

            if cost < dp[j[0]] :
                dp[j[0]] = cost

    return dp    

graph = [
    [],
    [(2,2), (3,5), (4,1)],  # 1    ※ (노드, 비용)
    [(3,3), (4,2)],         # 2
    [(2,3), (6,5)],         # 3
    [(3,3), (5,1)],         # 4
    [(3,1), (6,2)],         # 5
    []                      # 6
]

start = 1           # 시작 노드
n = len(graph)      # 노드 개수 (= 6)

dis = dijkstra(graph, start, n)

print(dis)