from json import loads

from kafka import KafkaConsumer


class KafkaConsumerHelper:

    def __init__(self, topic, server):
        """
        Constructor for the class for Kafka Consumer Helper.
        Will initialize the KafkaConsumer with kafka connection,
        auto_offset_reset: earliest - a policy for resetting offsets on OffsetOutOfRange errors,
        ‘earliest’ will move to the oldest available message
        value_deserializer - deserialize the message json
        """
        self.consumer = KafkaConsumer(topic, bootstrap_servers=server, auto_offset_reset='earliest',
                                      enable_auto_commit=True, group_id='my-group',
                                      value_deserializer=lambda x: loads(x.decode('utf-8')))

    def poll(self):
        """
        Return the consumer instance
        """
        return self.consumer
