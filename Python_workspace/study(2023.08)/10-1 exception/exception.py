
## 직접 정의해서 에러 만들기

class BigNumberError(Exception):
    def __init__(self, msg) :
        self.msg = msg
    
    def __str__(self):
        return self.msg

class SoldOutError(Exception):
    pass
    
# try :
#     print("나누기 전용 계산기 입니다")
#     num1 = int(input("첫 번째 숫자 입력 : "))
#     num2 = int(input("2 번째 숫자 입력 : "))
#     if num1 >= 10 or num2 >= 10 :
#         raise ValueError

#     print("{0} / {1} = {2}".format(num1, num2, int(num1/num2) ))
# except ValueError:
#     print("에러! 잘못된 값을 입력함")
# except BigNumberError :
#     print("무리무리")
# finally : 
#     print("프로그램 마무리")



chicken = 10
waiting = 1 # 대기번호 1부터 시작


while(True):
        try :    
            print("현재 남은 치킨은 {0}마리 입니다. ".format(chicken))
            order = int(input("몇 마리 주문하시겠습니까?"))
            if order < 1 :
                raise ValueError
            if order > chicken :
                print("재고가 부족합니다.")
            else :
                print("{0}마리 주문이 완료 됨 대기번호는 {1}번 입니다.".format(order,waiting))
                waiting += 1
                chicken -= order
            if chicken == 0 :
                raise SoldOutError  
        except ValueError:
            print("잘못된 값을 입력함")
        except SoldOutError:
            print("재고가 소진되어 주문 안되요")
            break
      





