#Rahul Pycalc v0.2
class Calculator():

	name = None

	def __init__(self, name):
		self.name = name

	def add(self, a , b):
		addresult = a+b	
		return(addresult)

	def sub(self, a , b):
		return(a-b)

	def times(self, a , b):
		return(a*b)

	def div(self, a , b):
		return(a/b)
obj1 = Calculator("Pycalc")
print("Welcome to pycalc v0.2")
a = float(input("What is the first number?  "))
b = float(input("What is the second number?  "))
c = input("What do you want to do?(+ , - , / , *)  ")
if c == "+":
	results = obj1.add(a,b)
elif c == "-":
	results = obj1.sub(a,b)
elif c == "/":
	results = obj1.div(a,b)
elif c == "*":
	results = obj1.times(a,b)
else:
	results = "Invalid"
print(results)

