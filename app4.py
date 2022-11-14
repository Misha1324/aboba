class Animal:
    name = ""
    ves = 0
    paroda = ""
    def golos(self):
        pass
    def ShowInfo(self):
        print("Name: ", self.name, "Paroda: ", self.paroda, "ves: ", self.ves)
#   дочерний класс Dog созданый на основе базового Animal
class Dog(Animal):
    def __init__(self, name, ves, paroda):
        self.name = name
        self.ves = ves
        self.paroda = paroda
    def golos(self):
        print("Gav gav")
#   дочерний класс Dog созданый на основе базового Animal
class Cat(Animal):
    def __init__(self, name, ves, paroda):
        self.name = name
        self.ves = ves
        self.paroda = paroda
    def golos(self):
        print("mau mau")


myDog = Dog("Bobik", 20, "staff")
myDog.showinfo()
myDog.golos()

myCat = Cat("Barsik", 5, "Bengas")
myCat.showinfo()
myCat.golos()

number = 100

myList = [number, 2, 3]

for i in myList:
    print(i)

myIterator = iter(myList)

#print(myIterator)
#print(next(myIterator))
#print(next(myIterator))
#print(next(myIterator))
#print(next(myIterator))

for elem in myIterator:
    print(elem)

class Counter:
    def __init__(self,max_number):
        self.max_number = max_number
        self.i = 0

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        self.i += 1
        if self.i > self.max_number:
            raise StopIteration
        return self.i

count = Counter(5)

print("===========================================")
for elem in count:
    print(elem)

for elem in count:
    print(elem)