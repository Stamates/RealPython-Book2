import sqlite3
from random import randint

with sqlite3.connect("new_num.db") as connection:
    c = connection.cursor()
    c.execute("DROP TABLE if exists numbers")
    c.execute("CREATE TABLE numbers(number INT)")
    for i in range(100):
        c.execute("INSERT INTO numbers(number) VALUES (?)", (randint(0,100),))
        
    
