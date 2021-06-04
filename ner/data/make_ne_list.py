import sys
from collections import defaultdict
import pprint as pp


with open(sys.argv[1],'r') as f:
	for line in f.readlines():
		tmp = line.split('\t')
		if len(tmp) != 2:# new line
			continue
		token, ne_tag = tmp
		ne_tag = ne_tag[:-1]
		if ne_tag == 'O' or ne_tag == "":
			continue
		if ne_tag[0] == 'B':
			print()
			print(ne_tag[2:],end="\t")
		print(token,end="")
