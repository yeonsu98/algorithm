# 미로 찾기
# step 4 : 인접 리스트로 생성하기

import maze as m

maze = [
    [1,2,1,1,1],
    [1,0,1,0,0],
    [1,0,1,0,1],
    [1,0,0,0,1],
    [1,1,1,1,1]
]

m.printMaze(maze)

nodeList = m.getNodeList(maze)

graph = m.getNodeGraph(nodeList)
for k, v in graph.items():
    print(f"{k} : {v}")
