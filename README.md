# api-test
##API по добавлению логов в БД

##Описание функционала API


### 1. /alllogsservice
    Запрос всех данных по сервису.  
    Примимает наименование сервиса в формате str.  
    Возвращает все записаные сообщения сервиса записанные в БД.  
    Если искомый сервис не найден, возвращает пустой лист.
### 2. /lastmessageallservice
    Последние сообщения от всех сервисов.
    Запрос без входных параметров.
    Возвращает последние записаные сообщения всех сервисов 
    зарегистрированных в БД.
    Если БД пуста, вернет пустой list.
### 3. /findsubstringallmessage
    Поиск лога по подстроке.
    Реализует поиск по задваемой подстроке.
    Принимает искомую подстроку.
    Возвращает результат поиска в формате JSON
    Если ничего не найдено, вернет пустой list.

### 4. /findsubstringinlastmessageallservice
    Поиск лога по подстроке среди последних записей от 
    каждого существующего сервиса.
    Принимает искомую подстроку.
    Возвращает результат поиска в формате JSON
    Если ничего не найдено, вернет пустой list.

### 5./sendlog
    Запрос на добавление нового лога.
    Принимает: - Текст лога в произвольном формате.
               - Наименование сервиса. (необязательный параметр)
    
    После добавления, возвращает 'Logs added to the database'
    Если не указан сервис, прикрепляет отправляемый лог к сервису по умолчанию: "no named service".
    Если указанного сервиса не существует в БД, динамичсески дополняет БД указанным сервисом.