
import random


guest = 0
todayMoney = 0

charge = 1000
charge_up = 500

for i in range(1,51):
    driveTime = random.randint(5, 50)
    if 5 <= driveTime <= 15 : 
        if driveTime > 10 :
            print("[O] {0}번째 손님 (소요시간 : {1}분) 요금은 기본 요금에 할증요금이 붙은 {2}원 입니다.".format(i,driveTime,charge+charge_up))
            todayMoney += charge+charge_up
        else :
            print("[O] {0}번째 손님 (소요시간 : {1}분) 요금은 기본 요금 {2}원 입니다".format(i,driveTime, charge))
            todayMoney += charge
        guest += 1
    else :
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i,driveTime))

print("총 탑승 승객 : {0} 명 , 오늘의 매출 {1}".format(guest,todayMoney))