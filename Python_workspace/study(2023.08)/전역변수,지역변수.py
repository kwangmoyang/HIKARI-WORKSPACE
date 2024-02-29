#전역변수와 지역변수를 공부하자

gun = 10

 
def checkpoint(soldiers): # 경계근무
    global gun # 전역 공간에 있는 gun을 사용하겠다
    # gun = 20
    gun = gun - soldiers
    print("[함수 내 남은 총 : {0}]".format(gun))


def checkpoint_ret(gun, soldiers) :
    gun = gun - soldiers
    print("[함수 내 남은 총 : {0}]".format(gun))
    return gun

#print("전체 총 : {0}".format(gun)) #전역변수 사용
gun = checkpoint_ret(gun, 2)
checkpoint(2) # 2명이 경계근무를 나가게 된다
#print("남은 총 : {0}".format(gun)) #전역변수 사용


## 퀴즈 표준 체중을 구하는 프로그램을 작성


def std_weight(height, gender):
    if gender == "남자" :
        niceBody = height * height * 22
    elif gender == "여자" :    
        niceBody = height * height * 21
    else :
        print("올바른 성별을 입력해주세요")
        
    print("키 {0}cm {1}의 표준 체중은 {2} 입니다.".format(height, gender, round(niceBody, 2)))



std_weight(1.7, "여2자")
