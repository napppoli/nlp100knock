#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sys
def split():
	with open(sys.argv[1],'r') as f:
		dataline=f.readlines()
	n=int(sys.argv[2])   
	ran=len(dataline)//n
	for i in range(ran):
		with open('out%s.txt' % chr(ord('a')+i),'w') as f:
			f.writelines(dataline[ran*i:min(ran*(i+1),len(dataline))])

split()
