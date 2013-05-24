#!/usr/bin/env python
#k->m
#o->q
#e->g
import string
scrambled ="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
scrambled2 = "map"
intab = string.lowercase
outtab = string.lowercase[2:26]+string.lowercase[0:2]

print intab
print outtab
trantab = string.maketrans(intab,outtab)

print scrambled.translate(trantab)
print scrambled2.translate(trantab)
