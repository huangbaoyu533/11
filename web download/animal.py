class Animal(object):
    def run(self):
        print('animal is running')
class Dog(object):
    def run(self):
        print('Dog is running')
class Cat(object):
    def run(self):
        print('Cat is running')
def run_twice(animal) :
    animal.run()
    animal.run()
a=Animal()
d=Dog()
