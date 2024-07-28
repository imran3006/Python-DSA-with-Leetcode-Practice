class School:
    #constructor
    def __init__(self, name, adress):
        self.name= name
        self.adress = adress

    def introduce(self):
        return f"school name {self.name} and address is {self.adress}"
    
school1 = School("nghs", "Nasirabad")
school2 = School("cghs", "Chawkbazar")

print(school1.introduce())
print(school2.introduce())

    
        
        