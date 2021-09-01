from DataBase.db_context import DBContext
from fastapi import FastAPI, Request
from typing import Optional
import datetime

app = FastAPI()
db = DBContext()

@app.get("/alllogsservice")
async def get_all_logs_service(service_name: str):
    """
    Запрос всех данных по сервису. \n
    :param service_name: наименование сервиса в формате str. \n
    :return: \n
    Возвращает все записаные сообщения сервиса записанные в БД. \n
        [ \n
          { \n
            "service_name": "рассылка почты",\n
            "logs_time": "31.08.2021 17:10:50",\n
            "logs_text": "{1:7}",\n
            "logs_ip": "127.0.0.1"\n
          },\n
            .....\n
          {\n
            "service_name": "рассылка почты",\n
            "logs_time": "31.08.2021 17:10:38",\n
            "logs_text": "{1:4}",\n
            "logs_ip": "127.0.0.1"\n
          }\n
        ]\n
    Если искомый сервис не найден, возвращает пустой лист.\n
        [\n
            {\n
                "service_name": "a service with this name was not found",\n
                "logs_time": "None",\n
                "logs_text": "None",\n
                "logs_ip": "None"\n
            }\n
        ]\n

    """

    returnlist = db.all_logs_service(service_name)
    return returnlist

@app.get("/lastmessageallservice")
async def get_last_message_all_service():
    """
    Последние сообщения от всех сервисов.\n
    Запрос без входных параметров.\n

    :return:\n
    Возвращает последние записаные сообщения всех сервисов зарегистрированных в БД.\n

    Если БД пуста, вернет пустой list.

    """

    returnlist = db.last_message_all_service()
    return returnlist

@app.get("/findsubstringallmessage") # Поиск лога по подстроке
async def get_find_substring_all_message(substring: str):
    """
    Поиск лога по подстроке.\n
    Реализует поиск по задваемой подстроке.\n

    :param substring: искомая подстрока.\n
    :return: результат поиска в формате JSON\n

    Если ничего не найдено, вернет пустой list.

    """

    returnlist = db.find_substr_all_message(substring)
    return returnlist

@app.get("/findsubstringinlastmessageallservice")
async def get_find_substring_last_message(substring: str):
    """
    Поиск лога по подстроке среди последних записей от каждого существующего сервиса.\n

    :param substring: искомая подстрока.\n
    :return: результат поиска в формате JSON\n

    Если ничего не найдено, вернет пустой list.

    """

    returnlist = db.find_sub_str_last_msg(substring)
    return returnlist

@app.post("/sendlog")
async def add_log_bd(log: str, request: Request, srv: str = "no named service"):
    """
    Запрос на добавление нового лога.\n

    :param log: Текст лога в произвольном формате.\n
    :param srv: Наименование сервиса. (необязательный параметр)\n
    :return: После добавления, возвращает 'Logs added to the database'\n

    Если не указан сервис, прикрепляет отправляемый лог к сервису по умолчанию: "no named service".\n
    Если указанного сервиса не существует в БД, динамичсески дополняет БД указанным сервисом.\n

    """

    client_ip = request.client.host
    dt_now = datetime.datetime.now()
    id_service = db.return_id_with_addition(srv)[0]
    addList = [id_service, dt_now, log, client_ip]
    db.insert_log_in_bd(addList)
    return {'Logs added to the database'}