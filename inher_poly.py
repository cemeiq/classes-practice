class Dog:
    def __init__(self, name , age, friendiliness):
        self.name = name
        self.age = age
        self. friendiliness = friendiliness

    def likes_bark(self):
        return True

    def bark_sound(self):
        return 'woof'

class Samoyed(Dog):
    def __init__(self, name, age, friendiliness):
        super().__init__(name, age, friendiliness)  

    def bark_sound(self):
        return 'oooooo'    

class Dalmation(Dog):
    def __init__(self, name, age, friendiliness):
        super().__init__(name, age, friendiliness)

    def fetching_ability(self):
        if self.age < 2:
            return 8
        else:
            return 4        

class Poodle(Dog):
    def __init__(self, name, age, friendiliness):
        super().__init__(name, age, friendiliness)     
    
    def shedding_amount(self):
        return False


class GoldenDoodle(Poodle, Dalmation):
    def __init__(self, name, age, friendiliness):
        super().__init__(name, age, friendiliness)

    def bark_sound(self):
        return 'aroo'    

sammie = Samoyed('sammie', 5, 5)
goldie = GoldenDoodle('Goldie', 10, 10) 
generic_dog = Dog('Gene', 10, 10)
# print(goldie.name, goldie.age, goldie.friendiliness)
# print(goldie.likes_bark())
# print(goldie.shedding_amount())      
# print(goldie.fetching_ability()) 
print(sammie.bark_sound())
print(goldie.bark_sound())
print(generic_dog.bark_sound())
