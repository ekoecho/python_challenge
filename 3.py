#!/usr/bin/python

import string
import re

infile = open("equality.html")
processme = infile.read().translate(None,'\n')

r = re.compile("[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]")
print r.findall(processme)
