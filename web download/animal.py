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
c=Cat()

print("a isAnimal?",isinstance(a,Animal))
print("a isAnimal?",isinstance(a,Dog))
print("a isAnimal?",isinstance(a,Cat))

print("d isAnimal?",isinstance(d,Animal))
print("d isAnimal?",isinstance(d,Dog))
print("d isAnimal?",isinstance(d,Cat))

run_twice(c)