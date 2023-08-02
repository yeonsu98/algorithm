def printMaze(maze):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            n = maze[i][j]

            if n == 1: n = "▤"
            if n == 0 : n = " "
            if n == 2 : n = "♤"
            if n == 3 : n = "·"

            print(n, end=" ")
        print()
    print()

# 이동 가능한 좌표 파악 
def getNodeList(maze):
    nodeList = []

    for x in range(len(maze)):
        for y in range(len(maze)):
            if maze[x][y] == 0:
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

# 인접한 node끼리 등록된 graph를 만들어 반환
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

# 입구 찾기 : 제일 위(i==0)이거나 제일 좌측(j==0)에서 0인 곳
def findSource(graph):
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            point = (i == 0 or j == 0)
            value = (graph[i][j] == 0)
            if point and value: 
                return (i, j)
                        
# 출구 찾기 : 제일 위(i==n)이거나 제일 좌측(j==m)에서 0인 곳
def findDestination(graph):
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            point = (i == len(graph)-1) or (j == len(graph[i])-1)
            value = (graph[i][j] == 0)
            if point and value:
                return (i, j)

# bfs 적용
import os
import time as t      
def bfs(graph, src, dst, maze):
    queue = [src]
    visited = {src}

    while queue:
        node = queue.pop(0)

        # 좌표 이동
        x, y = node
        maze[x][y] = 2

        t.sleep(0.2)
        os.system("clear")
        printMaze(maze)


        for fri in graph[node]:
            if fri not in visited:
                maze[x][y] = 3
                queue.append(fri)
                visited.add(fri)
            
# 역추적 테이블 적용해서 bfs
import os
import time as t      
def bfs2(graph, src, dst, maze):
    queue = [src]
    visited = {src}

    parents = {}

    for key in graph.keys():
        parents[key] = (0,0)

    while queue:
        node = queue.pop(0)

        for fri in graph[node]:
            if fri not in visited:
                queue.append(fri)
                visited.add(fri)

                parents[fri] = node
        
    # 경로 추적
    trace = []
    cur = dst

    while cur != src:
        trace.append(cur)
        cur = parents[cur]

    trace.append(src)
    trace.reverse()

    return trace

def printPath(maze, path):
    for x,y in path:
        t.sleep(0.1)
        os.system("clear")

        maze[x][y] = 2
        printMaze(maze)
        maze[x][y] = 3