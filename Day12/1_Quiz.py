# https://programmers.co.kr/learn/courses/30/lessons/64061

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]

moves = [1,5,3,5,1,2,1,4]

def solution(board, moves):

    moves = list(map(lambda x: x-1, moves))

    stack = []
    answer = 0

    for m in moves:
        for i in range(len(board)):
            n = board[i][m]
            board[i][m] = 0
            if n != 0:
                if len(stack) != 0:
                    if stack[-1] == n:
                        stack = stack[:-1]
                        answer += 2
                    else:
                        stack.append(n)
                else:
                        stack.append(n)
                break
    return answer

result = solution(board, moves)
print(result)