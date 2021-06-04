import sys



with open(sys.argv[1], 'r') as f:
	for line in f.readlines():
		line = line.strip()
		if len(line) == 1:
			print(line)
