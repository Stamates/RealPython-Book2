import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()
    # Create population table
    #c.execute("""CREATE TABLE population
    #               (city TEXT, state TEXT, population INT)
    #               """)
    #c.execute("INSERT INTO population VALUES('New York City', 'NY', 8200000)")
    #c.execute("INSERT INTO population VALUES('San Fran', 'CA', 8000000)")
    cities = [
        ('Boston', 'MA', 600000),
        ('Chicago', 'IL', 2700000),
        ('Houston', 'TX', 2100000),
        ('Phoenix', 'AZ', 1500000),
    ]
    c.executemany('INSERT INTO population VALUES(?,?,?)', cities)