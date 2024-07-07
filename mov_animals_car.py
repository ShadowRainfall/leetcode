class Moving:
    def __init__(self):
        self.move()

    def move(self):
        raise NotImplementedError('Move in %s.' % self.__class__.__name__)


class Animal(Moving):
    def voice(self):
        raise NotImplementedError('Voice in %s.' % self.__class__.__name__)


class Transport(Moving):
    def launch(self):
        raise NotImplementedError('Launch in %s.' % self.__class__.__name__)


class Duck(Animal):
    def voice(self):
        print('Duck quacks')

    def move(self):
        print('Duck swims')


class Tiger(Animal):
    def voice(self):
        print('Tiger roars')

    def move(self):
        print('Tiger runs')


class Car(Transport):
    status = bool()

    def move(self):

        if Car.status != True:
            print('Not launched')
        else:
            print('Car moves')

    def launch(self):
        print('Launched')
        Car.status = True


d = Duck()
t = Tiger()
c = Car()

print('--Duck--')
d.voice()
d.move()
print('--Tiger--')
t.voice()
t.move()
print('--Car--')
c.launch()
c.move()
