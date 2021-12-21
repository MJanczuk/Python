from os import listdir
from os.path import isfile, join

mypath = './Dane surowe'
#mypath = './Python'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print(onlyfiles)

from os import walk

filenames = next(walk(mypath), (None, None, []))[2]  # [] if no file
print(filenames)

import glob
print(glob.glob(mypath+'/*.rec'))