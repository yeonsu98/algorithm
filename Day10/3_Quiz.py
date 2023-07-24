# ex03.png

hour = int(input())

cnt = 0

for h in range(hour+1):
    for m in range(60):
        for s in range(60):
            time = str(h) + str(m) + str(s)
            if "3" in time:
                cnt += 1
                # 디버깅
                # print(f"{h}시{m}분{s}초 - {cnt}개")
print(cnt)  