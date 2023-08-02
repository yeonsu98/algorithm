# 미로 찾기
# step 5 : 입구, 출구 찾기

import maze as m

maze = [
    [1,0,1,1,1],
    [1,0,1,0,0],
    [1,0,1,0,1],
    [1,0,0,0,1],
    [1,1,1,1,1]
]

m.printMaze(maze)

src = m.findSource(maze)
dst = m.findDestination(maze)
print(f"출발지 : {src} , 목적지 : {dst}")

