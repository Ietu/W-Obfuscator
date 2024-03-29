pip install -r requirements.txt

# WObfuscator
Python obfuscator, part of upcoming Wratheon RAT tool. Easy to implement into a project to obfuscate code for "any" reason.

Obfuscates files using various encoding techniques like lzma, gzip, bz2, binascii, and zlib. Encoding method is randomized each time. The obfuscation strength can be adjusted using the "-s" or "--strength" flag, with a default value of 100.

If run with no arguments, opens a file dialog to select file to obfuscate and then type name of output file to console.

## Usage

Usage with arguments: `python obfuscator.py [-f FILE] [-o OUTPUT] [-s STRENGTH]`

Example: `python WObfuscator.py -f FileToObfuscate.py -o "Output.py"`

**Obfuscated output file can be ran regularly as a python file of course.**

Optional:
-h for help message
-s leave empty for default strength


Example code before obfuscator:

![cd81d47067aa9b3b4cbcb48d42a161b0](https://user-images.githubusercontent.com/54209182/227574283-3fad5f4e-1244-4934-8e61-fd661cc53cd9.png)



After obfuscator:

![3742704b40801444afa58f1ca4605237](https://user-images.githubusercontent.com/54209182/227574315-fe4dedc1-464d-4dd5-95b6-ba4eb93c80fe.png)
