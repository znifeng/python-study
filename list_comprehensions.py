#!/usr/bin/python
# -*- coding: utf-8 -*
__author__ = 'zni.feng'
import os

l1 = range(1,11)

l2 = [x * x for x in l1]

l3 = [x * x for x in l1 if x%2==0]

l4 = [m+n for m in 'ABC' for n in 'XYZ']

l5 = [d for d in os.listdir('.')]

dict = {'x':'A' , 'y':'B', 'z':'C'}
for k,v in dict.iteritems():
	print k,'=',v

l6 = [k+'='+v for k,v in dict.iteritems()]

print 'l1: ' , l1 
print 'l2: ', l2
print 'l3: ', l3
print 'l4: ', l4
print 'l5: ', l5
print 'l6: ', l6