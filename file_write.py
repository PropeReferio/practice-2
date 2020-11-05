with open('test2.txt', 'w') as f:
	f.write('Test')
	f.seek(0) #Goes back to start, overwrites
	f.write('N') #This will only overwrite the first letter of 'Test'