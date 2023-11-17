from dotenv import load_dotenv
import os

load_dotenv()
AZURE_TEXTANALYTICS_KEY = os.getenv("AZURE_TEXTANALYTICS_KEY")
AZURE_TEXTANALYTICS_ENDPOINT = os.getenv("AZURE_TEXTANALYTICS_ENDPOINT")
YOUTUBE_DEVELOPER_KEY = os.getenv("YOUTUBE_DEVELOPER_KEY")