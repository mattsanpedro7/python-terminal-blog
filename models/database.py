import pymongo

# this db is an object, and I'll define things it can do
# database inherit from object.  database will contain object's methods
class Database(object):
    # we want all connections to go through here
    # this uri will be the same for all database, static property!
    URI = "mongodb://127.0.0.1:27017"
    # db is a blueprint
    DATABASE = None

    # we don't want this:
    # def __init__(self):
    #     self.uri = ""
    #     self.database = None

    # we're not using self on this method, not an instance
    @staticmethod
    def initialize():
        # need to access URI inside class Database
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['python-udemy']