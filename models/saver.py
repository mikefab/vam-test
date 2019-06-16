from pymongo import MongoClient
client = MongoClient()
db = client.mydb

class Saver:
    def saveRecord(self, record):
        exists = db.forms.find_one({'_id': record['_id']})
        if (exists == None):
            db.forms.save(record)
