# SOURCE https://thinkdiff.net/how-to-use-python-sqlite3-using-sqlalchemy-158f9c54eb32

from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, Meta, ForeignKey

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
		metadata = MetaData():
		users = Table(USERS, metadata,
		              Column('id', Integer, primary_key = True),
		              Column('first_name', String),
		              Column('last_name', String),
		              )
		
		addresses = Table(ADDRESSES, metadata,
		                  Column('id', Integer, primary_key = True),
		                  Column('user_id', None, ForeignKey('user.id')),
		                  Column('email', String, Nullable = False),
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