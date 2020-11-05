with open('test.txt', 'r') as f: #Avoids the need to .close() Best practice
	print('name:', f.name) # See rthe file's name
	print('mode: ', f.mode) # Read mode, write mode, etc.
	
	size_to_read = 10

	f_contents = f.read(size_to_read)

	while len(f_contents) > 0:
		print(f_contents, end='*')
		print(f.tell()) #Tells us how far into the file we are
		f_contents = f.read(size_to_read)
	
	f.seek(5) # Go back to the 5th character of the file
	print('back to the 5th char...')

	for line in f: # This is a good practice, because with large files, taking the whole contents can be a memory issue. This
		print(line, end='') #Eliminates this problem.
	
	f_contents = f.read(20) # Only the first 20 characters
	print(f_contents)
	# print('f.readline(): ', f.readline())
	# print('f.readlines(): ', f.readlines())
	# f_contents = f.readline()
	# print(f_contents, end='') # Default end is \n, newline. This eliminates spaces.
	# f_contents = f.readline()
	# print(f_contents)
# f.close() # Always close after open()