ice = [
    [0, 0, 1, 1, 0],
    [0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0]
]

def bfs(graph, src):
    queue = [src]
    visited = {src}

    while queue : 
        node = queue.pop(0)
        print(node)
        for fri in graph[node]:
            if fri not in visited:
                queue.append(fri)
                visited.add(fri)
                

# 이동 가능한 좌표 파악 
def getNodeList(graph):
    nodeList = []

    for x in range(len(graph)):
        for y in range(len(graph)):
            if graph[x][y] == 0:
                nodeList.append((x,y))

    return nodeList

# 서로 인접한 노드인지 파악
def isNear(first, second):
    # x는 고정, y가 1차이. 즉, 좌우 한 칸 차이
    flag = (first[0] == second[0]) and (abs(first[1] - second[1]) == 1)

    # y는 고정, x가 1차이. 즉, 상하 한 칸 차이
    flag1 = (first[1] == second[1]) and (abs(first[0] - second[0]) == 1)

    # 둘 중 하나가 참일 때 (동시에 참일 순 없음 -> 대각선)
    return flag or flag1

def getNodeGraph(nodeList):

    graph = {}
    
    # 1. 그래프 초기화
    for n in nodeList:
        graph[n] = []

    # 2. 인접한 항목을 그래프에 추가
    for k, v in graph.items():
        #print(f"{k} : {v}")
        for node in nodeList:
            if isNear(k, node): # 현재 좌표와 node가 인접한 지 보기
                v.append(node)

    return graph

nodeList = getNodeList(ice)
graph = getNodeGraph(nodeList)

for n in nodeList:
    src = n
    bfs(graph, src)
    print()