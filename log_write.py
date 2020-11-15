import time, random

log_msg = ['New user added', 'New blog post', 'New message received']
num_logs = random.randint(5,15)
delay = random.uniform(0.5, 2.0)
print('num_logs:', num_logs)
print('delay:', delay)
print(time.asctime())

with open ('logfile.txt', 'w') as log:
	log.seek(0)
	log.write('Logfile Started')
	for i in range(num_logs):
		time.sleep(delay)
		log.write('\n' + time.asctime() + ' ' + log_msg[random.randint(0,2)])
	log.write('\nLogging complete')
	