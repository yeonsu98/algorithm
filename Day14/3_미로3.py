# 미로 찾기
# step 3 : 인접한 좌표인지 파악

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

first = nodeList[0]
second = nodeList[3]
print(f"{first}와 {second}는 인접? ", m.isNear(first, second))

# 인접한 것을 찾았으니 이걸 인접리스트 만들어서 bfs 구해보기