class Student:
    
    def __init__(self, name, age, student_class, language='EN'):
        self.name = name
        self.age = age
        self.student_class = student_class
        self.language = language

    def next_class(self):
        '''
        Giving nex class of student
    '''
        var_next_class = self.student_class + 1
        return var_next_class
    
    def change_language(self, language):
        '''
        Changing language for student object on language from params
        '''
        language = language
        return self.language
    
    def change_class(self, new_class):
        '''
        Change class of student to class from params
        '''
        self.student_class = new_class
        return self.student_class
    
class Teacher:
    def __init__(self, name, age, language='DE'):
        self.name = name
        self.age = age
        self.language = language

    def change_language(self, language):
        self.language = language
        print('This is teacher language')
        return self.language
        

