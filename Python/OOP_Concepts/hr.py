''' Encapsulation - refers to wrapping up data under a single unit.
                  - protects data from being accessed by code outside of the class.

    Benefits:
    - Data handling
    - Flexibility
    - Reusability

   public
   protected - one underscore
   private - two underscores 
'''

class Personal:
    def __init__(self, x, y, z):
        self.name = x
        self._age = y
        self.__salary = z

    def describe(self):
        return f'Hi {self.name}, your age is {self._age} and your salary {self.__salary}'
    
    @property
    def Salary(self):
        return self.__salary

    @Salary.setter    
    def Salary(self, val):
        self.__salary = val

    def __repr__(self):
        return 'Personal class method'

    

#if __name__ == ''