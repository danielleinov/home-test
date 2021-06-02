import pymongo


class MongoHelper:

    def __init__(self, connection_string):
        """
        Constructor for the class for Mongo Helper.
        Will initialize the MongoClient with mongo connection string
        The DB of this application will TEST - Can move to ENV
        """
        self.mongo_client = pymongo.MongoClient(connection_string)
        self.db = self.mongo_client.Test

    def insert(self, collection, document):
        """
        Insert the document to Mongo db
        :param collection: collection to insert the document
        :param document: document to insert
        """
        return self.db[collection].insert_one(document)

    def find(self, collection, query):
        """
        Find matching documents from collection by query
        :param collection: collection to run query
        :param query: query to run
        """
        return self.db[collection].find(query)