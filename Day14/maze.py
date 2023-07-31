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