#!/usr/bin/python
# -*- coding: utf-8 -*
__author__ = 'zni.feng'
import  sys
reload (sys)
sys.setdefaultencoding('utf-8')
from multiprocessing import Process, Pipe
import os, time, random

#发送数据进程
def send(child_pipe, name):
	print 'Child Process %s starts' % name
	child_pipe.send('This is Mr.Ni')
	child_pipe.close()
	time.sleep(random.random())
	print 'Child Process %s ends' % name

#接收数据进程
def recv(parent_pipe, name):
	print 'Child Process %s starts' % name
	print parent_pipe.recv()
	time.sleep(random.random())
	print 'Child Process %s ends' % name

if __name__ == "__main__":
	#创建管道
	parent,child = Pipe()
	#创建send进程
	ps = Process(target=send, args=(child, 'SEND'))
	#创建recv进程
	pr = Process(target=recv, args=(parent, 'RECEIVE'))
	#启动send进程
	ps.start()
	#等待send进程结束
	ps.join()
	#启动recv进程
	pr.start()
	#等待recv进程结束
	pr.join()
	print 'Test finish.'