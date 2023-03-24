# WObfuscator
Python obfuscator, part of upcoming Wratheon RAT tool. Easy to implement into a project to obfuscate code for "any" reason

Obfuscates files using various encoding techniques like lzma, gzip, bz2, binascii, and zlib. The obfuscation strength can be adjusted using the "-s" or "--strength" flag, with a default value of 100.

If run with no arguments, opens a file dialog to select file to obfuscate and then type output name to console

Usage with arguments: `python obfuscator.py [-f FILE] [-o OUTPUT] [-s STRENGTH]`

Example: `python WObfuscator.py -f FileToObfuscate.py -o "Output.py"`

Optional:
-h for help message
-s leave empty for default

