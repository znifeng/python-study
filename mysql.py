#!/usr/bin/python
# -*- coding: utf-8 -*
__author__ = 'zni.feng'

import MySQLdb

class DBProperties:
	def __init__(self):
		self.host = '127.0.0.1'
		self.port = 3306
		self.user = 'root'
		self.passwd = 'root'
		self.db = 'test'
		self.params = dict()
	
	def get_properties(self):
		if not self.params:
			self.params['host'] = self.host
			self.params['port'] = self.port
			self.params['user'] = self.user
			self.params['passwd'] = self.passwd
			self.params['db'] = self.db
		
		return self.params

class DBHelper:
	def __init__(self):
		self.dbProperties = DBProperties()
		self.connection = None

	def get_connection(self):
		if not self.connection or not self.connection.open:
			properties = self.dbProperties.get_properties()
			self.connection = MySQLdb.connect(**properties)
		return self.connection

	def close_connection(self):
		if self.connection.open:
			self.connection.close()
			print 'DB connection is closed success.'
		else:
			print 'DB connection is not open.'
	# 使用cursor()方法获取操作游标 
	def get_cursor(self):
		return self.get_connection().cursor()

	# 使用execute方法执行SQL语句,并获取查询结果
	def execute_sql(self, sql):
		cursor = self.get_cursor()
		cursor.execute(sql)
		result = cursor.fetchall()
		return result

	# 根据project名查找其在projects表中的id
	def get_project_id(self, project):
		sql = "select id from projects where name='%s'" % (project)
		res = self.execute_sql(sql)
		if not res:
			sys.exit('Project is not found : %s' % project)
		else:
			return res[0][0]

	# 根据project名和flow名，查找该实例的个数
	def get_executions_num(self, project, flow):
		project_id = self.get_project_id(project)
		sql = "select count(*) from execution_flows where project_id={0} and flow_id='{1}'".format(project_id, flow) 
		res = self.execute_sql(sql)
		return res[0][0]

	def clean_tables(self):
		tables = self.execute_sql("show tables")
		tables_to_truncate= ('active_executing_flows', 'active_sla', 'execution_flows', 'execution_jobs', 'execution_logs', 'triggers')
		for item in tables:
			table_name = item[0]
			if table_name in tables_to_truncate:
				self.execute_sql('truncate %s' % table_name)

if __name__ == "__main__":
	dbHelper = DBHelper()
	# res= dbHelper.execute_sql("select id from projects where name='%s'" % 'nzf_stable_schedule_test1')

	# res = dbHelper.get_project_id('nzf_stable_schedule_test1')

	# res = dbHelper.get_executions_num('nzf_stable_schedule_test1', 'stable_test_command_10')
	res = dbHelper.clean_tables()
	
	dbHelper.close_connection()