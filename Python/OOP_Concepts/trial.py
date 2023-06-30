from hr import Personal

per = Personal('Hollard', 45, '$4000')

#per.getSalary('$5000')
per.Salary = '1000'
per.name = 'John'
per._age = 16

print(per.name)
print(per._age)
print(per.Salary)
print(per.__dict__)
print(per._Personal__salary) # this method of accessing private variables is not good practice and should not be used during development.

print(per)