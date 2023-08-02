# nodeList 파악
def getNodeList(maze):
    nodeList = []

    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 1:
                nodeList.append((i, j))
    return nodeList

# 두 좌표가 인접한지 파악
def isNear(first, second) :
    # x는 고정, y가 1차이. 즉, 좌우 한칸 차이
    flag1 = (first[0] == second[0]) and abs(first[1] - second[1]) == 1

    # y는 고정, x가 1차이. 즉, 상하 한칸 차이
    flag2 = (first[1] == second[1]) and abs(first[0] - second[0]) == 1

    return flag1 or flag2

# 인접항 node끼리 등록된 grpah를 만들어 반환
def getNodeGraph(nodeList) :
    graph = {}

    # 1. 그래프 초기화
    for n in nodeList :
        graph[n] = []

    # 2. 인접한 항목을 그래프에 추가
    for k, v in graph.items() :
        for node in nodeList :
            if isNear(k, node) :
                v.append(node)

    return graph

def bfs(graph, src, dst, maze) :
    queue = [src]
    visitid = {src}

    parents = {}    # 역추적할 부모 테이블

    for k in graph.keys() :     # 부모 테이블 초기화
        parents[k] = (0, 0)

    while queue :
        node = queue.pop(0)
    
        for fri in graph[node] :
            if fri not in visitid :
                queue.append(fri)
                visitid.add(fri)

                parents[fri] = node

    trace = []
    cur = dst

    while cur != src :
        trace.append(cur)
        cur = parents[cur]

    trace.append(src)

    return len(trace)


    # 상  하  좌  우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs_teacher(graph, x, y):
    queue = [(x, y)]

    while queue : 
        x, y = queue.pop(0)

        for i in range(4):
            nx = x + dx
            ny = y + dy

            # 맵 밖의 범위
            if nx < 0 or ny < 0 or nx >= n or ny >= m :
                continue
            # 괴물의 위치
            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

n, m = map(int, input().split())

maze = []

for i in range(n):
    line = list(map(int, input()))
    maze.append(line)
# print(maze)

src = (0, 0)
dst = (n-1, m-1)
nodeList = getNodeList(maze)

graph = getNodeGraph(nodeList)
minDist = bfs(graph, src, dst, maze)
print("최소이동거리 : ", minDist)