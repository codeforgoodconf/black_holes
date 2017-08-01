import sys
with open(sys.argv[1], 'r') as f:
	for line in f:
		print ','.join(line.strip().split(',')[1:])