#!/usr/bin/env python

import requests

request_code = 200
nextnum="12345"
while request_code == 200:

  result = requests.get("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="+nextnum)
  nextnum=result.content.split(' ')[-1]

  print result.content
  request_code = result.status_code
