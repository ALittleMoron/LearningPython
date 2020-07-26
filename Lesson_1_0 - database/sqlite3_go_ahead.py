import sqlite3
import os.path


class WrongDataBaseNameException(Exception):
    """ Класс-исключение для отлова ошибки о неправильном введенном названии БД """
    pass


def connect_to_database(database_name:str, path:str = '') -> sqlite3.Connection:
    """ Функция подключения к базе данных. Возвращает соединение на уже
    существующую базу данных (Не хочу случайно создать лишнюю БД).

    аргументы:
    database_name -- файл базы данных
    path -- путь к файлу базы данных (Опциональный. Не передавать аргумент,
    если база данных находится рядом с python файлом.
    """
    try:
        database = os.path.join(path, database_name)
        if os.path.isfile(database) and ('.db' in database or '.sqlite' in database):
            connection = sqlite3.connect(database, timeout=5)
            return connection
        else:
            return None
    except sqlite3.Error as e:
        print(e)
        connection.close()


def create_database_table(connection:sqlite3.Connection,
                          table_name:str, args:dict) -> None:
    """ Функция создания таблицы в базе данных

    аргументы:
    connection -- соединение с базой данных
    table_name -- название таблицы
    args -- словарь элементов таблицы с их типами. Пример: {'title': 'TEXT'}
    """
    try:
        if connection is None:
            raise WrongDataBaseNameException('Неправильное название базы данных. Введите существующую')
        if type(table_name) is not str:
            raise TypeError('Название таблицы может быть только строковое')
        if type(args) is not dict:
            raise TypeError('элементы таблицы и их типы могут быть представлены только в словаре')
        cursor = connection.cursor()
        cursor.execute(f"""CREATE TABLE IF NOT EXISTS {table_name.lower()} (
                        {', '.join(f'{k} {v}' for k,v in args.items())})""")
        connection.commit()
    except sqlite3.Error as e:
        print(e)
    finally:
        connection.close()


def delete_database_table(connection:sqlite3.Connection,
                          table_name:str) -> None:
    """ Функция удаляет таблицу из базе данных

    аргументы:
    connection -- соединение с базой данных
    table_name -- название таблицы
    """
    try:
        if connection is None:
            raise WrongDataBaseNameException('Неправильное название базы данных. Введите существующую')
        if type(table_name) is not str:
            raise TypeError('Название таблицы может быть только строковое')
        cursor = connection.cursor()
        cursor.execute(f"""DROP TABLE IF EXISTS {table_name.lower()}""")
        connection.commit()
    except sqlite3.Error as e:
        print(e)
    finally:
        connection.close()


def add_info_to_table(connection:sqlite3.Connection,
                      table_name:str, args:tuple) -> None:
    """ Функция добавления информации в имеющуюся таблицу в базе данных

    аргументы:
    connection -- соединение с базой данных
    table_name -- название таблицы
    args -- кортеж элементов таблицы без их типов. Пример: ('something', ...)
    """
    try:
        if connection is None:
            raise WrongDataBaseNameException('Неправильное название базы данных. Введите существующую')
        if type(args) is not tuple:
            raise TypeError('аргумент args может быть только кортежем или списком')
        cursor = connection.cursor()
        cursor.execute(f"""INSERT INTO {table_name.lower()} VALUES
                        (?{', ?' * (len(args)-1)})""", args)
        connection.commit()
    except sqlite3.Error as e:
        print(e)
    finally:
        connection.close()


def delete_info_in_table(connection:sqlite3.Connection,
                         table_name:str, _id:int) -> None:
    """ Функция удаляет запись в таблице по её id

    аргументы:
    connection -- соединение с базой данных
    table_name -- название таблицы
    _id -- идентификационный номер записи в таблице
    """
    pass


def show_all_created_tables_name(connection:sqlite3.Connection) -> None:
    """ Функция выводит список имен всех созданных таблиц (без содержания)

    аргумент:
    connection -- соединение с базой данных
    """
    try:
        if connection is None:
            raise WrongDataBaseNameException('Неправильное название базы данных. Введите существующую')
        cursor = connection.cursor()
        cursor.execute("""SELECT name FROM sqlite_master
                        WHERE type='table'""")
        print("Список всех созданных таблиц:")
        for e, table in enumerate(cursor.fetchall()):
            print(e+1, ' -- ', table[0])
        connection.commit()
    except sqlite3.Error as e:
        print(e)
    finally:
        connection.close()


def show_all_created_tables_content(connection:sqlite3.Connection) -> None:
    """ Функция выводит список всех созданных таблиц с их содержанием

    аргумент:
    connection -- соединение с базой данных
    """
    try:
        if connection is None:
            raise WrongDataBaseNameException('Неправильное название базы данных. Введите существующую')
        cursor = connection.cursor()
        cursor.execute("""SELECT name FROM sqlite_master
                        WHERE type='table'""")
        tables_name = [table[0] for table in cursor.fetchall()]
        print("Список всех созданных таблиц и их содержание:")
        for table in tables_name:
            cursor.execute(f"""SELECT * FROM {table}""")
            print(table)
            for e, content in enumerate(cursor.fetchall()):
                print('  ', e+1, ' -- ', sep='', end='')
                print(*content, sep=', ')
        connection.commit()
    except sqlite3.Error as e:
        print(e)
    finally:
        connection.close()


def edit_info_in_table(connection:sqlite3.Connection,
                       table_name:str, _id:int, data:dict) -> None:
    """ Функция изменяет нужные данные в таблице

    аргументы:
    connection -- соединение с базой данных
    table_name -- название таблицы
    _id -- идентификационный номер записи в таблице
    data -- данные для изменения
    """
    try:
        if connection is None:
            raise WrongDataBaseNameException('Неправильное название базы данных. Введите существующую')
        if type(table_name) is not str:
            raise TypeError('Название таблицы может быть только строковое')
        if type(_id) is not int:
            raise TypeError('Идентификатор записи в таблице должен быть числом')
        if type(data) is not dict:
            raise TypeError('данные должны быть в формате словаря')
        cursor = connection.cursor()
        cursor.execute(f"""UPDATE {table_name.lower()}
                           SET {', '.join(f'{e} = "{b}"' for e,b in data.items())}
                           WHERE id = ?""", (_id,))
        connection.commit()
    except sqlite3.Error as e:
        print(e)
    finally:
        connection.close()


if __name__ == '__main__':
    data = {'title': 'Godfall', 'author': 'Ray Midler', 'cost': 1000.25}
    edit_info_in_table(connect_to_database('MyDataBase.db'), 'book', 1, data)
