def decorator_function(orig_func):
	def wrapper_func():
		print(f"Wrapper executed this before {orig_func.__name__}")
		return orig_func()
	return wrapper_func

# def display():
# 	print('display function ran')

# decorated_display = decorator_function(display)

# decorated_display()

@decorator_function #This block will do the same thing as the block above
def display(): #The decorator function takes the function on the following line
	print('display function ran') #as its argument

display()