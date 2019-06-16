import requests
from .saver import Saver

saver = Saver()
class Fetcher:
    def __init__(self, id):
        self._id = id

    def fetchData(self):
        print("ssssss")
        response = requests.get("https://api.ona.io/api/v1/data/{}".format(self._id))
        print(response)
        if response.status_code == 200:
            data = response.json()
            print(data)
            for record in data:
                saver.saveRecord(record)
        print("Done")
