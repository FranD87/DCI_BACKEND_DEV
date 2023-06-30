from abc import ABC, abstractmethod
class BaseClass(ABC):
    def new_pet(self):
        return f'Welcome {self.name}'
    @abstractmethod
    def feed(self):
        pass
    def play(self):
        result = 'play with ball'
        return result
class Dog(BaseClass):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def feed(self):
        a_step = 'put dog food in plate'
        b_step = 'feed the dog'
        result = f'{a_step}\n{b_step}\ndog is full'
        return result
class Fish(BaseClass):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def feed(self):
        a_step = 'put fish food to aquarium'
        b_step = 'feed fish'
        result = f'{a_step}\n{b_step}\nfish is full'
        return result
    def play(self):
        result = 'Never play ball with fish'
        return result
class Panda(BaseClass):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def feed(self):
        a_step = 'put bamboo in plate'
        b_step = 'feed panda'
        result = f'{a_step}\n{b_step}\npanda is full'
        return result
dog = Dog('Ben', 2)
fish = Fish('Goldy', 3)
panda = Panda('Mindy', 5)
# print(dog.new_pet())
# print(fish.new_pet())
# print(panda.new_pet())
print(dog.play())
print(fish.play())