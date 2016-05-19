#import sqlite3
from views import db
from models import Task
from datetime import date
#from _config import DATABASE_PATH

# create the database and the db table
db.create_all()

# insert data
#db.session.add(Task("Finish this tutorial", date(2015, 3, 13), 10, 1))
#db.session.add(Task("Finish Real Python", date(2015, 3, 13), 10, 1))
# commit the changes
db.session.commit()


#with sqlite3.connect(DATABASE_PATH) as connection:
#    c = connection.cursor()
#    c.execute(""" CREATE TABLE tasks (task_id INTEGER PRIMARY KEY AUTOINCREMENT,
#              name TEXT NOT NULL, due_date TEXT NOT NULL,
#              priority INTEGER NOT NULL, status INTEGER NOT NULL)""")
#    c.execute(
#        'INSERT INTO tasks (name, due_date, priority, status)'
#        'VALUES("Finish this tutorial", "10/25/2015", 10, 1)'
#        )
#    c.execute(
#        'INSERT INTO tasks (name, due_date, priority, status)'
#        'VALUES("Finish Real Python Course 2", "12/15/2015", 10, 1)'
#        )
