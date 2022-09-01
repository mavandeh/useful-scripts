#!/usr/bin/python

import os

findtext = input('Input text to find:\n')
replacetext = input('Input text to replace with:\n')

for path, dirs, files in os.walk("."):
	for file in files:
		newname = file.replace(findtext, replacetext)
		try:
			os.rename(os.path.join(path, file), os.path.join(path, newname))
		except:
			print("File not renamed, probably permissions issue: " + file)



	