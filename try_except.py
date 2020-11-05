
try:
	f = open('corrupt.txt')
	# var = bad_var
	if f.name == 'corrupt.txt':
		raise Exception
except FileNotFoundError:
	print('Sorry, that file doesn\'t exist.')
except NameError as e:
	print('There was a problem with a variable name: ', e)
except Exception:
	print('Error!')
else:
	#This block fires when the try block has no problem
	print(f.read())
	f.close()
finally:
	#This always happens, regardless of errors
	# Useful for closing files, closing connections, etc.
	pass