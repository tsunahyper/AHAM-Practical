import sqlite3
import datetime
conn = sqlite3.connect('investmentfund.db')

cursor = conn.cursor()


#CREATE TABLE
cursor.execute("""CREATE TABLE IF NOT EXISTS invest_fund (
            fund_id integer PRIMARY KEY, 
            fund_name text, 
            fund_manager text, 
            description text, 
            nav integer, 
            creation_date text, 
            performance real
    )""")

conn.commit()
conn.close()

# Fetch Fund Data
def get_all_fund(cursor):
    cursor.execute("""SELECT * FROM invest_fund""")
    return (cursor.fetchall())

def get_fund_id_query(cursor,fund_id):
    cursor.execute(f"""SELECT * FROM invest_fund where fund_id = {fund_id}""")
    return (cursor.fetchall())

# Migrate data from SQLite to SQL (currently using SQLite to insert as an example of db structure)
def create_new_fund(cursor,resp):
    cursor.execute("""
        INSERT INTO invest_fund (
            fund_id, 
            fund_name, 
            fund_manager, 
            description, 
            nav, 
            creation_date, 
            performance
        )
        VALUES
        (
            ?, 
            ?, 
            ?, 
            ?, 
            ?, 
            ?, 
            ?
        )""", (resp.fund_id,resp.fund_name,resp.fund_manager,resp.description,resp.nav,resp.creation_date,resp.performance))
    return ("Success")


def update_new_fund(cursor,resp):
    cursor.execute("""
        UPDATE invest_fund set
            fund_name = ?, 
            fund_manager = ?, 
            description = ?, 
            nav = ?, 
            performance = ?
        WHERE
            fund_id = ?""", (resp.fund_name,resp.fund_manager,resp.description,resp.nav,resp.performance,resp.fund_id))
    return ("Success")

def delete_fund_query(cursor, resp):
    cursor.execute("""
        DELETE FROM invest_fund where fund_id = ?""", (resp,))
    return ("Success")
