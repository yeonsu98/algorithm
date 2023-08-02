# 미로 찾기
# step 7 : 다른 미로에 적용

import maze as m

maze = [
    [1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1],
    [1,0,0,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,0,1],
    [1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,0,1],
    [1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1]
]


nodeList = m.getNodeList(maze)      # 0값 좌표 리스트
graph = m.getNodeGraph(nodeList)    # 인접 그래프

src = m.findSource(maze)            # 출발지
dst = m.findDestination(maze)       # 목적지

path = m.bfs(graph, src, dst, maze)
m.printPath(maze, path)

path.reverse()
m.printPath(maze, path)