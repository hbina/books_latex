#!/usr/bin/python3

import subprocess
import os
import string
import sys

print(f"Number of arguments:{len(sys.argv)}")
print(f"Argument List:{str(sys.argv)}")

rootDir = '.'
for dirName, subdirList, fileList in os.walk(rootDir):
    for fname in list(filter(lambda x: x.endswith(".tex"), fileList)):
        tex_file = "{}/{}".format(dirName, fname)
        print("compiling:{}".format(tex_file))
        subprocess.run(args=["tectonic",
                             "--keep-intermediates",
                             "--print",
                             tex_file])
