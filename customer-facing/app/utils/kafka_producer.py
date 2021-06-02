from json import dumps

from kafka import KafkaProducer


class KafkaProducerHelper:

    def __init__(self, topic, server):
        """
        Constructor for the class for kafka producer helper.
        Will initialize the KafkaProducer with kafka connection and
        value_serializer that used to convert user-supplied message values to bytes
        :param topic: where the message will be published
        :param server: kafka url
        """
        self.producer = KafkaProducer(bootstrap_servers=server,
                                      value_serializer=lambda x: dumps(x).encode('utf-8'))
        self.topic = topic

    def send(self, message):
        """
        Send the message to kafka
        :param message: the message to send
        """
        return self.producer.send(self.topic, value=message)

