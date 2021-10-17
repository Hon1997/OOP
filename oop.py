
class amigos:
    def __init__(self,name,age,skincolor):
        self.name=name
        self.age=age
        self.skincolor=skincolor
    def amigoinfo(self):
        print(f"{self.name}  is {str(self.age)}  and his skin color is   {self.skincolor}")
    def birthday(self):
        self.age+=1
Honore=amigos("Honore",24,"Blown")
Jerome=amigos("Jerome",25,"Black")
James=amigos("James",26,"White")

Honore.amigoinfo()
Jerome.amigoinfo()
James.amigoinfo()
    
Honore.birthday()
print(f"New Honore's age {Honore.age}")
    