# Building some classes

class Car():
	def __init__(self, color, num_wheels, trans):
		self.color = color
		self.num_wheels = num_wheels
		self.trans = trans

	def get_stats(self):
		print(f"This is a {self.color} car with {self.num_wheels} wheels and an\
 {self.trans} transmission.")

class Honda(Car):
	def __init__(self, model, color, num_wheels, trans):
		super().__init__(color, num_wheels, trans)
		self.model = model

	def get_stats(self):
		print(f"This is a {self.color} Honda {self.model} with {self.num_wheels} wheels and an\
 {self.trans} transmission.")

crv = Car('maroon', 4, 'automatic')
crv.get_stats()

civic = Honda('Civic', 'green', 4, 'manual')
civic.get_stats()