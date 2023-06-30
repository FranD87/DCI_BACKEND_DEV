class Singleton:
   __instance = None
   @staticmethod
   def getInstance():
      """ Static access method. """
      if Singleton.__instance == None:
         Singleton()
      return Singleton.__instance
   def __init__(self):
      """ Virtually private constructor. """
      if Singleton.__instance == None:
         Singleton.__instance = self
      else:
         raise ValueError('Instance already created')
s = Singleton()
print(s)
b = Singleton.getInstance()
print(b)
d = Singleton()




