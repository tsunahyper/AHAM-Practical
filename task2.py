import task1
from task_3_n_4 import *
from flask import request, jsonify

funds=[]

def retrieve_fund():
    #Get all Fund
    conn = sqlite3.connect('investmentfund.db')
    cursor = conn.cursor()
    fetch_all_fund = get_all_fund(cursor)
    conn.commit()
    conn.close()
    return jsonify(fetch_all_fund)

def create_fund():
    data = request.get_json()
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    conn = sqlite3.connect('investmentfund.db')
    cursor = conn.cursor()
    fund_id = data['fund_id']
    resp = task1.investment_fund(
        fund_id,
        data['fund_name'],
        data['fund_manager'],
        data['description'],
        data['nav'],
        current_time,
        data['performance']
    )
    
    create_fund = create_new_fund(cursor,resp)
    
    if create_fund == 'Success':
        get_fund = get_all_fund(cursor)
        conn.commit()
        conn.close()
        print(get_fund)
        return jsonify(get_fund), 201
    conn.close()
    return "Error: Create Fund Error", 500

def get_fund_id(fund_id):
    # Retrieve details of a specific fund using its ID
    conn = sqlite3.connect('investmentfund.db')
    cursor = conn.cursor()
    fetch_fund_id = get_fund_id_query(cursor,fund_id)
    conn.commit()
    conn.close()
    if fetch_fund_id:
        return jsonify(fetch_fund_id)
    return "Error: Fund not found", 404

def update_fund_id(fund_id):
    # Update the performance of a fund using its ID
    data = request.get_json()
    conn = sqlite3.connect('investmentfund.db')
    cursor = conn.cursor()
    conn.commit()
    resp = task1.investment_fund(
        fund_id,
        data['fund_name'],
        data['fund_manager'],
        data['description'],
        data['nav'],
        data['creation_date'],
        data['performance']
    )

    update_fund = update_new_fund(cursor,resp)
    if update_fund == 'Success':
        funds = get_fund_id_query(cursor,fund_id)
        conn.commit()
        conn.close()
        return jsonify(funds), 200
    conn.close()
    return "Error: Update Fund", 404 

def delete_fund_id(fund_id):
    # Delete a fund using its ID
    conn = sqlite3.connect('investmentfund.db')
    cursor = conn.cursor()
    del_fund = delete_fund_query(cursor,fund_id)
    if del_fund == 'Success':
        conn.commit()
        conn.close()
        return jsonify(f"Fund deleted {fund_id}"), 204
    conn.close()
    return "Error: Fund not found", 404
