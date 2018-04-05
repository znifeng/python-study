#!/usr/bin/python
# -*- coding: utf-8 -*
__author__ = 'zni.feng'
import re

pattern_old = re.compile('[a-zA-Z_0-9\u4e00-\u9fa5|-|$]+')
pattern_new = re.compile(r'[a-zA-Z_0-9\u4e00-\u9fa5|\$|-]+')

s = '中文'
m_old=pattern_old.match(s)
m_new=pattern_new.match(s)

print m_old.group() if m_old else None

print m_new.group() if m_new else None

pattern = re.compile('[01459]')
st = '59'
# m = pattern.match(st)
# print m.group() if m else None
print pattern.findall(st)