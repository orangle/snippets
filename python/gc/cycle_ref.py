import gc
import sys 

class Student(object):
    def __init__(self, name, classroom):
        self.name = name 
        self.classroom = classroom

class ClassRoom(object):
    def __init__(self):
        self.students = []

    def add(self, name):
        self.students.append(Student(name, self))

room = ClassRoom()
print sys.getrefcount(room)
print gc.get_referents(room)

room.add("lzz")
print sys.getrefcount(room)
room.add("cc")
print sys.getrefcount(room)

