# # 상황 1

# class Person:
#     population = 0
    
#     def __init__(self):
#         Person.population += 1 # -->
  
#     @classmethod
#     def get_population(cls):
#         return Person.population

# class Student(Person):
#     population = 0
    
#     def __init__(self):
#         super().__init__() 
#         Student.population += 1

# p1 = Person() 
# s1 = Student()

# print(Person.get_population()) 
# print(Student.get_population()) 

# 상황 2

class Person:
    population = 0
    
    def __init__(self):
        Person.population += 1
  
    @classmethod
    def get_population(cls): # cls->클래스->Student.get.population()->Student 클래스가 cls / Person.get_population() -> Person 클래스가 cls
        print(cls)
        return cls.population

class Student(Person):
    population = 0
    
    def __init__(self):
        super().__init__()
        Student.population += 1

p1 = Person()
s1 = Student()

print(Person.get_population())
print(Student.get_population())

print(Person.population)
print(Student.population)