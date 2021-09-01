'''
Переменные для работы с БД

PATH - путь до базы данных.
SQL_QUERY_GET_LAST_ID - sql запрос возвращающий id последней добавленной записи в таблицу
SQL_QUERY_ID_SERVICES - sql запрос возвращающий id сервиса по его наименованию
SQL_QUERY_INSERT_SERVICE - sql запрос добавляющий новый сервис в таблицу
SQL_QUERY_INSERT_LOGS - sql запрос добавляющий новый лог в таблицу
SQL_QUERY_ALL_LOGS_SERVICE - sql запрос возвращающий все логи по запрашиваемому сервису
SQL_QUERY_LAST_MSG_ALL_SERVICE - sql запрос возвращающий последние логи по всем существующим в БД сервисам
SQL_QUERY_FIND_SUBSTR_ALL_MSG - sql запрос возвращающий все логи всех сервисов с искомой подстракой
SQL_QUERY_FIND_SUBSTR_LAST_MSG - sql запрос возвращающий логи из последних записей всех сервисов с искомой подстракой
SQL_QUERY_FIRST_START_DB - скрипт создания и настройки БД при первом запуске сервиса

'''

PATH = 'DataBase\\loginfo.db'

SQL_QUERY_GET_LAST_ID = f"""select last_insert_rowid()"""

SQL_QUERY_ID_SERVICES = f"""select service_id from service where service_name = ? """

SQL_QUERY_INSERT_SERVICE = f"""insert into service (service_name) values (?)"""

SQL_QUERY_INSERT_LOGS = f"""insert into logs (logs_service_id, logs_time, logs_text, logs_ip) values (?,?,?,?)"""

SQL_QUERY_ALL_LOGS_SERVICE = f"""select 
                    t2.service_name, 
                    strftime("%d.%m.%Y %H:%M:%S", t1.logs_time) as logs_time, 
                    t1.logs_text, 
                    t1.logs_ip from (select * from logs where logs_service_id = ? order by strftime(logs_time) DESC) t1
                    join (select * from service) t2 on t1.logs_service_id = t2.service_id"""

SQL_QUERY_LAST_MSG_ALL_SERVICE = f"""select
                    t2.service_name,
                    strftime("%d.%m.%Y %H:%M:%S", t1.logs_time),
                    t1.logs_text,
                    t1.logs_ip from (select logs_service_id,
                                     max(strftime(logs_time)) as logs_time,
                                     logs_text, logs_ip from logs group by logs_service_id) t1
                    join (select * from service) t2 on t1.logs_service_id = t2.service_id"""


SQL_QUERY_FIND_SUBSTR_ALL_MSG = f"""select 
                    t2.service_name, 
                    strftime("%d.%m.%Y %H:%M:%S", t1.logs_time), 
                    t1.logs_text, 
                    t1.logs_ip from (select * from logs where logs_text like ? ) t1 
                    join (select * from service) t2 on t1.logs_service_id = t2.service_id"""




SQL_QUERY_FIND_SUBSTR_LAST_MSG = f"""select
                    t2.service_name,
                    strftime("%d.%m.%Y %H:%M:%S", t1.logs_time),
                    t1.logs_text,
                    t1.logs_ip from (select logs_service_id,
                                     max(strftime(logs_time)) as logs_time,
                                     logs_text, logs_ip from logs group by logs_service_id) t1
                    join (select * from service) t2 on t1.logs_service_id = t2.service_id where t1.logs_text like ? """

SQL_QUERY_FIRST_START_DB = """
            
            PRAGMA foreign_keys=on;
            
            CREATE TABLE IF NOT EXISTS logs (
            logs_id INTEGER PRIMARY KEY AUTOINCREMENT not null,
            logs_service_id INTEGER NOT NULL,
            logs_time TEXT,
            logs_text TEXT,
            logs_ip TEXT,           
            foreign key (logs_service_id) references service(service_id)); 
            
            CREATE TABLE IF NOT EXISTS service (
            service_id INTEGER PRIMARY KEY AUTOINCREMENT not null, 
            service_name TEXT); 
            
            CREATE INDEX IF NOT EXISTS "IDX_logs_service_id" ON "logs" ("logs_service_id"); 
            CREATE INDEX IF NOT EXISTS "IDX_logs_text" ON "logs" ("logs_text"); 
            
            """