import logging
import sys
from os import environ

import requests

from app.utils.kafka_producer import KafkaProducerHelper
logger = logging.getLogger(__name__)


class CustomerFacing:
    def __init__(self):
        """
        Constructor for the class for customer facing.
        Will initialize the KafkaProducerHelper with kafka connection from env and the
        customer management service url
        """
        if any(param is None for param in (environ.get('CUSTOMER_URL'), environ.get("KAFKA_CONNECTION"))):
            sys.exit("Failed find env of: CUSTOMER_URL, KAFKA_CONNECTION")
        self.kafka = KafkaProducerHelper(topic="orders", server=[environ.get("KAFKA_CONNECTION")])
        self.customer_url = environ.get('CUSTOMER_URL')

    def buy(self, message):
        """
        buy method for add new order, get json body and send it to kafka
        :param message: json order body message
        """

        try:
            self.kafka.send(message)
            return {"status": "ok"}
        except Exception as e:
            logger.exception(e)
            return {"status": "error", "error": e}

    def get_orders(self, user_name):
        """
        get orders for username , get username and get from the customer managment service the orders
        :param user_name: username of user
        """

        try:
            result = requests.get(url=f"{self.customer_url}/?username={user_name}")
            return result.json()
        except requests.exceptions.RequestException as e:
            logger.exception(e)
            return {"status": "error", "error": e}

