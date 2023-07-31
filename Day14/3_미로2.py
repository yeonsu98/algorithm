# 미로 찾기
# step 2. 이동 가능한 좌표를 목록으로 작성

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
print("이동 가능(=0)한 좌표 : " )
for p in nodeList:
    print(p)