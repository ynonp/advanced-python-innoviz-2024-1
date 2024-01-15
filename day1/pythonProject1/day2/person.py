from typing import *

class Person:
    age: int = 0
    def __init__(self, age: int):
        self.age = age

    def grow_up(self) -> None:
        if self.age < 120:
            self.age += 1
        else:
            raise Exception("You're dead")



class Classroom:
    students: Sequence[Person] = []
    def __init__(self, students: Sequence[Person]):
        self.students = students

    def teach(self):
        for s in self.students:
            s.grow_up()



p = Person(17)
q = Person(17)
t = Person(17)

people = (p, p, p)
people[0].grow_up()


c = Classroom([p, q, t])
c.teach()

print(p.age)




