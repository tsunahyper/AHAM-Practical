import sqlite3
import datetime
conn = sqlite3.connect('investmentfund.db')

cursor = conn.cursor()

current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(current_time)
print(type(current_time))
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
cursor.execute(f"""INSERT INTO invest_fund (
        fund_id, 
        fund_name, 
        fund_manager, 
        description, 
        nav, 
        creation_date, 
        performance
    )
        VALUES(
            111, 
            'RONALDO', 
            'JOSE MOURINHO', 
            'invest from football club', 
            10111, 
            '2023-11-07 00:11:14', 
            50.1
    )""")

conn.commit()
conn.close()


# def get_dummy_data():
#     cursor.execute("""SELECT * FROM invest_fund WHERE fund_id = 'F111'""")
#     print(c.fetchall())
#     conn.commit()
#     conn.close()
    
# def insert_table():
#     cursor.execute("""
#         INSERT INTO invest_fund (
#             fund_id, 
#             fund_name, 
#             fund_manager, 
#             description, 
#             nav, 
#             creation_date, 
#             performance
#         )
#         VALUES
#         (
#             :fund_id, 
#             :fund_name, 
#             :fund_manager, 
#             :description, 
#             :nav, 
#             :creation_date, 
#             :performance
#         )""")
    
#     conn.commit()
#     conn.close()
#     return ("Success")