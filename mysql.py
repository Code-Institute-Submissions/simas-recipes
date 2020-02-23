import os
import pymysql
from datetime import datetime

username = os.getenv('C9_USER')

connection = pymysql.connect(host='localhost',
                            user=username,
                            password='',
                            db='recipestable')

try:
    with connection.cursor() as cursor:
        #sql = "SELECT * FROM Genre;"
        
        #Inserting Single line
        #row = ('Lamb Karahi', 'Lamb, Masala, Oil, Spices','Mix Oil, Onion and Spices into a pan.', '2020-02-07 20:10:32')
        #cursor.execute("INSERT INTO recipes VALUES(%s, %s, %s, %s);", row)
        
        #Inserting mupliple lines
        #rows = [('Chicken Karahi', 'Chicken, Masala, Oil, Spices','Mix Oil, Onion and Spices into a pan.', '2019-12-17 02:17:39'),
        #        ('Chicken Korma', 'Chicken, Korma Masala, Oil, Spices','Mix Oil, Onion and Spices into a Frying pan.', '2017-10-21 12:07:00'),
        #        ('Mix Vegetable', 'Vegetables, Masala, Oil, Spices','Mix Vegetables, Oil and Spices into a pan.', '2015-03-01 04:49:28')]
        #cursor.executemany("INSERT INTO recipes VALUES(%s, %s, %s, %s);", rows)
        
        #Updating table content
        #cursor.execute('UPDATE recipes SET content = "Mix Vegetable, Masala, Oil, Spices" WHERE name = "Mix Vegetable";')
        
        #Update values Alternative Way
        #cursor.execute('UPDATE recipes SET DOC = %s WHERE name = %s;',
        #                ('2018-03-01 04:49:28', 'Mix Vegetable'))
        
        #Update many Values
        #rows = [('2020-02-06 10:17:39', 'Chicken Karahi'),
        #        ('2020-02-05 10:05:17', 'Chicken Korma'),
        #        ('2020-02-04 10:00:59', 'Mix Vegetable')]
        #cursor.executemany('UPDATE recipes SET DOC = %s WHERE name = %s;', rows)
        
        #Delete Single row from Table
        #cursor.execute('DELETE FROM recipes WHERE name = "Chicken Korma";')
        
        #Aleternate DELETE Method
        #row = cursor.execute('DELETE FROM recipes WHERE name = %s;', "Chicken Karahi")
        
        #DELETE many Methos
        #row = cursor.executemany('DELETE FROM recipes WHERE name = %s;', ["Chicken Karahi","Mix Vegetable"])
        
        #DELETE WHERE in
        list_of_name = ['Lamb Karahi', 'Chicken Korma']
        format_strings = ','.join(['%s']*len(list_of_name))
        cursor.execute("DELETE FROM recipes WHERE name in ({});".format(format_strings), list_of_name)
        connection.commit()
        
        #for row in cursor:
            #print(row)

finally:
   connection.close()
