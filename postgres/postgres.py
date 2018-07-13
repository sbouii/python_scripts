import psycopg2

class Postgres:
 def __init__(self, host, database, user):
  self.host = host
  self.database = database
  self.user = user
 def connect(self):
  '''
  Connect to the PostgreSQL database server
  '''
  conn = None
  try:
   conn = psycopg2.connect(host=self.host, database=self.database, user=self.user)
   cur = conn.cursor()
   '''
    Get PostgreSQL database version
   '''
   print 'PostgreSQL database version *****************************************'
   cur.execute('SELECT version()')
   db_version = cur.fetchone()
   print(db_version)    
   '''
    Check the active SQL queries and open connections in Postgres by checking the table pg_stat_activity
   '''
   print 'Active SQL queries **************************************************'
   command1 = "select datname, usename, pid, client_addr, waiting, query_start from pg_stat_activity;"
   cur.execute(command1)
   active_queries = cur.fetchall()
   print(active_queries)

   '''
    Get all databases     
   '''
   print 'All databases *******************************************************'
   command2 = "select datname from pg_database;"
   cur.execute(command2)
   databases = cur.fetchall()
   print(databases)

   '''
    Get all tables in the current database
   '''
   print 'All tables in the current database **********************************'
   command3 = "select * from pg_catalog.pg_tables where schemaname != 'pg_catalog' and schemaname != 'information_schema';;"
   cur.execute(command3)
   tables_current_database = cur.fetchall()
   print(tables_current_database)

   '''
    Get the size of the database
   '''
   command4 = "select pg_database_size('testing');"
   cur.execute(command4)
   database_size = cur.fetchall()  
   print (database_size)
  except (Exception, psycopg2.DatabaseError) as error:
   print(error)
  finally:
   if conn is not None:
     conn.close()
     print('Database connection closed') 

def main():
 p = Postgres('127.0.0.1', 'testing', 'postgres')
 p.connect()

if __name__ == "__main__":
 main() 
