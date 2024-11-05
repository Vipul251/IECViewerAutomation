from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Configurations
BROWSER = os.getenv('BROWSER')
TIMEOUT = int(os.getenv('TIMEOUT', 10))
