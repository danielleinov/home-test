from datetime import datetime

from flask import request, jsonify, Blueprint
from app.models import *
main_route = Blueprint('main', __name__)


@main_route.route("/getAllUsersOrders", methods=['GET'])
def get_customer_orders():
    """
    get username orders endpoint
    """
    user_name = request.args.get('username', None)
    if user_name is None:
        return jsonify({"status": "error", "error": "Missing username"})
    return jsonify(customer.get_orders(user_name))


@main_route.route("/buy", methods=['POST'])
def buy():
    """
    buy endpoint get the parameters from json body and add timestamp
    """
    parameters = ("username", "userid", "price")
    hook = request.json
    if all(key in hook for key in parameters):
        hook['timestamp'] = datetime.now().isoformat()
        return jsonify(customer.buy(message=hook))
    return jsonify({"status": "error", "error": "Missing parameters"})