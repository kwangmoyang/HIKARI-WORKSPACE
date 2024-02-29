# 튜플
# 내용변경이나 추가가 불가능함
# but 속도가 list보다 빠름

menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

#menu.add("생선까스") 추가가 안됨

name = "김종국"
age  = 20
hobby = "코딩"
print(name, age, hobby)

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)

# 집합 (set)
# 중복 안됨, 순서 없음
my_set = {1,2,3,3,3}
print(my_set) # 1,2,3 만 출력

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

#교집합 (java와 python을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

#합집합 (java도 할 수 있거나 python도 할 수 있는 개발자)
print(java | python) #순서는 보장되지 않음

#차집합 (java는 할줄 알지만 python은 할줄 모름)
print(java - python)
print(java.difference(python))

#python을 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)

#java를 까먹을 경우  (삭제)
java.remove("김태호")
print(java)
