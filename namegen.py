import string, sys
from collections import defaultdict
from math import sqrt
from random import choice, gauss, randint, random

def name_len_mean_stdev(names):
	mean = 0.0
	for name in names:
		mean += len(name)*1.0/len(names)

	variance = 0.0
	for name in names:
		variance += ((len(name) - mean)**2)*1.0/len(names)

	stdev = sqrt(variance)

	return mean, stdev
		

def next_letter(letter1, letter2, trigrams):
	subdict = trigrams[letter1][letter2]
	freqs = dict()

	normalizer = 0
	for _, v in subdict.iteritems():
		normalizer += v

	cdf = 0.0
	rnum = random()
	for letter, count in subdict.iteritems():
		cdf += count*1.0/normalizer
		if rnum <= cdf:
			return letter


def main():
	if len(sys.argv) < 3:
		print "USAGE: python %s <corpus_file> <#names>" % (sys.argv[0])
		quit()

	trigrams = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))

	# Open corpus & retrieve names
	corpus_file = sys.argv[1]
	names = []
	with open(corpus_file, 'r') as f:
		names = [string.strip(x).lower() for x in f.readlines()]

	# Build trigram frequencies
	for name in names:
		for c in range(len(name)-2):
			trigrams[name[c]][name[c+1]][name[c+2]] += 1

	# Make names!
	num_names = 0
	try:
		num_names = int(sys.argv[2])
	except:
		print "expected an integer value for #names; got \"%s\"" % (sys.argv[2])
		quit()
	for i in range(num_names):
		name = ""
		rname = choice(names)
		name = rname[0] + choice([c for c in trigrams[rname[0]].keys() if c in "aeiou"])
		mean_len, stdev_len = name_len_mean_stdev(names)
		exp_len = gauss(mean_len, stdev_len)
		while True:
			nl = next_letter(name[-2], name[-1], trigrams)
			if not nl or len(name) > exp_len:
				print name
				break

			name = name + nl

if __name__ == "__main__":
	main()
