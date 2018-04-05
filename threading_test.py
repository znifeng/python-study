#!/usr/bin/python
# -*- coding: utf-8 -*
__author__ = 'zni.feng'
import  sys
reload (sys)
sys.setdefaultencoding('utf-8')

import threading, time

def test(index):
	print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
	print 'thread %s starts.' % threading.current_thread().name
	print 'the index is %d' % index
	time.sleep(3)
	print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
	print 'thread %s ends.' % threading.current_thread().name

if __name__ == "__main__":
	print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
	print 'thread %s starts.' % threading.current_thread().name
	#创建线程
	my_thread = threading.Thread(target = test, args=(1,) , name= 'zni_feng_thread')
	#等待2s
	time.sleep(2)
	#启动线程
	my_thread.start()
	#等待线程结束
	my_thread.join()
	print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
	print 'thread %s ends.' % threading.current_thread().name