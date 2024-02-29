print('풍선')
print("나비")
print("ㅎㅇ"*9)


# boolean 참/거짓
print(5 > 10)
print(5 < 10)
print(True)
print(not True) 
print("11번쨰줄",not (5 > 10))


animal = "고양이"
name = "해피"
age = 2
hobby = "산책"
is_adult = age >= 3


'''
이렇게 하면 한번에
여러줄이 주석처리가 가능하다
그리고 컨트롤 + 슬래시를 눌러도 가능
'''

# 애완동물을 소개해주세요
print("우리집 " +animal+ " 이름은 " + name+ "에요")
hobby = "공놀이"
#print(name+ "는 "+str(age)+"살이며, "+hobby+"을 좋아해요")
print(name+ "는 ", age,"살이며, "+hobby+"을 좋아해요")
print(name+ "는 어른일 까요?"+str(is_adult))


#QUIZ) 변수를 이용하여 다음 문장을 출력하시오

station = "사당"

print(station+"행 열차가 들어오고 있습니다.")



