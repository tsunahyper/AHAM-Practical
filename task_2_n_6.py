import task_1
from validation import *
from task_3_4_5 import *
from flask import request, jsonify, abort

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
    try:
        data = request.get_json()
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        conn = sqlite3.connect('investmentfund.db')
        cursor = conn.cursor()
        
        try:
            InsertValidationBaseSchema().load(data)
            if data:
                resp = task1.investment_fund(
                    data['create_fund']['fund_id'],
                    data['create_fund']['fund_name'],
                    data['create_fund']['fund_manager'],
                    data['create_fund']['description'],
                    data['create_fund']['nav'],
                    current_time,
                    data['create_fund']['performance']
                )
            
                create_fund = create_new_fund(cursor,resp)
                
                if create_fund == 'Success':
                    get_fund = get_all_fund(cursor)
                    conn.commit()
                    conn.close()
                    print(get_fund)
                    return jsonify(get_fund), 201
                conn.close()
                abort({"Error":"Create Fund Error"}), 400
        
        except Exception as e:
            abort({"Error":"Validation Create Fund Error" + e}), 400
    except ValidationError as err:
        conn.close()
        return jsonify(err.messages), 400

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
    try:    
        data = request.get_json()
        conn = sqlite3.connect('investmentfund.db')
        cursor = conn.cursor()
        conn.commit()
        try:
            UpdateValidationBaseSchema().load(data)
            if data:
                resp = task1.investment_fund(
                    fund_id,
                    data['update_fund']['fund_name'],
                    data['update_fund']['fund_manager'],
                    data['update_fund']['description'],
                    data['update_fund']['nav'],
                    data['update_fund']['performance']
                )

                update_fund = update_new_fund(cursor,resp)
                if update_fund == 'Success':
                    funds = get_fund_id_query(cursor,fund_id)
                    conn.commit()
                    conn.close()
                    return jsonify(funds), 200
                conn.close()
                abort({"Error":"Create Fund Error"}), 400 
        except Exception as e:
            abort({"Error":"Validation Create Fund Error" + e}), 400
            
    except ValidationError as err:
        conn.close()
        return jsonify(err.messages), 400
    
    return jsonify({'message': 'Unable to Register!'}), 400
def delete_fund_id(fund_id):
    # Delete a fund using its ID
    conn = sqlite3.connect('investmentfund.db')
    cursor = conn.cursor()
    if not fund_id:
        abort({"Error":"Error Fund ID"}), 400 
        
    del_fund = delete_fund_query(cursor,fund_id)
    if del_fund == 'Success':
        conn.commit()
        conn.close()
        return jsonify(f"Fund deleted {fund_id}"), 204
    conn.close()
    abort({"Error":"Delete Fund Error"}), 400 
