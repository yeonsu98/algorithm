# https://programmers.co.kr/learn/courses/30/lessons/64061

def printMap(board):
    for line in board:
        for n in line:
            if n == 0 : n = " "
            print(n, end=" ")
        print()

def push(stack, n):
    stack.append(n)

def solution(board, moves):
    stack = []      # 뽑은 인형이 쌓일 스택
    answer = 0
    #printMap(board)

    # move의 요소를 1씩 차감 (왜? index는 0부터라서)
    moves = list(map(lambda x : x-1, moves))

    for j in moves:
        for i in range(len(board)):
            #print(board[i][j])
            if board[i][j] != 0:
                push(stack, board[i][j])
                board[i][j] = 0
                break
            if len(stack) >= 2:
                if stack[-1] == stack[-2]:
                    stack.pop()
                    stack.pop()

                    answer += 2
        #printMap(board)

    return answer
        

    
board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

result = solution(board, moves)
print(result)