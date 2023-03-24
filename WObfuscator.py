import argparse
import binascii
import bz2
import gzip
import lzma
import marshal
import os
import random
import time
import zlib

from rich.progress import Progress
from tkinter import Tk, filedialog

w = "\033[37m"  # white
R = "\033[31m"  # red
C = "\033[36m"  # cyan


def encode(source: str) -> str:
    selected_mode = random.choice((lzma, gzip, bz2, binascii, zlib))
    marshal_encoded = marshal.dumps(compile(source, "Scorch", "exec"))
    if selected_mode is binascii:
        encoded = binascii.b2a_base64(marshal_encoded)
    else:
        encoded = selected_mode.compress(marshal_encoded)
    if selected_mode is binascii:
        TMP = "import marshal,lzma,gzip,bz2,binascii,zlib;exec(marshal.loads(binascii.a2b_base64({})))"
        return TMP.format(encoded)
    else:
        TMP = "import marshal,lzma,gzip,bz2,binascii,zlib;exec(marshal.loads({}.decompress({})))"
        return TMP.format(selected_mode.__name__, encoded)


def getArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="Input file path")
    parser.add_argument("-o", "--output", help="Output file name")
    parser.add_argument("-s", "--strength", help="Obfuscation strength (default: 100)", default=100)
    args = parser.parse_args()

    if args.file:
        file_path = args.file
    else:
        root = Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename()

    if args.output:
        output_name = args.output
    else:
        output_name = input(f"{C}> {w}Enter output file name: ")
        if not output_name:
            output_name = os.path.join(os.path.dirname(os.path.abspath(__file__)), "obfuscated.py")

    strength = int(args.strength)

    return file_path, output_name, strength


def start():
    file_path, output_name, strength = getArgs()
    print(f"{C}> {w}Encoding " + file_path)
    with open(file_path, "rb") as f:
        source = f.read()
        with Progress() as progress:
            task1 = progress.add_task(f"{C}> {w}[white]Encoding...", total=strength)
            encoded = source
            for i in range(strength):
                encoded = encode(source=encoded)
                time.sleep(0.1)
                progress.update(task1, advance=1)

    with open(output_name, "w") as f:
        f.write(encoded)

    print(f"{C}> {w}Encoding successful!\n{C}> {w}Saved as '{C}{output_name}{w}'")
    print(f"\n{C}> {w}Press '{R}Enter{w}' to exit.")
    input()


if __name__ == "__main__":
    start()