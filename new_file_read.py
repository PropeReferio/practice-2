with open('logfile.txt', 'r') as log:
	log_contents = log.readline()

	while len(log_contents) > 0:
		print(log_contents, end='')
		print('Where? ', log.tell())
		log_contents = log.readline()

	log.seek(0)
	for line in log:
		print(line, end='')