#!/usr/bin/env python3

class Animal:
	def __init__(self, name):
		self.name=name
	def talk(self):
		raise NotImplementedError ("Subclass must implement talk method")

class Cat(Animal):
	def blah():
		pass
	def talk(self):
		return "Meow"

class Dog(Animal):
	def blah():
		pass
	def talk(self):
		return "Woof! Woof!"

if __name__ == "__main__":
	c=Cat("Maxine")
	d=Dog("Walter")
	
	c.talk()
	d.talk()
	
	animals=[Cat("Maxine"),Dog("Walter"), Dog("Boone")]
	for animal in animals:
		print (animal.name +': ' + animal.talk())