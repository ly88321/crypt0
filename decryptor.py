#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  decryptor.py
#  
#  Copyright 2018 
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  


from Crypto.Hash import SHA256
from Crypto.Cipher import AES
from Crypto import Random
from pathlib import Path
from sys import stdout
import time, os, base64


blue = "\033[94m"
red = "\033[91m"
end = "\033[0m"


print(red+"""

\t
\t               |
\t               |
\t          -----+------        -----------
\t               |                                   
\t               |
\t    )                                           (
\t    \ \                                       / /
\t     \ |\                                   / |/
\t      \|  \                               /   /
\t       \   |\         --------          / |  /
\t        \  |  \_______________________/   | /
\t         \ |    |      |      |      |    |/
\t          \|    |      |      |      |    /
\t           \____|______|______|______|___/



\t             By: @ly88321
\t          https://github.com/ly88321/crypt0

"""+end)




def write(word):
	stdout.write(word+"                                         \r")
	stdout.flush()
	return True



def getkey(key):
	key = SHA256.new(key)
	return key.digest()


def decrypt(key, filename):
	buffersize = 64 * 1024
	outputfile = filename.split('.hacklab')[0]

	with open(filename, 'rb') as infile:
		filesize = int(infile.read(16))
		IV = infile.read(16)
		decryptor = AES.new(key, AES.MODE_CBC, IV)

		with open(outputfile, 'wb') as outfile:
			while True:
				buf = infile.read(buffersize)

				if len(buf) == 0:
					break

				outfile.write(decryptor.decrypt(buf))
			outfile.truncate(filesize)


list_f = []


p = path('C:\\',
         'D:\\',
         'E:\\',
         'F:\\',
         'G:\\',
         'I:\\',
         'J:\\',
         'K:\\',
         'L:\\',
         'M:\\',
         'N:\\',
         'O:\\',
         'P:\\',
         'Q:\\',
         'R:\\',
         'S:\\',
         'T:\\',
         'U:\\',
         'V:\\',
         'W:\\',
         'X:\\',
         'Y:\\',
         'Z:\\')
key = "aGFja2xhYg=="

try:
	searche = list(p.glob('**/*.hacklab'))
	for x in searche:
		x = str(x)
		#x = x.split("/")[-1]
		list_f.append(x)
		#print(x)

except OSError:
	pass

for i in list_f:
	name = i.split("\\")[-1]
	path = i.replace(name, "")
	write(blue + "[*]Decryption: " + end + str(name))
	os.chdir(path)
	decrypt(getkey(base64.b64decode(key)), name)
	os.remove(name)

print("\n* Done *")
