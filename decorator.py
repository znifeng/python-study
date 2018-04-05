#!/usr/bin/python
# -*- coding: utf-8 -*
__author__ = 'zni.feng'

import functools

#decorator1
def log(func):
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper

#decorator2
def log2(func):
    @functools.wraps(func) #将func的方法名赋值给wrapper，等同于wrapper.__name__ = func.__name
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper

#decorator3. 带参数的decorator
def log3(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator

#decorator4. 带参数的decorator
def log4(*args, **kw):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            for i in args:
                print i
            return func(*args, **kw)
        return wrapper
    return decorator

def f1():
    print 'f1'

def f2(f3):
    f3()
    print 'f2'

@log
def now():
	print '2017-6-23'

@log2
def hello():
	print 'hello world.'

@log3('zni')
def back():
	print 'back home.'


@log4(['zni','cy'])
def test(age):
    print 'age=' + str(age)

if __name__ == "__main__":
	# now()
	# print now.__name__
	# hello()
	# print hello.__name__
	# back()
	# print back.__name__
    # f2(hello)
    test(25)