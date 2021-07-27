class LandAnimal:
    def walk(self):
        print('walk')

class WaterAnimal:
    def swim(self):
        print('swim')
    # def walk(self):
    #     print('water walk')

class Amphibian(WaterAnimal, LandAnimal):
    pass

frog = Amphibian()

frog.swim()
frog.walk()

