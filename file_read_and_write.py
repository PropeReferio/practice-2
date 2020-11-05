with open('test.txt', 'r') as rf:
	with open('test_copy.txt', 'w') as wf:
		for line in rf:
			wf.write(line)
	#Above block copies from one file (test.txt) to another (test_copy.txt)
with open('bo-stevens-headshot.jpg', 'rb') as rf:
	with open('bo_copy.jpg', 'wb') as wf: #Mode must be binary for images!
		chunk_size = 4096
		rf_chunk = rf.read(chunk_size)
		while len(rf_chunk) > 0:
			wf.write(rf_chunk)
			rf_chunk = rf.read(chunk_size)