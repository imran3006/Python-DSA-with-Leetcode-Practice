class Animal:
    def __init__(self, name):
        self.name= name

    def speak(self):
        pass # base class doesnot provide specific implementation

class Cat(Animal):
    def speak(self):
        return f"{self.name} calls meua meau"
    
cat = Cat("robi")
print(cat.speak())


