# Starting point for fetching and saving responses to forms hosted by ona platform
import os
from dotenv import load_dotenv
from models.fetcher import Fetcher
load_dotenv()
print("HI")
# Assign Ona account ID to variable
dataID = os.environ.get("DATA_ID")

# Initialize Fetcher class
fetcher = Fetcher(dataID)
print('DONE')
# # Fetch data
# fetcher.fetchData()
