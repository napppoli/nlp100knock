#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys
with open(sys.argv[1],'r') as f:
	line=f.readlines()
line=[x.split()[0] for x in line]
#d=list(sorted({i:line.count(i) for i in set(line)}.items(), key=lambda x:x[1],reverse=True))
#print('\n'.join([x[0] for x in d]))
for x in list(sorted({i:line.count(i) for i in set(line)}.items(), key=lambda x:x[1],reverse=True)):
	print (x[0])
