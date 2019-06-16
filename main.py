# Starting point for fetching and saving responses to forms hosted by ona platform
import os
from dotenv import load_dotenv
from models.fetcher import Fetcher
load_dotenv()

# Assign Ona account ID to variable
dataID = os.environ.get("DATA_ID")
print('Begin')
# Initialize Fetcher class
fetcher = Fetcher(dataID)
# Fetch data
docsSaved = fetcher.fetchData()
print('DONE')
# Fetch data
fetcher.fetchData()
