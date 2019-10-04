import os
from configparser import ConfigParser

# Load configs file
config = ConfigParser(os.environ, strict=False)

config.read("{current_dir}/{ini_file}".format(current_dir=os.path.dirname(__file__), ini_file="app.ini"))

KBIT_API_URL = config.get("app", "kbit_api_url")
