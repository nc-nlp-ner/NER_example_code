import sys
from collections import defaultdict
import pprint as pp


with open(sys.argv[1],'r') as f:
	ne_dict = defaultdict(list)
	for line in f.readlines():
		ne_tag , word  = line.split('\t')
		ne_dict[word[:-1]].append(ne_tag)
	
	for word, ne_tags in ne_dict.items():
		if len(ne_tags) != 1:
			print(word,ne_tags,sep='\t')
