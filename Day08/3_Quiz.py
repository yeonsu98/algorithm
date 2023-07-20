# https://school.programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    answer = []
    length = len(stages) # 유저수

    for i in range(1, N+1):

        # i번째 머물러 있는(=실패한) 유저 카운트
        count = stages.count(i) 

        # 실패율 : 실패한 유저 / 도달한 유저
        if length == 0:
            fail = 0
        else : 
            fail = count / length

        answer.append((i, fail))
        length -= count

    # 실패율을 1번 index에 담고 그를 기반으로 내림차순 정렬
    answer.sort(key = lambda x : -x[1])

    #정답은 실패율 빼고 스테이지만 반환
    answer = [i[0] for i in answer]
    return answer

print("결과 1 :", solution(5, [2,1,2,6,2,4,3,3]))