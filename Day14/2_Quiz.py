metro = {
    "교대" : ["연산"],
    "거제" : ["연산"],
    "연산" : ["교대", "거제", "시청", "물만골"],
    "시청" : ["연산", "양정"],
    "양정" : ["시청", "부전"],
    "부전" : ["양정", "서면"],
    "서면" : ["부전", "부암", "범내골", "전포"],
    "부암" : ["서면"],
    "범내골" : ["서면"],
    "전포" : ["서면", "국제"],
    "국제" : ["전포", "문현"],
    "문현" : ["국제", "지게골"],
    "지게골" : ["문현", "못골"],
    "못골" : ["지게골", "대연"],
    "대연" : ["못골", "경성대부경대"],
    "경성대부경대" : ["대연", "남천"],
    "남천" : ["경성대부경대", "금련산"],
    "금련산" : ["남천", "광안"],
    "광안" : ["금련산", "수영"],
    "수영" : ["광안", "민락", "망미"],
    "민락" : ["수영", "센텀시티"],
    "센텀시티" : ["민락"],
    "물만골" : ["연산", "배산"],
    "배산" : ["물만골", "망미"],
    "망미" : ["배산", "수영"]

}

# 1. 출발역을 지정해서 모든 노드의 촌 수를 구한다.
src = input("출발역 > ")
dst = input("도착역 > ")

def bfs(graph, node):

    queue = [(node, 0)] # (노드, 촌수)
    visited = set()

    while queue :
        node, count = queue.pop(0)
        visited.add(node)
        print(f"{node}({count})", end=" ")

        for sta in graph[node] :
            if sta not in visited :
                queue.append((sta, count+1))
                visited.add(sta)

bfs(metro, src)
print()
print("="*90)


# 2. 도착역도 지정해서 도착역의 촌 수를 출력한다
# - 이 촌 수가 최소 횟수가 됨
def getMinPath(graph, src, dst):

    queue = [(src, 0)]
    visited = {src}

    parents = {} # 역 추적할 부모 리스트

    for key in graph.keys():
        parents[key] = ""
    # print(parents)

    while queue:
        src, count = queue.pop(0)
        # print(f"{src}({count})", end=" ")

        for sta in graph[src]:
            if sta not in visited:
                queue.append((sta, count+1))
                visited.add(sta)    

               # 다음 진입할 노드에 이전 위치로 현재 노드 저장
                parents[sta] = src 

    # for k, v in parents.items():
    #     print(f"{k} : {v}")

    # 경로 추척
    trace = []
    cur = dst
    
    while cur != '':
        trace.append(cur)
        cur = parents[cur]
    
    trace.reverse()
    return trace


minPath = getMinPath(metro, src, dst)
print(f"최소 거리 : {len(minPath)-1} 정거장") # 출발지도 들어가기 때문에 -1 해줌
print("경로 : ", " => ".join(minPath))