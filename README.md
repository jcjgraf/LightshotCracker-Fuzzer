# Lightshot Cracker/Fuzzer
### Shows you the images other people upload to Lightshot and let you save them

---

This script iterates though images other people upload to [LightShot](https://prnt.sc). Your are not just able to see these images, but you can also downlad and save them on your system.

---

## Installation
1. Download the package
2. The script depends on some other packages, which can be installed with e.g. `pip`:
```
pip install requests lxml matplotlib urllib
```
## Usage
1. Run the script with python 3, e.g. `python3 urlCracker.py`
2. You are prompted for a 6 digit string. You have two posibilities now:
	* Eighter enter a random 6 digit long string consisting of all number and lower case letters.
	* or upload an image to [Lighthot](https://prnt.sc) eighter inbrowser or via the app. Copy the last six digits from the given URL and pass it to the script.
3. After clicking `Enter` the script starts showing you the images. If it repeatedly says that no image can be found, repeat step two with another input string.
4. Dismiss the image with `CTRL + W`(or just close the plot) or save it by clicking on the save icon on the plot


## TODO
* Make the script much faster by preloading new images


## What you should learn from this project
Newer upload anything private via Lightshot or similar uploader, since everyone can see it!