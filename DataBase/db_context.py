import uuid
import psycopg2
import psycopg2.extras
from DataBase.utils import *

psycopg2.extras.register_uuid()


class DBContext:

    def __init__(self):
        #self.conn = psycopg2.connect(user='postgres', dbname='api_log', password='admin', host='db', port='5432')
        self.conn = psycopg2.connect(user='postgres', dbname='api_log', password='admin', host='192.168.1.188', port='5432')
        self.cursor = self.conn.cursor()
        self.conn.commit()

    def return_id_with_addition(self, service_name):
        self.cursor.execute(SQL_QUERY_ID_SERVICES, [service_name])
        id = self.cursor.fetchone()
        if id is None:
            id = (uuid.uuid4(),)
            self.cursor.execute(SQL_QUERY_INSERT_SERVICE, [id[0], service_name])
            self.conn.commit()
        return id

    def insert_log_in_bd(self, addList):
        self.cursor.execute(SQL_QUERY_INSERT_LOGS, addList)
        self.conn.commit()

    def all_logs_service(self, service_name):
        self.cursor.execute(SQL_QUERY_ID_SERVICES, [service_name])
        id = self.cursor.fetchone()
        if id is None:
            result_query = [('a service with this name was not found', 'None', 'None', 'None')]
        else:
            self.cursor.execute(SQL_QUERY_ALL_LOGS_SERVICE, id)
            result_query = self.cursor.fetchall()
        return result_query

    def last_message_all_service(self):
        self.cursor.execute(SQL_QUERY_LAST_MSG_ALL_SERVICE)
        result_query = self.cursor.fetchall()
        return result_query

    def find_substr_all_message(self, substring):
        self.cursor.execute(SQL_QUERY_FIND_SUBSTR_ALL_MSG, ["%" + substring + "%"])
        result_query = self.cursor.fetchall()
        return result_query

    def find_sub_str_last_msg(self, substring):
        self.cursor.execute(SQL_QUERY_FIND_SUBSTR_LAST_MSG, ["%" + substring + "%"])
        result_query = self.cursor.fetchall()
        return result_query
