# https://www.acmicpc.net/problem/18310

n = int(input())
home = list(map(int, input().split()))

home.sort()
print(home[(n-1)//2])



