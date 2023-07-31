# BFS를 활용해서 가까운 친구들 부터 탐색해보자~
# ※ set : 순서x, 중복x
# - 방문한 노드를 여기에 저장한다

def bfs(graph, node, visited) :
    queue = [node]
    visited.add(node)

    while queue :
        node = queue.pop(0)
        print(node, end = " ")

        for fri in graph[node] :
            if fri not in visited :
                queue.append(fri)
                visited.add(fri)

def dfs(graph, node, visited) :
    visited.add(node)
    print(node, end = " ")

    for fri in graph[node] :
        if fri not in visited :
            dfs(graph, fri, visited)
            

graph = {
    "Summer" : ["John", "Justin", "Mike"],
    "John" : ["Summer", "Justin"],
    "Justin" : ["Summer", "John", "Mike", "May"],
    "Mike" : ["Summer", "Justin", "Tom"],
    "May" : ["Justin", "Kim"],
    "Kim" : ["May"],
    "Tom" : ["Jerry", "Mike"],
    "Jerry" : ["Tom"]
}

visited = set()
bfs(graph, "Summer", visited)
print()


visited = set()
dfs(graph, "Summer", visited)
