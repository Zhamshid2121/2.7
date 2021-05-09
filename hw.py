#Создайте класс. Добавьте к классу 3 параметра. Напишите 
# 1 метод, который будет выводить 
# на экран все 3 параметра. Создайте экземпляр класса. 
# Вызовите его метод

class Jon:
    born = 15
    height = 50
    step = 25

    def men(self):
        return self.born + self.height +self.step

c = Jon()
c.men()
print(c.men())