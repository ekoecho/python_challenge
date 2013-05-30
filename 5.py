#!/usr/bin/env python
import pickle
import sys

mydata = pickle.load(open("banner.p","rb"))
for item in mydata:
  for subitem in item:
    sys.stdout.write(subitem[0]*subitem[1])
  print "\n"

