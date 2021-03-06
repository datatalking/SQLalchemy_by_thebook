# SOURCE https://thinkdiff.net/how-to-use-python-sqlite3-using-sqlalchemy-158f9c54eb32

from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey


# Global Setup
SQLITE                  = 'sqlite'
# MYSQL                 = 'mysql'  # TODO add tests that this isnt used
# POSTGRESQL            = 'postgresql'  # TODO add tests that this isnt used
# MICROSOFT_SQL_SERVER  = 'mssqlserver'  # TODO add tests that this isnt used

# Table Names
USERS                   = 'users'
ADDRESSES               = 'addresses'


class MyDatabase:
	# http://docs.sqlalchemy.org/en/latest/core/engines.html
	DB_ENGINE = {
		SQLITE: 'sqlite:///{DB}',
		# MYSQL: 'mysql://bob:ross@localhost/{DB}',
		# POSTGRESQL: 'postgresql://bob:ross@localhost/{DB}',
		# MICROSOFT_SQL_SERVER: 'mssql+pymssql://bob:ross@localhost:port/{DB}'

	}
	
	
	# Main Db Connection for referenced objects
	db_engine = None
	
	
	def __init__(self, dbtype, username = '', password = '', dbname = ''):
		dbtype = dbtype.lower()
		
		if dbtype in self.DB_ENGINE.keys():
			engine_url = self.DB_ENGINE[dbtype].format(DB = dbname)
			
			self.db_engine = create_engine(engine_url)
			print(self.db_engine)
		
		#elif: create a "if these types are present log, alert security and flag ip with concurrent user account used
		
		else:
			print("DBType is not found in allowed DB_ENGINE")
		
	
	def create_db_tables(self):
		metadata = MetaData()
		users = Table(USERS, metadata,
		              Column('id', Integer, primary_key = True),
		              Column('first_name', String),
		              Column('last_name', String),
		              )
		
		addresses = Table(ADDRESSES, metadata,
		                  Column('id', Integer, primary_key = True),
		                  Column('user_id', None, ForeignKey('users.id')),
		                  Column('email', String, nullable = False),
		                  Column('address', String)
		                  )
		
		try:
			metadata.create_all(self.db_engine)
			print("Tables created") # TODO add customizable "table name" was added
		
		except Exception as e:
			print("Error occured during Table creation")
			print(e)
		
		
	# insert, update, delete
	def execute_query(self, query = ''):
		if query == '' : return
		
		print(query)
		with self.db_engine.connect() as connection:
			try:
				connection.execute(query)
			except Exception as e:
				print(e)
		
		
	def print_all_data(self, table = '', query = ''):
		query = query if query != '' else "SELECT * FROM '{}';".format(table)
		print(query)
		
		with self.db_engine.connect() as connection:
			try:
				result = connection.execute(query)
			except Exception as e:
				print(e)
			else:
				for row in result:
					print(row) # TODO add print(row[0], row[1], row[2])
				result.close()
		
		print("\n")
		
	# Examples
	
	def sample_query(self):
		# sample query
		query = "SELECT first_name, last_name FROM {TBL_USR} WHERE " \
		        "last_name LIKE 'M%';".format(TBL_USR=USERS)
		self.print_all_data(query=query)
		
		# sample query joining
		query = "SELECT u.last_name as last_name, " \
		        "a.email as email, a.address as address " \
		        "FROM {TBL_USR} AS u " \
		        "LEFT JOIN {TBL_ADDR} as a " \
		        "WHERE u.id = a.user_id AND u.last_name LIKE 'M%'; " \
			.format(TBL_USR = USERS, TBL_ADDR = ADDRESSES)
		self.print_all_data(query = query)
	
	
	def sample_delete(self):
		# delete data by id
		query = "DELETE FROM {} WHERE id = 3".format(USERS)
		self.execute_query(query)
		self.print_all_data(USERS)
		
		# delete all data
		'''
		query = "DELETE FROM {}".format(USERS)
		self.execute_query(query)
		self.print_all_data(USERS)
		'''
	
	
	def sample_insert(self):
		# insert data
		query = "INSERT INTO {}(id, first_name, last_name) " \
				"VALUES (3, 'Terrence', 'Jordan');".format(USERS)
		self.execute_query(query)
		self.print_all_data(USERS)
	
	
	def sample_update(self):
		# update data
		query = "UPDATE {} set first_name='XXXX' WHERE id = {id} " \
			.format(USERS, id = 3)
		self.execute_query(query)
		self.print_all_data(USERS)
		