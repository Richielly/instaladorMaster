# import MySQLdb # para o MySQL
# import sqlite  # para o SQLite
# from pyPgSQL import PgSQL # para o PostgreSQL
import fdb # para Interbase / Firebird
# import pymssql  #para o MS-SQL. (existem outros módulos - ADOdb for Python/PHP)
# import cx_Oracle #para o Oracle

class BdConnections:

    def mysql_connection(self,host, bd, user, password):
        con = MySQLdb.connect(host, user, password)
        con.select_db(bd)

    def sqlite_connection(self, bd):
        con = sqlite.connect(bd, mode=775)

    def postgre_connection(self, host, bd, user, password):
        con = PgSQL.connect(host=host,
                    database=bd,
                    user=user,
                    password=password)

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

