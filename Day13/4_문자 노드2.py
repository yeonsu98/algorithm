# ex04를 그래프로 표현시
graph = {
    "Summer" : ["John", "Justin", "Mike"],
    "John" : ["Summer", "Justin"],
    "Justin" : ["Summer", "John", "Mike", "May"],
    "Mike" : ["Summer", "Justin"],
    "May" : ["Justin", "Kim"],
    "Kim" : ["May"],
    "Tom" : ["Jerry"],
    "Jerry" : ["Tom"]
}

print("Summer의 친구들 :", graph["Summer"])
print("Justin의 친구들 :", graph["Justin"])