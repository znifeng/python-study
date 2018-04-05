#!/usr/bin/python
# -*- coding: utf-8 -*
__author__ = 'zni.feng'
import  sys
reload (sys)
sys.setdefaultencoding('utf-8')
from multiprocessing import Process, Queue, Lock
import os, time, random
#写数据进程
def write(q, lock, name):
	print 'Child Process %s starts' % name
	#获得锁
	lock.acquire()
	for value in ['A' , 'B', 'C']:
		print 'Put %s to queue...' % value
		q.put(value)
		time.sleep(random.random())
	#释放锁
	lock.release()
	print 'Child Process %s ends' % name

#读数据进程
def read(q, lock, name):
	print 'Child Process %s starts' % name
	while True: #持续地读取q中的数据
		value =q.get()
		print 'Get %s from queue.' % value
	print 'Child Process %s ends' % name

if __name__ == "__main__":
	#父进程创建queue，并共享给各个子进程
	q= Queue()
	#创建锁
	lock = Lock()
	#创建第一个“写”子进程
	pw = Process(target = write , args=(q, lock, 'WRITE-1', ))
	#创建第二个“写”子进程
	pw2 =Process(target = write , args=(q, lock, 'WRITE-2', ))
	#创建“读”进程
	pr = Process(target = read, args=(q,lock, 'READ',))
	#启动子进程pw,写入：
	pw.start()
	pw2.start()
	#启动子进程pr，读取：
	pr.start()
	#等待pw结束：
	pw.join()
	pw2.join()
	#pr是个死循环，通过terminate杀死：
	pr.terminate()
	print 'Test finish.'

