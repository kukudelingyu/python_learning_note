
class Animal:
    def speak(self):
        pass


class Cat(Animal):
    def speak(self):
        print("喵喵喵")


class Dog(Animal):
    def speak(self):
        print("汪汪汪")


def make_noise(animal: Animal):
    animal.speak()

dog = Dog()
cat = Cat()

make_noise(dog)
