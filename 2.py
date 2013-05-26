#!/usr/bin/python

import string

infile = open("ocr.html")
processme = infile.read()
for character in string.punctuation:
  if processme.count(character)>4:
    processme = processme.translate(None,character) 

print processme.translate(None,'\n')
