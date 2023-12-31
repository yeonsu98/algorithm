# 그래프
# - 비선형 자료구조
# - Node와 Edge로 이루어진 구조
# - 그래프는 인접 행렬과 인접 리스트 방식으로 표현

F = float('inf')
print(F)

# 1. 인접 행렬
# - 모든 노드의 정보를 2차원으로 표현해서 그래프 전체 구성 파악이 용이
# - 단 노드가 많으면 크기가 커진다. O(n^2)
graph1 = [
#    0  1  2
    [0, 7, 5],      # 0번 노드
    [7, 0, F],      # 1번 노드
    [5, F, 0]       # 2번 노드
]

# 2. 인접 리스트
# - 인접한 행의 정보만 기입
# - 전체 구성 파악은 힘들지만 크기가 많이 절약된다.
graph2 = [
#    0  1  2
    [(1, 7), (2, 5)],      # 0번 노드
    [(0, 7)],              # 1번 노드
    [(0, 5)]               # 2번 노드
]
