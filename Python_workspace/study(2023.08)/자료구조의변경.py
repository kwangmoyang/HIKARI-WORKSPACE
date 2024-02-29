#자료구조의 변경
menu = {"커피", "우유", "주스"}
#print(menu, type(menu)) #{'주스', '우유', '커피'} <class 'set'>

menu = list(menu)
#print(menu, type(menu))

menu = tuple(menu)
#print(menu, type(menu))


#########퀴즈##########################
from random import *

####풀이
users = range(1, 21) # range로  1~20까지 손님을 설정해준다
#print(type(users))   # type이 range 타입이기 때문에  타입변경이 필요
users = list(users)  # 타입 변경이 완료

shuffle(users)       # list에 담긴 값이 랜덤으로 재 배정됨

winners = sample(users, 4) #랜덤으로 재 배정된 user 리스트에서 sample로 4명만 꺼내옴
# print(winners) # 4명 뽑힌거 확인 

# print(" -- 당첨자 발표 -- ")
# print(" 치킨 당첨자 : {} ".format(winners[0])) #4명중 첫번째 넣기
# print(" 커피 당첨자 : {} ".format(winners[1:])) # 나머지 때려 넣기
# print(" -- 축하합니다 -- ")

###재 풀이


customer = list(range(1,21))
shuffle(customer)
event = sample(customer, 4)


print(" -- 당첨자 발표 -- ")
print(" 치킨 당첨자 : {} ".format(event[0])) #4명중 첫번째 넣기
print(" 커피 당첨자 : {} ".format(event[1:])) # 나머지 때려 넣기
print(" -- 축하합니다 -- ")
