# SOURCE Muhmad Ahsan
# SQLalchemy

from data import User_Database


def main():
	dbms = User_Database.MyDatabase(User_Database.SQLITE, dbname = 'mydb.sqlite') # TODO .format for SQLITE f string
	
	# create Tables
	dbms.create_db_tables()
	# dbms.insert_single_data()
	dbms.print_all_data(User_Database.USERS)
	dbms.print_all_data(User_Database.ADDRESSES)
	
	dbms.sample_query() # simple query
	dbms.sample_delete() # delete data
	dbms.sample_insert() # insert data
	dbms.sample_update() # update data


# run the program
if __name__ == '__main__':
	main()