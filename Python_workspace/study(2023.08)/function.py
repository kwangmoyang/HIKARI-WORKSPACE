#함수를 아라보자
def open_account() : #함수의 정의
    print("새로운 계좌가 생성되었습니다. ")

def deposit(balance, money): # 입금 함수
    print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
    return balance + money

def withdraw(balance, money): # 출금 함수
    if balance >= money :
        
        print("{0}원 출금이 완료. 남은 금액{1}원 입니다.".format(money, balance - money))
        return balance - money 
    else :
        print("이 돈은 못뽑아")
        
def withdraw_night(balance, money): #저녁에 출금
    commision = 100 # 수수료 100원
    return commision, balance - money - commision
        


balance = 0 # 잔액
balance = deposit(balance, 1000)
print(balance)
#balance = withdraw(balance, 2500)
commission, balance = withdraw_night(balance, 500)
print("수수료는 {0} 원이며, 잔액은 {1} 원입니다.".format(commission, balance))