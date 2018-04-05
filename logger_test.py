#!/usr/bin/python
# -*- coding: utf-8 -*
__author__ = 'zni.feng'
import os
# mac 上logging的源码路径 /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/logging
import logging
import logging.handlers

class Logger:
    def __init__(self, name="root"):
        self._logger = logging.getLogger(name)
        #def __init__(self, fmt=None, datefmt=None)
        formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] - %(filename)s(line:%(lineno)d) - %(message)s', '%Y-%m-%d %H:%M:%S')

        #class logging.handlers.TimedRotatingFileHandler(filename, when='h', interval=1, backupCount=0, encoding=None, delay=False, utc=False)
        handler_info = logging.handlers.TimedRotatingFileHandler('logs/info.log', when='D', interval=1)
        handler_warn = logging.handlers.TimedRotatingFileHandler('logs/warn.log', when='D', interval=1)

        handler_info.setFormatter(formatter)
        handler_warn.setFormatter(formatter)

        #当handler的log level高于logger本身的log level时，此设置才会生效
        handler_info.setLevel(logging.INFO)
        handler_warn.setLevel(logging.WARN)

        self._logger.addHandler(handler_info)
        self._logger.addHandler(handler_warn)

        #默认情况下，logger本身的log level是warn，为了让info handler的level等级生效，所以调低logger本身的level
        self._logger.setLevel(logging.INFO)
        
    def getLogger(self):
        return self._logger