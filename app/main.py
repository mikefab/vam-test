# Starting point for fetching and saving responses to forms hosted by ona platform
import os
import time
from dotenv import load_dotenv
from models.fetcher import Fetcher
load_dotenv()
print("HI")
# Assign Ona account ID to variable
dataID = os.environ.get("DATA_ID")

# Initialize Fetcher class
fetcher = Fetcher(dataID)
# Fetch data
# fetcher.fetchData()
time.sleep( 5999999999 )
print('DONE')
