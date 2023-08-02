# 미로 그림 출력
def printMaze(maze) :
    for i in range(len(maze)) :
        for j in range(len(maze[i])) :
            n = maze[i][j]

            if n == 1: n = "▤"
            if n == 0 : n = " "
            if n == 2 : n = "♤"
            if n == 3 : n = "·"

            print(n, end = "")
        
        print()
    print()


# 이동 가능한 좌표 파악
def getNodeList(maze) :
    nodeList = []

    for x in range(len(maze)) :
        for y in range(len(maze[x])) :
            if maze[x][y] == 0 :
                nodeList.append((x, y))

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


# 제일 위(i == 0)이거나 제일 좌측(j == 0)에서 0인 곳
def findSource(maze) :
    for i in range(len(maze)) :
        for j in range(len(maze[i])) :
            point = (i == 0 or j == 0)
            value = maze[i][j] == 0

            if point and value :
                return (i, j)

# 제일 아래(i == n)이거나 제일 우측(j == m)에서 0인 곳
def findDestination(maze) :
    for i in range(len(maze)) :
        for j in range(len(maze[i])) :
            point = (i == len(maze) - 1 or j == len(maze[i]) - 1)
            value = maze[i][j] == 0

            if point and value :
                return (i, j)

import os
import time as t

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
    trace.reverse()

    return trace

def printPath(maze, path) :
    for x, y in path :
        t.sleep(0.1)
        os.system("clear")

        maze[x][y] = 2
        printMaze(maze)
        maze[x][y] = 3



