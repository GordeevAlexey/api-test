import sqlite3
from DataBase.utils import *

class DBContext:


    def __init__(self):

        self.conn = sqlite3.connect(PATH)
        self.cursor = self.conn.cursor()
        self.cursor.executescript(SQL_QUERY_FIRST_START_DB)
        self.conn.commit()

    def return_id_with_addition(self, service_name):
        id = self.cursor.execute(SQL_QUERY_ID_SERVICES, [service_name]).fetchone()

        if id is None:
            self.cursor.execute(SQL_QUERY_INSERT_SERVICE, [service_name])
            self.conn.commit()
            id = self.cursor.execute(SQL_QUERY_GET_LAST_ID).fetchall()[0]
        return id

    def insert_log_in_bd(self, addList):
        self.cursor.execute(SQL_QUERY_INSERT_LOGS, addList)
        self.conn.commit()

    def all_logs_service(self, service_name):
        id = self.cursor.execute(SQL_QUERY_ID_SERVICES, [service_name]).fetchone()
        if id is None:
            result_query = [('a service with this name was not found', 'None', 'None', 'None')]
        else:
            result_query = self.cursor.execute(SQL_QUERY_ALL_LOGS_SERVICE, id).fetchall()
        return result_query

    def last_message_all_service(self):
        result_query = self.cursor.execute(SQL_QUERY_LAST_MSG_ALL_SERVICE).fetchall()
        return result_query

    def find_substr_all_message(self, substring):
        result_query = self.cursor.execute(SQL_QUERY_FIND_SUBSTR_ALL_MSG, ["%" + substring + "%"]).fetchall()
        return result_query

    def find_sub_str_last_msg(self, substring):
        result_query = self.cursor.execute(SQL_QUERY_FIND_SUBSTR_LAST_MSG, ["%" + substring + "%"]).fetchall()
        return result_query
