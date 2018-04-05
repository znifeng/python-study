#!/usr/bin/python
# -*- coding: utf-8 -*
__author__ = 'zni.feng'
import sys

l=[9,7,5,4,2,1]

def isInOrder(index):
	if index<0 or index>= len(l):
		sys.exit('Invalid index.')

	if index==0:
		return True

	if l[index]>l[index-1]:
		return True
	
	return False

re = map( isInOrder, xrange(len(l)) )
print re
print all(re)
print any(re)