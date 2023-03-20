class Mobile:
    def __init__(self,model,ram,rom):
        self.model = model
        self.ram = ram
        self.rom = rom
    def details(self,lol):
        print(f"My phone name is {self.model} and it's Ram is {self.ram}")
        
        
obj1 = Mobile('rellme8', 8, 128)
obj1.details('lol')

print(obj1.model)