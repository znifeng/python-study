#!/usr/bin/python
# -*- coding: utf-8 -*
__author__ = 'zni.feng'
import  sys
reload (sys)
sys.setdefaultencoding('utf-8')
import threading, multiprocessing

def loop():
	print 'thread %s starts' % threading.current_thread().name
	x= 1 
	while True:
		x *= 1

for i in range(2):
	t = threading.Thread(target= loop)
	t.start()
