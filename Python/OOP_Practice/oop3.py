class Person:

    nation = 'korea'
    code = 'KR'

    def __init__(self, name, age, location, email):
        self.name = name
        self.age = age
        self.location = location
        self.email = email

    def greeting(self):
        return f'안녕, 나는 {self.name}이고, {self.age}고, {self.location}, {self.email}'

    @classmethod
    def info(cls):
        return f'{cls.nation}의 코드는 {cls.code}이다.'

class Student(Person):

    def __init__(self, name, age, location, email, student_id):
        super().__init__(name, age, location, email)
        self.student_id = student_id

    def talk(self):
        return f'안녕하세요 저는 {self.name}이고, {self.age}살 입니다.'

    # def greeting(self):
    #     return f'안녕, 나는 {self.name}이고, {self.age}고, {self.location}, {self.email}'

class Professor(Person):

    def __init__(self, name):
        self.name = name

    def talk(self):
        return f'나는 {self.name}일세.'

p1 = Professor('park')
print(p1.talk())

s1 = Student('kim', 23, 'ser', 'sakdf@asdklf.com', 93294)
print(s1.info())
print(p1.info())

print(Person.info())