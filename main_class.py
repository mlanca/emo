import os
import sqlite3
import datetime
from sqlite3.dbapi2 import IntegrityError


class main_class:
    """  """
    def __init__(self, db_name):
        self.db_name = db_name

    def list_clients(self):
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()
        for row in cur.execute('SELECT email FROM client ORDER BY email'):
            print(row[0])
        con.close()

    def add_client(self):
        fn = input("Enter the first name: ")
        em = input("Enter the email: ")
        no = str(datetime.datetime.now())
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()
        sql = 'INSERT INTO client(fname,email,created) VALUES(?, ?, ?);'
        data = (fn, em, no)
        try:    
            print("...working...")
            cur.execute(sql, data)
            con.commit()
        except IntegrityError:
            print("email in use")
            try:
                os.system('pause')  #windows, doesn't require enter
            except:
                os.system('read -p "Press any key to continue"') #linux
        if con:   
            con.close()

    def update_kv(self, opt='body'):
        su = input("Enter text: ")
        no = str(datetime.datetime.now())
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()
        sql = 'UPDATE keyvalue SET target_val = ? WHERE target = ?'
        data = (su, opt)
        try:
            print("...working...")
            cur.execute(sql, data)
            con.commit()
        except IntegrityError:
            print("whoops")
            try:
                os.system('pause')  #windows, doesn't require enter
            except:
                os.system('read -p "Press any key to continue"') #linux
        if con:   
            con.close()


    def send_email():
        pass
