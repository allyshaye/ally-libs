import os
import pymysql
from pymysql.cursors import DictCursor,SSDictCursor,SSCursor,Cursor


DEFAULT_OPT_FILE = "{}/.my.cnf".format(os.environ['HOME'])


class MySQLConnection:

	def __init__(self, option_file=DEFAULT_OPT_FILE):
		self.opt_file = option_file
		self.connection = self.connection()

	def connection(self):
		""" Returns MySQL connection. """ 
		return pymysql.connect(read_default_file=self.opt_file,autocommit=True)


	def cursor(self, cursor_type=None):
		""" Returns cursor object. """
		if cursor_type == "DictCursor":
			_cursor = pymysql.cursors.DictCursor
		elif cursor_type == "SSDictCursor":
			_cursor = pymysql.cursors.SSDictCursor
		elif cursor_type == "SSCursor":
			_cursor = pymysql.cursors.SSCursor
		else:
			_cursor = pymysql.cursors.Cursor
		return self.connection.cursor(cursor=_cursor)	


	def run_query(self, cursor, query, args=None):
		""" Runs a query once and returns all results. """
		cursor.execute(query, args)
		results = cursor.fetchall()
		return results


	def repeat_query(self,query, args, max_statement_length=1024000):
		""" Runs the same query multiple times with several 
		data stored in args."""
		cursor.max_stmt_length = max_statement_length
		cursor.executemany(query,args)
		results = cursor.fetchall()
		return results

	
	def close_cursor(self, cursor):
		""" CLoses cursor."""
		cursor.close()


	def close_connection(self):
		""" Closes open connection. """
		if self.connection.open:
			self.connection.close()



