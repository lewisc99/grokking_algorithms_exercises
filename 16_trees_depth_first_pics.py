from os import listdir
from os.path import isfile, join
from collections import deque

def printnames(dir):
    for file in sorted(listdir(dir)):
      fullpath = join(dir, file)
      if isfile(fullpath):
        print(file)
      else:
        printnames(fullpath)

printnames("C://Users//Pichau//Desktop//pics")