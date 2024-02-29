import sys
#print("Python", "Java", file=sys.stdout) # 표준 출력으로 처리
#print("Python", "Java", file=sys.stderr) # 표준 에러로 확인 (로그 확인?)


scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items(): #key와 value 값을 과목과 점수에 각각 넣는다
    print(subject.ljust(8), str(score).rjust(4), sep=":")


# 은행 대기순번표
# 001, 002 003

#for num in range(1, 21):
#    print("대기번호 : " + str(num).zfill(3)) # 3개 크기만큼 공간을 확보하고 빈공가넹 대해선 0으로 ㅊ워달라

#answer = input("아무 값이나 입력하세요 : ") #사용자 입력으로 받을땐 무조건 문자형으로 받게된다.
#print("입력값은"+ answer + "입니다.")


##########데이터 입출력을 설정해보자 ####################

#print("Python", "Java", "JavaScript", sep=",", end="?")
# Python vs Java vs JavaScript 각 글자 마다 
#print("무엇이 더 재밌을까요?")
# end=" " 를 씀으로써 두줄에 걸치는게 아니라 한번에 나옴




# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500))
# 양수일 떈 +로 표시, 음수일떈 -로 표시
print("{0: >+10}".format(500)) # +500
print("{0: >-10}".format(500)) # -500

# 왼쪽 정렬하고, 빈칸을 _로 채우기
print("{0:_<+10}".format(500)) #+500______
# 3자리 마다 콤마를 찍어주기
print("{0:,}".format(1000000000)) # 1,000,000,000

#소수점 출력
print("{0:.2f}".format(5/3))  # .2를 붙임으로써 2자리 까지만 나오게 해달라
