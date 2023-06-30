# What will happen if we will try to convert 'Abc' to int?
# How can we prevent it?
var = '123'
def check_int_conv(value):
    try:
        int(value)
        return True
    except ValueError:
        # Handle the exception
        return False
if check_int_conv(var):
    print(int(var))
else:
    print('We can not convert')
def converter(var):
    try:
        if var.isdigit():
            print('This is integer')
        else:
            raise ValueError('This string can not be converted to int')
    except ValueError as massage:
        print(massage)
converter('ABC')
converter('123')
class Dog:
    def speak(self):
        return "Woof!"
class Cat:
    def speak(self):
        return "Meow!"
def get_pet(pet):
    if pet == 'cat':
        return Cat()
    elif pet == 'dog':
        return Dog()
    else:
        raise TypeError('Invalid type of pet')
d = get_pet('dog') # -> d = Dog()
print(d.speak())
# w = get_pet('test')
# Factory control object creation depending on specific conditions
class PetFactory:
    @staticmethod
    def get_pet(pet):
        if pet == 'cat':
            return Cat()
        elif pet == 'dog':
            return Dog()
        else:
            raise TypeError('Invalid type of pet')
test_d = PetFactory.get_pet('dog') # -> test_d = Dog()
test_c = PetFactory.get_pet('cat') # -> test_c = Cat()
test_w = PetFactory.get_pet('test') # -> test_w = TypeError
print(test_d.speak())
print(test_c.speak())

# https://realpython.com/factory-method-python/
