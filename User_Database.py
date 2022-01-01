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