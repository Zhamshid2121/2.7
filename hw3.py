#Создайте класс Person. При создании экземпляра данного
#  класса мы должны вводить 3 парамметра name, age, gender. 
# Напишите метод calculate_agec к этому классу, этот метод 
# должен принимать в себя число и возвращать 
# в каком возрасте будет человек через это число лет.

class Person:
    name = 'John'
    age = 23
    gender = 'men'
    
    def __init__(self, calculate_age):
        self.calculate_age = calculate_age
        print('(Через 10 лет John исполнится 33: {0})'.format(self.calculate_age))
  
       
    def yer(self):
        return self.age + self.calculate_age
c = Person(10)
print(c.yer())