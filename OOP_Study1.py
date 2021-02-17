'''
2021/2/10

物件導向

多重繼承(Multiple Inheritance)

多重繼承顧名思義，子類別可繼承多個Parent類別，且能夠擁有這些Parent類別的屬性與method。
這要怎樣理解呢？你可以想像「你自己」，「你自己」就是一個多重繼承的概念，你繼承了你爸媽這兩個類別所有的基因與行為，
這也是為什麼大家常講的「小孩是不能偷生的」( XDDDD )，因為可以從外觀、言行舉止進行判讀。

'''
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sound(self, voice):
        return voice

class Dog(Animal):
    def __init__(self, name, age, color):
        Animal.__init__(self, name,age) 
        self.color = color
    def sound(self, voice):
        return f"{self.name} has the {voice} sounds"
    def run(self):
        return "Running fast"

class Labrador(Dog, Animal):
    pass

ami = Labrador("AMI", 2, "Brown")
print("My name is {} and {} years old".format(ami.name, ami.age)) # My name is AMI and 2 years old
print(ami.run())   # Running fast