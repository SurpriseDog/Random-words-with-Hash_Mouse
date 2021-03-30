#!/usr/bin/python3
#Randomly choose words from a list using hash_mouse to sample the mouse position and time in another thread
#Usage: ./ranword.py <wordfile>


from shutil import get_terminal_size
import time
import sys

try:
	from Xlib import display
except ImportError:
	print("Can't hash mouse movements because Xlib not installed.")
	print("This will limit randomness to that provided by the secrets module (still very good!)")
	print("To install: sudo apt install python3-xlib")
	import secrets
	class Hash_Mouse:
		def __init__(self, *args, **kargs):
			self.count = 0
		def ensure_min(self, *args):
			pass
		def randint(self, count):
			return secrets.randbelow(count)
else:
	from hash_mouse import Hash_Mouse


def load_words(filename):
	#Read the words into a list
	words = []
	count = 0
	print("Loading words:", end='')
	with open(filename) as f:
		for word in f:
			word = word.strip()
			if word.startswith('#'):
				continue
			words.append(word)
			count += 1
			if not count % 10000:
				print('.', end='', flush=True)
	print()
	return words



if __name__ == "__main__":
	if len(sys.argv) > 1:		
		filename = sys.argv[1]
	else:
		filename = '/usr/share/dict/words'

	words = load_words(filename)

	mhash = Hash_Mouse(verbose=0)
	mhash.ensure_min(16)
	print("Ready! Mouse movements will continue to be hashed in the background.")
	print("The number in the left column shows the sample count")

	print("\n\nPress ctrl+c to quit. ")
	term_width = get_terminal_size()[0]
	line = str(mhash.count)

	while True:
		choice = words[mhash.randint(len(words))]
		new = line + ' ' + choice
		if len(new) < term_width:
			line = new
		else:
			print(line)
			time.sleep(1)
			line = str(mhash.count)
		
	
