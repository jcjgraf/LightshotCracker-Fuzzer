#!/usr/bin/env python3

#############
# LIBRARIES #
#############

import requests
from lxml import html


############
# FUNCTION #
############

# def setupBrowser

def getImage(url):
	with requests.Session() as c:
		sourceCode = c.get(url).content

	tree = html.fromstring(sourceCode)

	img = tree.xpath('//img/@src')[1]

	print(img)

	# witeToFile(sourceCode)

def witeToFile(toSave):
	with open('test.html', 'w') as file:
		file.write(str(toSave))


########
# MAIN #
########

if __name__ == '__main__':
	getImage("http://prntscr.com/gfpo6w")


