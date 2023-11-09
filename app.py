from flask import Flask, Blueprint
from task_2_n_6 import *
app = Flask(__name__)

bp = Blueprint('aham', __name__)

@bp.route('/funds', methods=['GET'])
def get_all_funds():
    return retrieve_fund()

@bp.route('/funds', methods=['POST'])
def new_fund():
    return create_fund()

@bp.route('/funds/<fund_id>', methods=['GET'])
def retrieve_id_fund(fund_id):
    return get_fund_id(fund_id)

@bp.route('/funds/<fund_id>', methods=['PUT'])
def update_fund(fund_id):
    return update_fund_id(fund_id)

@bp.route('/funds/<fund_id>', methods=['DELETE'])
def delete_fund(fund_id):
    return delete_fund_id(fund_id)


app.register_blueprint(bp, url_prefix='/aham')
if __name__ == '__main__':
    app.run(debug=True)
