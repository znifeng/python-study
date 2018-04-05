#!/usr/bin/python
# -*- coding: utf-8 -*
__author__ = 'zni.feng'

str1 = '{0},{1}'
print str1.format('zni', '26')

str2 = '{name} , {age}'
print str2.format(age=26, name='zni')

str3 ='{1},{0},{1}'
print str3.format('haha', 'hehe')

str4='{0}, {1}'
print str4.format('a', 'b', 'c')

#IndexError: tuple index out of range
# str5='{0}, {1}'
# print str4.format('a')

black_list = ('proxyanalysis', 'getdeviceid', 'refreshtoken', 'ping', 'cdn', 'traceroute', 'sysunadd', 'report_event',
              'delete_spam_event', 'syssub', 'sysadd', 'sysprivate', 'wakeup', 'sysaction', 'wakeupunactive', 'mam',
              'weakup', 'skinusing', 'alarmringusing', 'abtestreqsucc', 'abtestreqsuss', 'getposition', 'skinning',
              'pushswitch', 'bluetooth', 'httpdns', "error", "httpdnsquery", "sysdebug",
              "abtestserver", "spsysaction")

white_list = ('play', 'page', 'view', 'add', 'unadd', 'active', 'login', 'click', 'activeclient',
              'vote', 'subscribe', 'register', 'download', 'playend', 'skip', 'close', 'zan',
              'activeweb', 'follow', 'abtest', 'logexception', 'register', 'uploadidfa')
list = ["'{}'".format(action) for action in white_list]
print ','.join(list)

sql = """select dt, count(1) black_act_users, sum(u2) white_act_users
             from
             (
                select dt, abs(cast(userid as bigint)) u1,
                max(if(lower(action) in ({0}) or lower(action) like '%impress%', 1, 0)) u2
                from music.user_action_process where dt = 'datetime'
                and lower(action) not in ({1}) and userid != '0' and type = 'valid' group by 1, 2
             ) act_users group by 1
             """.format(",".join(["'{}'".format(action) for action in white_list]),
                        ",".join(["'{}'".format(action) for action in black_list]))

print sql