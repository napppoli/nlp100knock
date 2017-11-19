#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sys
with open(sys.argv[1],'r') as f:
	lines=f.readlines()
#lines=[x.split() for x in lines]
#lines.sort(key=lambda line:line[2],reverse=True)
#print('\n'.join(['\t'.join(x) for x in lines]))

for line in sorted(lines, key=lambda x:x.split()[2],reverse=True):
	print(line)
