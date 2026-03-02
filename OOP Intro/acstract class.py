from abc import ABC,abstractmethod
class Bird(ABC):
    @abstractmethod
    def makesound(self):
        pass
    
class Sparrow(Bird):
    def makesound(self):
        print("Chirp...chirp...chirp...!")
        
class Dove(Bird):
    def makesound(self):
        print("Coo...coo...coo...!")
        
class Crow(Bird):
    def __init__(self):
        print("Kaale hai toh kya huwa dilwale hai!!!")
    def makesound(self):
        print("Caw...caw...caw...!")
    
        
bird = [Sparrow(),Dove(),Crow()]
for item in bird:
    item.makesound()
    