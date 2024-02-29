#중요한 클래스에 대해 아라보자
# 마린 : 공격 유닛, 군인, 총을 쏠 수 있음


# 탱크 : 만들자

# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35

# print("{} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))


# def attack(name, location, damage) :
#     print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(name, location, damage))

# attack(tank_name, "1시", tank_damage)


##########################################[클래스 만들기]#####################################################




# # 그래서 __init__은 뭐지? : 생성자 


# marine1 = Unit("마린", 30, 500)
# marine2 = Unit("마린", 50, 500)
# tank    = Unit("탱크", 200, 3000)

# wraith1 = Unit("레이스", 340, 70)                                      #멤버변수를 밖에서 쓰는 작업
# print("[정보] 유닛이름 : {0}, 유닛의 체력 : {1}, 유닛의 공격력 : {2} ".format(wraith1.name, wraith1.hp, wraith1.damage ))


# # 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것

# wraith2 = Unit("뺐은 레이스", 80, 5)  
# wraith2.clocking = True

# if wraith2.clocking == True :
#     print("{0} 는 현재 클로킹 상태입니다".format(wraith2.name))


##########################################[메서드 만들기]#####################################################
####상속 까지 내용 있다 ####

class Unit :
    def __init__(self, name, hp, speed):
        self.name = name #클래스 내에 정의된 변수가 멤버변수
        self.hp   = hp
        self.speed = speed
        print("{0} 유닛이 생성 되었습니다".format(name))

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))

# 공격 유닛
class AttackUnit(Unit) : # ( ) 괄호안에 상속받을 클래스 이름 넣으면 됨
    def __init__(self, name, hp, damage, speed):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage #클래스 내에 정의된 변수가 멤버변수
    
    def attack(self, location) :                        #self는 자기 자신을 의미한다  location은 셀프가 없으니 인자값을 받아서 사용
        print("{0} : {1} 방향으로 적군을 공격 합니다. 공격력 {2} ".format(self.name, location, self.damage))

    def damaged(self, damage) :
        print("{0} : {1} 데미지를 입었다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 뒤져버렷".format(self.name))


# hikari = AttackUnit("히카리", 50, 25)
# hikari.attack(50)
# hikari.damaged(60)

# 그럼 다중 상속은??? 

# 드랍쉽 공중 유닛, 수송기. 

class Flyable :
    def __init__(self, flying_speed) :
        self.flying_speed = flying_speed
    
    def fly(self, name, location) :
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스
class FlyandAttack(AttackUnit,Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name,hp, 0, damage)
        Flyable.__init__(self, flying_speed)


    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)


# 발키리 : 공중 곡격 유닛, 한번에 14발 발사
#valkyrie = FlyandAttack("발키리", 200, 300, 300)
#valkyrie.fly(valkyrie.name, 200)

# 벌쳐 만들어보자
vultuer = AttackUnit("벌쳐", 80, 10, 20)

# 배틀 크루저 :
battlecruiser = FlyandAttack("배틀 크루저", 500, 25, 3)

vultuer.move("12시")
battlecruiser.move("3시")




######################PASS 는 뭐냐 ###################

# 건물
class BuildingUnit(Unit) :
    def __init__(self, name, hp, location):
        # Unit.__init__(self, name, hp, 0)
        super().__init__(name, hp, 0) # super 써서 사용이 가능 But문제는 다중상속시 문제
        self.location = location
        # pass 일단 완성된것처럼 보이게? 기본생성자 인건가


# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")

# def game_over() :
#     pass


supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

    