import logging
import sys
from os import environ

from bson import json_util
import json

from app.utils.kafka_consumer import KafkaConsumerHelper
from app.utils.mongo_helper import MongoHelper
logger = logging.getLogger(__name__)


class CustomerManagemnt:

    def __init__(self):
        """
        Constructor for the class for customer management.
        Will initialize the KafkaConsumerHelper with kafka connection from env
        Will initialize the MongoHelper with mongo connection string from env
        """

        if any(param is None for param in (environ.get('MONGO_CONNECTION'), environ.get("KAFKA_CONNECTION"))):
            sys.exit("Failed find env of: MONGO_CONNECTION, KAFKA_CONNECTION")
        self.kafka = KafkaConsumerHelper(topic="orders", server=[environ.get("KAFKA_CONNECTION")])
        self.mongo = MongoHelper(connection_string=environ.get('MONGO_CONNECTION'))

    def consume_write_mongo(self):
        """
        Consume message from kafka and write each message to mongo
        """

        logger.info("Start polling from kafka")
        consumer = self.kafka.poll()
        for msg in consumer:
            self.mongo.insert(collection="orders", document=msg.value)

    def get_orders(self, user_name):
        """
        get orders from mongo for user by filtering by username
        :param user_name: username
        """

        try:
            result = self.mongo.find(collection="orders", query={"username": {"$eq": f"{user_name}"}})
            return json.loads(json_util.dumps(result))
        except Exception as e:
            logger.exception(e)
            return {"status": "error", "error": e}
