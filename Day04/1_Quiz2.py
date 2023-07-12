# 피보나치 수열

def fibo(n):
    global fiboSave      # 함수 밖의 전역변수를 사용 시 선언

    if fiboSave[n] != 0: # 0이 아니라는 것은 이미 한 번 구한 적 있는 피보나치 수열
        return fiboSave[n]

    if n > 0 and n <= 2:
        fiboSave[n] = 1
        return 1
    
    fiboSave[n] = fibo(n-1) + fibo(n-2)
    return fiboSave[n]
    
n = 100
fiboSave = [0]*(n+1)
print(fiboSave)

for i in range(1, n+1):
    print(f"{i}번째 fibo =", fibo(i))
    #print(fiboSave) # debugging