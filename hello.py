#!/usr/bin/env python3
import collections

print("hello world")
L=[x*x for x in range(1,11) if x%2==0]
print(L)
if isinstance([],collections.Iterable):
	print("true")

class Student(object):

    def __init__(self,name,score):
        self.__name = name
        self.__score = score

    def getName(self):
    	return self.__name

    def getScore(self):
    	return self.score


class Teacher(object):
	def __init__(self,name,score):
		self.name = name
		self.score = score

bar = Student('abc',50)
print(bar.getName())

bar._Student__name = 'cedee'

print(bar.getName())

tar = Teacher('abad',30)
print(tar.name,tar.score)

class People(object):
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

p = People()
p.birth=100
print(p.birth)

class Fib(object):
    def __init__(self):
        self.a,self.b=1,2

    def __iter__(self):
        return self

    def __next__(self):
        self.a,self.b=self.b,self.a + self.b
        if self.a > 100:
            raise StopIteration()
        return self.a

for n in Fib():
    print(n)

def foo(s):
    n = int(s)
    if n == 0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n

def bar():
    try:
        foo('1')
    except ValueError as e:
        print('ValueError!',e)

bar()