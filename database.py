from getpass import getpass
from mysql.connector import connect, Error

'''try:
    with connect(
        host="localhost",
        user=input("Enter username: "),
        password=getpass("Enter password: "),
    ) as connection:
        create_db_query = "CREATE DATABASE my_connections"
        with connection.cursor() as cursor:
            cursor.execute(create_db_query)
except Error as e:
    print(e)'''

try:
    with connect(
        host="localhost",
        user=input("Enter username: "),
        password=getpass("Enter password: "),
        database="my_connections",
    ) as connection:
        print(connection)
except Error as e:
    print(e)