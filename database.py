import sqlite3
import json

def deserialize():
    f = open('accounts.json')
    data = json.load(f)
    for item in data:
        write_record(item['id'], item['name'], item['ssn'], item['address'])

def init():
    conn = sqlite3.connect('api.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE accounts (
            id INTEGER,
            username TEXT,
            ssn INTEGER,
            address TEXT
            )""")
    conn.close()

def write_record(id_num, name, ssn, address):
    conn = sqlite3.connect('api.db')
    c = conn.cursor()
    c.execute("INSERT INTO accounts VALUES (?,?,?,?)", (id_num, name, ssn, address))
    print(f'{id_num} {name} {ssn} {address}')
    print()
    conn.commit()
    conn.close()

def retreive_record(id_num):
    conn = sqlite3.connect('api.db')
    c = conn.cursor()
    c.execute("SELECT * FROM accounts WHERE id = (?)", (id_num,))
    items = c.fetchall()
    my_dict = {}
    my_keys = ['id', 'name', 'ssn', 'address']
    for i, item in enumerate(items[0]):
        my_dict.update({my_keys[i]: item})
    conn.close()
    return my_dict

def retreive_all():
    conn = sqlite3.connect('api.db')
    c = conn.cursor()
    c.execute("SELECT * FROM accounts")
    items = c.fetchall()
    my_dict = {}
    my_keys = ['id', 'name', 'ssn', 'address']
    output = []
    for x in range(len(items)):
        for i, item in enumerate(items[x]):
            my_dict.update({my_keys[i]: item})
        output.append(my_dict)
        my_dict = {}
    conn.close()
    return output

if __name__ == '__main__':
    # Initialize DB
    #init()
    # Populate DB
    #deserialize()
    #retreive_record(31433215)
    retreive_all()
    