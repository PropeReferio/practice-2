def decorator_function(orig_func):
	def wrapper_func(*args, **kwargs): #Args and kwargs enable the passing of
		# any number of arguments
		print(f"Wrapper executed this before {orig_func.__name__}")
		return orig_func(*args, **kwargs)
	return wrapper_func


def timer(orig_func):
	import time

	def wrapper_func(*args, **kwargs):
		start = time.time()
		result = orig_func(*args, **kwargs)
		stop = time.time() - start
		print(f"Time elapsed: {stop}")
		return result

	return wrapper_func


class decorator_class(object):

	def __init__(self, orig_func):
		self.orig_func = orig_func

	def __call__(self, *args, **kwargs):
		print(f"call method executed this before {self.orig_func.__name__}")
		return self.orig_func(*args, **kwargs)

# @decorator_class
@timer
def woop(name='johnny'):
	print(f"{name} {name} WOOP {name}")

woop('janie')
woop()

# def display():
# 	print('display function ran')

# decorated_display = decorator_function(display)

# decorated_display()

@decorator_function #This block will do the same thing as the block above
def display(): #The decorator function takes the function on the following line
	print('display function ran') #as its argument

@decorator_function
def print_info(name, age):
	print(f"My name is {name} and I'm {age} years old.")

print_info('Bo', 39)
display()
