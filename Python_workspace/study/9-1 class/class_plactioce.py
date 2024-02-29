class Unit :
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Unit, Flyable) :
    def __init__(self):
        super().__init__()



dropshit  = FlyableUnit()


