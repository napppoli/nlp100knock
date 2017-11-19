#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys
with open(sys.argv[1],'r') as f:
	lines=f.readlines()

lines=[x.split()[0] for x in lines]
lines.sort()
print(set(lines))

