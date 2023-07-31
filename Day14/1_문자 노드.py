# 촌수 출력
# bfs를 활용해 가까운 친구부터 탐색
# 그 후 친구들의 촌수 출력

def bfs(graph, node):

    queue = [(node, 0)] # (노드, 촌수)
    visited = set()

    while queue :
        node, count = queue.pop(0)
        visited.add(node)
        print(f"{node}({count})", end=" ")

        for fri in graph[node] :
            if fri not in visited :
                queue.append((fri, count+1))
                visited.add(fri)

graph = {
    "Summer" : ["John", "Justin", "Mike"],
    "John" : ["Summer", "Justin"],
    "Justin" : ["Summer", "John", "Mike", "May"],
    "Mike" : ["Summer", "Justin"],
    "May" : ["Justin", "Kim"],
    "Kim" : ["May"],
    "Tom" : ["Jerry", "Mike"],
    "Jerry" : ["Tom"]
}

bfs(graph, "Summer")
print()