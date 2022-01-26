# import MySQLdb # para o MySQL
# import sqlite  # para o SQLite
#import psycopg2 # para o PostgreSQL
import fdb # para Interbase / Firebird
# import pymssql  #para o MS-SQL. (existem outros módulos - ADOdb for Python/PHP)
# import cx_Oracle #para o Oracle

class BdConnections:

    def mysql_connection(self,host, bd, user, password):
        con = MySQLdb.connect(host, user, password)
        con.select_db(bd)

    def sqlite_connection(self, bd):
        con = sqlite.connect(bd, mode=775)

    def postgre_connection(self, host, bd, port, user, password):
        con = psycopg2.connect(host=host,
                    port=port,
                    dbname=bd,
                    user=user,
                    password=password)
        return con

    def firebird_connection(self, host, database, user, password, port):
        conn = fdb.connect(host=host,
                          database=database,
                          user=user,
                          password=password,
                          port=port)
        return conn

    def mssql_connection(self, host, database, user, password):
        con = pymssql.connect(host = host,
                      user = user,
                      password = password,
                      database = database)

