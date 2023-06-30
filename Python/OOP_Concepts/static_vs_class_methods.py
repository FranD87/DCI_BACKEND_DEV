
# https://realpython.com/instance-class-and-static-methods-demystified/#:~:text=Class%20methods%20don't%20need,belong%20to%20the%20class's%20namespace.

class MyClass:
    def method(self):
        return 'instance method called', self
    @classmethod
    def clas_method(cls):
        return 'class method called', cls
    @staticmethod
    def st_method():
        return 'static method called'
# print(MyClass.method()) -> TypeError: MyClass.method() missing 1 required positional argument: 'self'
print(MyClass.clas_method())
print(MyClass.st_method())
class Student:
    # class variables
    school_name = None
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # instance method
    def show(self):
        # access instance variables
        print('Student:', self.name, self.age)
        # access class variables
        print('School:', self.school_name)
    def set_school(self, school):
        if Student.school_name is None:
            self.school_name = school
            print('Student start to learn in school', school)
        else:
            print(f'Student change school from {self.school_name} to {school}')
            self.school_name = school
    @classmethod
    def change_School(cls, name):
        # access class variable
        print('Previous School name:', cls.school_name)
        cls.school_name = name
        print('School name changed to', Student.school_name)
    @staticmethod
    def find_notes():
        # can't access instance or class attributes
        return ['chapter 1', 'chapter 2', 'chapter 3']
# create object
student1 = Student('Bob', 12)
# call instance method
student1.show()
student1.set_school('ABC School')
student1.show()
print(Student.school_name)
Student.change_School('TEST')
student1.show()
print(Student.school_name)


'''
The provided code includes two classes: `MyClass` and `Student`.

Class: MyClass
- Method: `method(self)`
  - Instance method that takes `self` as the parameter.
  - Returns a tuple with the string "instance method called" and the instance itself.

- Class Method: `clas_method(cls)`
  - Class method that takes `cls` as the parameter.
  - Returns a tuple with the string "class method called" and the class itself.

- Static Method: `st_method()`
  - Static method with no parameters.
  - Returns the string "static method called".

Class: Student
- Class Variables:
  - `school_name`: A class variable that is initially set to `None`.

- Constructor: `__init__(self, name, age)`
  - Initializes the instance with `name` and `age` attributes.

- Instance Method: `show(self)`
  - Prints the student's name and age using instance variables.
  - Prints the school name using the class variable `school_name`.

- Instance Method: `set_school(self, school)`
  - Sets the school name using the instance variable `school_name`.
  - Prints a message indicating whether the student is starting to learn in a new school or changing schools.

- Class Method: `change_School(cls, name)`
  - Changes the school name using the class variable `school_name`.
  - Prints the previous school name and the new school name.

- Static Method: `find_notes()`
  - Returns a list of notes without accessing any instance or class attributes.

- Creating an object of the Student class: `student1 = Student('Bob', 12)`
- Calling instance methods on the `student1` object:
  - `student1.show()`: Displays the student's name, age, and school name.
  - `student1.set_school('ABC School')`: Sets the school name to "ABC School" and displays a message.
  - `student1.show()`: Displays the updated student's information.
- Accessing the class variable `school_name` using the class name `Student.school_name`.
- Calling the class method `change_School('TEST')`: Changes the school name and displays the previous and new school
  names.
- Calling `student1.show()`: Displays the updated student's information.
- Accessing the class variable `school_name` using the class name `Student.school_name`.
'''



