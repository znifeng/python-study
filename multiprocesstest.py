#!/usr/bin/python
# -*- coding: utf-8 -*
__author__ = 'zni.feng'
import  sys
reload (sys)
sys.setdefaultencoding('utf-8')

from multiprocessing import Process
import os
import time

#子进程fun
def child_projcess_fun(name):
	print 'Child process %s with processId %s starts.' % (name, os.getpid())
	time.sleep(3)
	print 'Child process %s with processId %s ends.' % (name, os.getpid())

if __name__ == "__main__":
	print 'Parent processId is: %s.' % os.getpid()
	p = Process(target = child_projcess_fun, args=('zni',))
	print 'Process starts'
	p.start()
	p.join()
	print 'Process ends.'