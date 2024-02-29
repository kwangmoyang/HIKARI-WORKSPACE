#if 문을 배워보자

# weather = input("오늘 날씨는 어떄요?")
# if weather == "비":
# #if 조건:
# #    실행 명령문
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요 없어")


temp = int(input("기온은 어떄요?"))
if 30 <= temp:
    print("더우니까 나가지마라")
elif 10 <= temp and temp < 30:
    print("적당한 날씨긴하다")
elif 0 <= temp < 10:
    print("외투 챙기라")
else:
    print("너무 추웡")