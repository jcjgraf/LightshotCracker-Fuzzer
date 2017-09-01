#!/usr/bin/env python3

#############
# LIBRARIES #
#############

import requests
from lxml import html

import matplotlib.pyplot as plt
import urllib


#############
# VARIABLES #
#############

numListS2V = {'0': 0,
		 '1': 1,
		 '2': 2,
		 '3': 3,
		 '4': 4,
		 '5': 5,
		 '6': 6,
		 '7': 7,
		 '8': 8,
		 '9': 9,
		 'a': 10,
		 'b': 11,
		 'c': 12,
		 'd': 13,
		 'e': 14,
		 'f': 15,
		 'g': 16,
		 'h': 17,
		 'i': 18,
		 'j': 19,
		 'k': 20,
		 'l': 21,
		 'm': 22,
		 'n': 23,
		 'o': 24,
		 'p': 25,
		 'q': 26,
		 'r': 27,
		 's': 28,
		 't': 29,
		 'u': 30,
		 'v': 31,
		 'w': 32,
		 'x': 33,
		 'y': 34,
		 'z': 35}


############
# FUNCTION #
############

def showImage(url):
	"""
		Displays the image of the given URL with Matplotlib
	"""
	with requests.Session() as c:
		sourceCode = c.get(url).content

	try:
		tree = html.fromstring(sourceCode)
		imgURL = tree.xpath('//img/@src')[1]

		req = urllib.request.Request(imgURL, headers={'User-Agent': 'Mozilla/5.0'})			# Change the useragent in order to prevent blocking
		f = urllib.request.urlopen(req)

		img = plt.imread(f)

		fig_size = plt.rcParams["figure.figsize"]
		# fig_size[0] = 12
		# fig_size[1] = 9
		plt.rcParams["figure.figsize"] = fig_size

		print("ImageURL:" + imgURL)

		plt.imshow(img)
		plt.xticks([]), plt.yticks([])
		plt.show()
	except Exception as e:
		print(e)
		print("Image does no longer exist. If it continous like this you might want to change your staring number")


def incrementUrl(url):
	"""
		Converts the last six base 36 number of the url to denary, adds one and converts it back to base 36. Returns the following url, unless the last possible on is reached, then it will return the first one.
	"""
	dataNumber = url[-6:]

	# Convert base 36 number to base 10
	den = 0
	for digit in dataNumber:
		value = numListS2V[digit]
		den *= 36
		den += value
	
	# Make sure that we don't exceede the max 6 digit base 36 value
	if den + 1 <= 2176782335:
		den += 1
	else:
		den = 0

	# Convert the eenary back to base 36
	numListV2S = dict(map(reversed, numListS2V.items()))

	numArray = []
	while den:
		den, value = divmod(den, 36)
		numArray.append(numListV2S[value])

	dataNumber = str(''.join(reversed(numArray)))

	while len(dataNumber) < 6:
		dataNumber = "0" + dataNumber

	return "http://prntscr.com/" + dataNumber


########
# MAIN #
########

if __name__ == '__main__':
	try:
		url = "http://prntscr.com/" + input("Enter a random 6 digits long string containing just lowercase letters and all numbers. If most of the images don't exist anymore, you might have to restart the script and enter a different string\n")
		while True:
			# Check if image still exists
			showImage(url)

			url = incrementUrl(url)


	except KeyboardInterrupt:
		print("Exit\n")


