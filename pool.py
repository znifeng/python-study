#!/usr/bin/python
# -*- coding: utf-8 -*
__author__ = 'zni.feng'
import  sys
reload (sys)
sys.setdefaultencoding('utf-8')

from multiprocessing import Pool, Manager
import os, time


def child_process_test(name, sleep_time, result_list, result_dict):
	print 'Child process %s with processId %s starts.' % (name, os.getpid())
	time.sleep(sleep_time)
	result_list.append(name)
	result_dict[sleep_time] = name
	print 'Child process %s with processId %s ends.' % (name, os.getpid())

if __name__ == "__main__":
	print 'Parent processId is: %s.' % os.getpid()
	p = Pool()  #进程池默认大小是cpu的核数
	manager = Manager()
	# 多进程共享的变量
	result_list = manager.list()
	result_dict = manager.dict()

	#p = Pool(10) #生成一个容量为10的进程池，即最大同时执行10个子进程
	for i in range(5):
		p.apply_async(child_process_test, args=('zni_'+str(i), i+1, result_list, result_dict)) #p.apply_async向进程池提交目标请求

	print 'Child processes are running.'
	p.close()
	p.join() #用来等待进程池中的所有子进程结束再向下执行代码，必须在p.close()或者p.terminate()之后执行
	print 'All Processes end.'
	print list(result_list)
	print dict(result_dict)