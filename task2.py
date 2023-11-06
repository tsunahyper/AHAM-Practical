import task1
from flask import request, jsonify

funds=[]

def retrieve_fund():
    
    return jsonify(list(funds.values())) if funds else None

def create_fund():
    data = request.get_json()
    fund_id = data['fund_id']
    resp = task1.investment_fund(
        fund_id,
        data['fund_name'],
        data['fund_manager'],
        data['description'],
        data['nav'],
        data['creation_date'],
        data['performance']
    )
    
    fund_dict = {
        "fund_id": resp.fund_id,
        "fund_name": resp.fund_name,
        "fund_manager": resp.fund_manager,
        "description": resp.description,
        "nav": resp.nav,
        "creation_date": resp.creation_date,
        "performance": resp.performance
    }
    funds = fund_dict
    
    return jsonify(funds), 201

def get_fund_id(fund_id):
    # Retrieve details of a specific fund using its ID
    if fund_id in funds:
        return jsonify(funds[fund_id].__dict__)
    return "Fund not found", 404

def update_fund_id(fund_id):
    # Update the performance of a fund using its ID
    if fund_id in funds:
        data = request.get_json()
        funds[fund_id].performance = data['performance']
        return jsonify(funds[fund_id].__dict__), 200
    return "Fund not found", 404

def delete_fund_id(fund_id):
    # Delete a fund using its ID
    if fund_id in funds:
        del funds[fund_id]
        return "Fund deleted", 204
    return "Fund not found", 404
