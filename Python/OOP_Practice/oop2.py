class Poketmon():
    hp = 100

    def attack(self):
        return '공격했습니다.'

class Pikachu(Poketmon): # 부모클래스 : 포켓몬 / 자식클래스 : 피카츄
    
    def electric(self):
        return '전기공격을 했습니다.'

class Pairi(Poketmon):

    def attack(self): # 부모가 가지고 있는 attack이 있지만, 다시 만듬. overriding = 덮어씀
        self.hp = self.hp -5 # (2번째 self.hp에서 시작하는데 인스턴스에서 먼저 가져오려고함.)
        return f'현재 hp는 {self.hp}입니다.'

p1 = Pikachu()
p2 = Pikachu()

print(p1.electric())
print(p2.attack())

p3 = Pairi()
print(p3.attack())
print(p3.attack())
print(p3.attack())
print(p3.attack())
print(p3.attack())


# # 파이리가 부모클래스의 poketmon의 attack('공격ㅎㅆ습니다.')를 사용하기위해서는
# # super()를 쓰면 부모클래스가 가지고 있는 '공격했습니다.' 먼저 사용하고 나서 파이리에 있는
# # 클래스를 사용한다.

class Puppy: # 클래스
    population = 0 # 클래스 변수 
    
    def __init__(self, name, breed): # 생성자 함수 -> 인스턴스가 생성될 때 자동으로 실행됨
        self.name = name
        self.breed = breed
        Puppy.population += 1
        
    def __del__(self): # 소멸자 함수 -> 인스턴스가 삭제될 때 자동으로 실행됨
        Puppy.population -= 1
    
    def bark(self): # 인스턴스 메서드 -> 인스턴스가 항상 첫 번째 인자로 넘어감
        return f'왈왈! 나는{self.name}, {self.breed}(이)야'

    @classmethod
    def get_population(cls): # 클래스 메서드 -> 클래스가 항상 첫 번째 인자로 넘어감
        print(cls)
        return f'현재 강아지 마리수: {cls.population}'
    
    @staticmethod
    def info():
        return '귀여운 강아지를 만들기 위한 클래스입니다.'


p1 = Puppy('초코', '푸들')
p2 = Puppy('몽이', '허스키')
p3 = Puppy('복실이', '진돗개')

print(p1.bark())
print(p2.bark())
print(p3.bark())

print(Puppy.get_population())

del p3

print(Puppy.get_population())

# 개발자용 

class Puppy:
    population = 0

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        Puppy.add_population()

    def __del__(self):
        Puppy.remove_population()

    def bark(self):
        return f'왈왈! 나는{self.name}, {self.breed}야'

    @classmethod
    def add_population(cls):
        cls.population += 1

    @classmethod
    def remove_population(cls):
        cls.population -= 1

    @classmethod
    def get_population(cls):
        return f'현재 강아지 마리수: {cls.population}'

p1 = Puppy('초코', '푸들')
p2 = Puppy('몽이', '허스키')
p3 = Puppy('복실이', '진돗개')

# print(p1.bark())
# print(p2.bark())
# print(p3.bark())

# print(Puppy.get_population())

# del p3

# print(Puppy.get_population())

print(Puppy.bark(p1))