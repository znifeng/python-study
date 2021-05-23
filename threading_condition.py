# Condition/Lock的用法: https://zhuanlan.zhihu.com/p/337690762
# with condition 相当于 condition.acquire() + condition.release()
import threading
import time

con = threading.Condition()
start = 1
flag=1

def print_task_one():
    global start, flag
    while start < 75:
        with con:
            if start<75 and flag == 1:
                print("thread1:" + ",".join([str(start + _) for _ in range(5)]))
                start += 5
                flag =2
            
def print_task_two():
    global start, flag
    while start<75:
        with con:
            if start<75 and flag ==2 :
                print("thread2:" + ",".join([str(start + _) for _ in range(5)]))
                start +=5
                flag =3
            
def print_task_three():
    global start, flag
    while start<75:
        with con:
            if start<75 and flag ==3 :
                print("thread3:" + ",".join([str(start + _) for _ in range(5)]))
                start +=5
                flag =1

thread_one = threading.Thread(target=print_task_one, daemon=False)
thread_two = threading.Thread(target=print_task_two, daemon=False)
thread_three = threading.Thread(target=print_task_three, daemon=True)

thread_one.start()
thread_two.start()
thread_three.start()
thread_one.join()
thread_two.join()
thread_three.join()
