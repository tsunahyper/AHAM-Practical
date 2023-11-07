import sqlite3
import datetime
conn = sqlite3.connect('investmentfund.db')

cursor = conn.cursor()

# current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# print(current_time)
# print(type(current_time))
# cursor.execute("""CREATE TABLE IF NOT EXISTS invest_fund (
#             fund_id integer PRIMARY KEY, 
#             fund_name text, 
#             fund_manager text, 
#             description text, 
#             nav integer, 
#             creation_date text, 
#             performance real
#     )""")

# conn.commit()
# conn.close()

# def insert_dummy_data():
# cursor.execute(f"""INSERT INTO invest_fund (
#         fund_id, 
#         fund_name, 
#         fund_manager, 
#         description, 
#         nav, 
#         creation_date, 
#         performance
#     )
#         VALUES(
#             111, 
#             'RONALDO', 
#             'JOSE MOURINHO', 
#             'invest from football club', 
#             10111, 
#             '2023-11-07 00:11:14', 
#             50.1
#     )""")

# conn.commit()
# conn.close()


def get_all_fund(cursor):
    cursor.execute("""SELECT * FROM invest_fund""")
    return (cursor.fetchall())

def get_fund_id_query(cursor,fund_id):
    cursor.execute(f"""SELECT * FROM invest_fund where fund_id = {fund_id}""")
    return (cursor.fetchall())
    
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
    
    conn.commit()
    conn.close()
    return ("Success")


def update_new_fund(cursor,resp):
    cursor.execute("""
        UPDATE invest_fund set(
            fund_name = ?, 
            fund_manager = ?, 
            description = ?, 
            nav = ?, 
            creation_date = ?, 
            performance = ?
        WHERE
            fund_id = ?""", (resp.fund_name,resp.fund_manager,resp.description,resp.nav,resp.creation_date,resp.performance,resp.fund_id))
    
    conn.commit()
    conn.close()
    return ("Success")