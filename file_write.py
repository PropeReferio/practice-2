with open('test2.txt', 'w') as f:
	f.write('Test')
	f.seek(0) #Goes back to start, overwrites
	f.write('N') #This will only overwrite the first letter of 'Test'

with open('corrupt.txt', 'w') as f:
	#In this example, corrupt.txt is created even though
	#We don't do anything to it
	f.seek(0)