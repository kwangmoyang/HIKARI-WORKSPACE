# 리스트 (배열) []

# 지하철 칸별로 10명, 20명, 30명

subway = [10, 20, 30]
print(subway.index(10)) #10의 위치가 어디 있는가?

human = ["유재석","조세호","박명수"]
print(human.index("조세호"))

# 하하씨가 다음 정류장에 탄다면
human.append("하하") #append  더하다
print(human)

#정형돈씨를 유재석/ 조세호 사이
human.insert(1, "정형돈") # index 1번자리에 넣어준다
print(human)

#지하철에 있는 사람을 한명씩 뒤에서 꺼냄
print(human.pop())
print(human)

#같은 이름의 사람이 몇명인지 확인
human.append("유재석")
print(human)
print(human.count("유재석"))

#정렬도 가능
num_list = [1,6,3,4,5]
print(num_list)
num_list.sort()
print(num_list)
num_list.reverse() #역순으로 정렬
print(num_list)

#모두 지우기
num_list.clear()
print(num_list)

#다양한 자료형 함께 사용
#리스트 확정
subway.extend(human)
print(subway)

