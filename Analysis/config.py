from dotenv import load_dotenv
import os
load_dotenv()


API_BASE = os.getenv('API_BASE', 'https://bluemutualfund.in/server/api/company.php')
API_KEY = os.getenv('API_KEY', 'ghfkffu6378382826hhdjgk')
DB_URI = os.getenv('DB_URI', 'mysql+pymysql://user:pass@localhost:3306/financial')
REQUEST_TIMEOUT = int(os.getenv('REQUEST_TIMEOUT', '10'))