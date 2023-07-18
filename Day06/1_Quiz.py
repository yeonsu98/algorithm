# 1. 사용자 수를 입력받는다.
num = int(input("사용자 수 > "))

# 2. 입력받은 수만큼 이름, 나이를 입력받아 리스트에 저장한다.
user = []
for i in range(1, num+1):
    name = input(f"{i}번째 사용자 이름 > ")
    age = int(input(f"{i}번째 사용자 나이 > "))
    user.append((name, age))

# 3. 입력받은 데이터를 출력
# [("홍길동", 17), ("김민지", 33), ("박수진", 25)]
print("정렬 전 :", user)
# - 정렬 알고리즘 아무거나 사용하여 내림차순 정렬
while True: # 선택정렬 사용해서 내림차순으로 정렬
    cnt = 0
    for i in range(0, num-1):
        if user[i][1] < user[i+1][1]:
            user[i], user[i+1] = user[i+1], user[i]
            cnt += 1
    if cnt == 0:
        break
print("정렬 후 :", user)

