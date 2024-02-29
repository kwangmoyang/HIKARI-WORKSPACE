#반복문
# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")

for waiting_no in [0, 1, 2, 3, 4]:
    print("대기번호 : {0}".format(waiting_no))


for waiting_no in range(1,6): # 0,1,2,3,4  range(1,6)은 1부터 6전 숫자까지
    print("대기번호 : {0}".format(waiting_no))


starbucks = ["아이언맨", "토르", "아이엠 그루트"]
for customer in starbucks:
    print("{0}, 커피가 주문되었습니다.".format(customer))


# while 문

# customer = "토르"
# index = 5
# while index >= 1:
#     print("{0}, 커피가 준비 되었습니다. {1} 번 남았어요".format(customer, index))
#     index -= 1
#     if index == 0 :
#         print("커피는 폐기 처분입니다.")


# customer = "아이언맨"
# index = 1
# while True:
#     print("{0}, 커피가 준비 되었습니다.{1}회째".format(customer, index))
#     index += 1


# customer = "토르"
# person = "Unknown"

# while person != customer :
#     print("{0}님 커피가 준비되었어요. 이름이 뭐에요?".format(customer))
#     person = input("이름이 모에요?")
#     if person == customer :
#         print("{0}님 감사합니다 또 이용해 주세요".format(customer))
#     else :
#         print("너 아니에요")    

#continue

absent = [2, 5] # 결석
no_book = [7] # 책을 깜빡했음
for student in range(1, 11): # 1,2,4
    if student in absent:
        continue # 52번 라인의 조건문에 일치하면 54번 라인은 진행하지 않고 넘어간다
    elif student in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
        break #아얘 for문을 탈출해버림
    print("{0}, 책을 읽어봐".format(student))

# 한줄로 끝내는 for문?
# 출석번호가 1 2 3 4, 앞에 100을 붙이기로 함 -> 101, 102, 103
students = [1,2,3,4,5]
#print(students)
students = [i+100 for i in students]
#print(students)

# 학생 이름을 길이로 변환
students = ["Iron man", "Thor", "I am groot"]
#students = [len(i) for i in students]
students = [i.upper() for i in students]
print(students)