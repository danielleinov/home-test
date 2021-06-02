from flask import request, jsonify, Blueprint
from app.models import *
main_route = Blueprint('main-route', __name__)


@main_route.route("/", methods=['GET'])
def get_customer_orders():
    """
    Endpoint for get customer orders by username
    """
    user_name = request.args.get('username', None)
    if user_name is None:
        return jsonify({"status": "error", "error": "Missing username"})
    return jsonify(customer.get_orders(user_name))
