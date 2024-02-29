#연산자

# print(1+1) # 2
# print(5*2) # 10

# print(2**3) #2의 3제곱
# print(5//3) # 몫을 출력한다


# print(3 == 3) #true ===는 파이썬에서 안되네 
# print(3 + 4 == 7)
# print(not(1 != 3)) # FALSE

# print((3 > 0) and (0 < 3)) # and 연산자 
# print((3 > 0) & (0 < 3)) # and 연산자 

# 간단한 수식
number = 3 + 4

number += 3
#print(number)

#숫자 처리
# print(abs(-5)) # 절댓값
# print(pow(4, 2)) # 4^2 = 4*4 = 16
# print(max(5, 12)) #12 max값 출력해줌
# print(round(3.14)) # 뒷 숫자 버림

from math import * # math 임폴트
# print(floor(3.4)) #숫자 내림
# print(ceil(3.4)) #숫자 올림
# print(sqrt(16)) #제곱근


#랜덤 함수

from random import *

#print(round(random()))
# print(int(random() * 45) + 1)

# print(randrange(1, 46)) # 1 ~ 46 미만의 임의의값 생성
# print(randint(1, 45)) # 1 ~ 45  의 값을 생성


#result = randint(4, 28)
#print("오프라인 스터디 모임 날짜는 매월"+(str(result))+" 일로 선정되었습니다.")


##### 문자열

sentence = '나는 소년입니다'
#print(sentence)
sentence2 = "파이썬은 쉬워요"
#print(sentence2)


sentence3 = """
안녕하세요
양광모

입니다

"""
#print(sentence3)


jumin = "990120-1234567"

print("성별 : " + jumin[7]) #배열
print("연 : " + jumin[0:2]) # 0 부터 2 직전까지 즉 0,1이 출력
print("월 : " + jumin[2:4]) 
print("일 : " + jumin[4:6]) 

print("생년월일 : " + jumin[:6]) # 첨부터 6직전까지
print("뒷자리 : " + jumin[7:]) # 선택한 부분부터 마지막 까지

#뒤에서 부터 가져오기
print("마지막 부터 어케가져오냐 "+jumin[-7:])

##################문자열 처리함수 ############################

python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper()) # 배열의 해당 자리가 대문자or소문자가 맞는지
print(len(python)) # 해당 변수의 길이
print(python.replace("Python", "Life")) #해당 단어 변경 리플레이스

index = python.index("n") #인덱스 값의 위치를 찾아줌
print(index)
index2 = python.index("n", index + 1) #첫번쨰 N값의 다음 알파벳을 찾는다
print(index2)

print(python.find("n")) #index위치 찾는거 처럼 비슷함


#find에서 내가 원하는 값을 발견하지 못하면 -1를 반환 시킴

print(python.count("n")) #n이라는 글자가 총 몇개 있는지?

################################################################



# 문자열 포멧

# 방법1
print("나는 %d살 입니다." % 20) #정수형
print("나는 %s을 좋아해요. " % "파이썬")
print("Apple은 %c로 시작한답니다" % "A")

# 값을 2개 넣을 경우에
print("나는 %s 색과 %s 색을 좋아해요" %("파랑", "빨강")) 

# 방법 2
print("나는 {}살입니다. ".format(20))
print("나는 {}색과 {}색을 좋아해요".format("빨강" , "파랑")) 
print("나는 {1}색과 {0}색을 좋아해요".format("빨강" , "파랑")) #순서를 직접 정해서 사용이 가능

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요".format(age = 20, color="빨강"))

# 방법 4 (v3.6 이상~)
age = 20
color = "빨강"
print(f"나는 {age}살이며, {color}색을 좋아해요")

#탈출 문자
print("백문이 불여일견 \n 백견이 불여일타")
print("저는 \'나도코딩\'입니다.")

# \\ : 문장 내에서 \

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine") 

# \b : 백스페이스 (한 글자 삭제)
print("Redd\bApple")

# \t : 탭
print("Red\tApple")


##########풀이 #####################

urll = "http://naver.com"
my_str = urll.replace("http://", "")
print(my_str)
#naver.com
my_str = my_str[:my_str.index(".")]
#naver
pw = my_str[:3] + str(len(my_str)) + str(my_str.count('e')) + "!" #정수일경우 str로 형변환이 필요
print("{0}의 비밀번호는 {1} 입니다.".format("광모",pw))

##re
urll_re = "http://naver.com"
url_temp = urll_re.replace("http://","")

url_temp = url_temp[:url_temp.index(".")]
re_pw = url_temp[:3] + str(len(url_temp)) + str(url_temp.count("e")) + "!"
print("{0}님의 암호는{1}입니다.".format("메밍묵",re_pw))

###########심화 블로거 id 추출 ##############
bloger_url = "https://blog.naver.com/1ovest"
bloger_url_result = bloger_url.replace("https://blog.naver.com/","")
print("추출된 블로거는{}입니다".format(bloger_url_result))


