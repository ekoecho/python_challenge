#!/usr/bin/env python

import zipfile
import sys

myfile = zipfile.ZipFile("zip/channel.zip")

nextnum="12345"
nextfile="90052"
while True:

  result = open("zip/"+nextfile+".txt","r").readlines()
  #print result
  nextfile=result[0].split(' ')[-1]
  #for line in result:
    #print line
  sys.stdout.write(myfile.getinfo(nextfile+".txt").comment)

