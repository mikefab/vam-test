import requests
from .saver import Saver

saver = Saver()
class Fetcher:
    def __init__(self, id):
        self._id = id

    def fetchData(self):
        response = requests.get("https://api.ona.io/api/v1/data/{}".format(self._id))
        if response.status_code == 200:
            data = response.json()
            for record in data:
                saver.saveRecord(record)
        print("Done")
