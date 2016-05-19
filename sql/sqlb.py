import csv
import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()
    employees = csv.reader(open("employees.csv","rU"))
    try:
        c.execute("CREATE TABLE employees(firstname TEXT, lastname TEXT)")
        c.executemany("INSERT INTO employees(firstname, lastname) VALUES (?,?)", employees)
    except:
        c.execute("SELECT firstname, lastname FROM employees")
        rows = c.fetchall()
        for r in rows:
            print r[0],r[1]
        
    
