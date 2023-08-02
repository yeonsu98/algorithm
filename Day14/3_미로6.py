# 미로 찾기
# step 6 : 준비 끝 bfs 진행

import maze as m

maze = [
    [1,0,1,1,1],
    [1,0,1,0,0],
    [1,0,1,0,1],
    [1,0,0,0,1],
    [1,1,1,1,1]
]

m.printMaze(maze)

nodeList = m.getNodeList(maze)

graph = m.getNodeGraph(nodeList)

src = m.findSource(maze)
dst = m.findDestination(maze)
# print(f"출발지 : {src} , 목적지 : {dst}")

m.bfs(graph, src, dst, maze)