# Создайте 2 экземпляра данного класса. У каждого 
# экземпляра вызовите оба параметра описанные в этом классе.
#  Для обоих экземпляров вызовите метод **climb**

class Monkey:
    max_age = 12
    loves_bananas = True

    def climb(self):
	    print('I am climbing the tree') 

c = Monkey()
p = Monkey()
c.climb()
print(c.max_age)
print(c.loves_bananas)
p.climb()
print(p.max_age)
print(p.loves_bananas)