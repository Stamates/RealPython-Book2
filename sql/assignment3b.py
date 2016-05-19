import csv
import sqlite3

with sqlite3.connect("new_num.db") as connection:
    c = connection.cursor()
    valid = ['AVG', 'MAX', 'MIN', 'SUM', 'EXIT']
    while True:
        ag = None
        while ag not in valid:
            ag = raw_input("Type in the aggregation method (AVG, MAX, MIN, SUM) or type EXIT to quit: ").upper()
        if ag == 'EXIT':
            break
        select = "SELECT " + ag + "(number) FROM numbers"
        c.execute(select)
        result = c.fetchone()
        print "The " + str(ag) + " is: " + str(result[0])

        
    
