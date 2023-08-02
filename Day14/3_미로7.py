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

m.printMaze(maze)

nodeList = m.getNodeList(maze)

graph = m.getNodeGraph(nodeList)

src = m.findSource(maze)
dst = m.findDestination(maze)
print(f"출발지 : {src} , 목적지 : {dst}")

# m.bfs(graph, src, dst, maze)

path = m.bfs2(graph, src, dst, maze)
m.printPath(maze, path)

path.reverse()
m.printPath(maze, path)
