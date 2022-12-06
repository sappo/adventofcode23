import os
import sys
from typing import List

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

import re
from utils import read


lines = read.read_puzzle(6)
datastream = lines[0].strip()

for i in range(len(datastream) - 4):
    sopm = set(datastream[i:i+4])
    if len(sopm) == 4:
        print(f"Start-of-package-marker is: {i+4}")
        print(datastream[i:i+4])
        break

for i in range(len(datastream) - 14):
    sopm = set(datastream[i:i+14])
    if len(sopm) == 14:
        print(f"Start-of-message-marker is: {i+14}")
        print(datastream[i:i+14])
        break
