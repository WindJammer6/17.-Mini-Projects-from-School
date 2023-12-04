import math

class Vector():

	# possible directions
	_directions = ["up", "left", "down", "right"]
	# unit vectors and their corresponding directions 
	_unit_vectors = {(0, 1):"up", (-1, 0):"left", (0, -1):"down", (1, 0):"right"}

	def __init__(self, x, y):
		"""
		1) Takes in integers/floats as x and y coordinates

		2) Initialises vector with x and y coordinates provided

		3) Calculates x and y components of this vector's unit vector

		4) Compares this unit vector against the unit_vectors dictionary and assigns the corresponding
		string to the 'dir' attribute
		"""
		self._hash = None
		self._x = round(x, 10)
		self._y = round(y, 10)
		unit_x =  0 if not x else x/abs(x) # assigns 0 if x is 0, 1 if x is positive, -1 if x is negative
		unit_y =  0 if not y else y/abs(y) # ditto, for y
		self._dir = self._unit_vectors.get((unit_x, unit_y))

	@property
	def x(self):
		"""Getter method for vector's x component
		"""
		return self._x

	@x.setter
	def x(self, new_x):
		"""Setter method for vector's x component
		"""
		self._x = round(new_x, 10)
	
	@property
	def y(self):
		"""Getter method for vector's y component
		"""
		return self._y

	@y.setter
	def y(self, new_y):
		"""Setter method for vector's y component
		"""
		self._y = round(new_y, 10)

	@property
	def dir(self):
		"""Getter method for vector's direction
		"""
		return self._dir

	@dir.setter
	def dir(self, new_dir):
		"""Setter method for vector's direction
		"""
		self._dir = new_dir 

	@property
	def directions(self):
		"""Getter method for vector's possible directions
		"""
		return self._directions

	def translate(self, translater):
		"""
		1) Takes in a vector object 'translater'

		2) Adds translater vector's x and y components to self's x and y components respectively
		"""
		self.x += translater.x
		self.y += translater.y

	def rotate(self, new_dir):
		"""
		1) Takes in a string 'new_dir', which must be in the 'directions' class attribute 

		2) Uses indexes of 'new_dir' and 'self.dir' in the 'directions' class attribute to determine the
		direction and number of quadrants to rotate the vector

		3) Cancels rotation if the angle is 0 or 180 degrees

		4) Uses formula from https://matthew-brett.github.io/teaching/rotation_2d.html to calculate and
		assign new x and y components after rotation
		"""
		prev_dir = self.dir

		quadrants_to_rotate = self._directions.index(new_dir) - self._directions.index(prev_dir)
		if abs(quadrants_to_rotate) == 2:
			print("attempt to reverse direction detected, input blocked")
			return
		if abs(quadrants_to_rotate) == 0:
			print("specified direction is the same as current direction")
			return

		self.dir = new_dir
		angle =  math.pi/2 * quadrants_to_rotate
		sine = math.sin
		cosine = math.cos
		x = self.x
		y = self.y
		self.x = x*cosine(angle) - y*sine(angle)
		self.y = x*sine(angle) + y*cosine(angle)

	def copy(self):
		"""Returns a copy of the vector itself
		"""
		return type(self)(self.x, self.y)

	def __eq__(self, other):
		"""Overrides __eq__ method to let '==' operator return True if both vectors being compared have
		identical x and y components. 
		"""
		if isinstance(other, Vector):
			return self.x == other.x and self.y == other.y
		return NotImplemented

	def __hash__(self):
		"""Makes vector class hashable again after overriding __eq__
		"""
		if self._hash is None:
			pair = (self.x, self.y)
			self._hash = hash(pair)
		return self._hash