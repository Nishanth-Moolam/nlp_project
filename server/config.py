import os
import secrets

# sqlalchemy config
sql_alchemy_database_uri = "sqlite:///nlpproject.db"
secret_key = secrets.secret_key

# absolute path
server_path = os.path.abspath('')

# microsoft computer vision coonfig
ms_computer_vision_ocr_url = "https://microsoft-computer-vision3.p.rapidapi.com/ocr"
ms_computer_vision_ocr_query_string = {"detectOrientation":"true","language":"unk"}
ms_computer_vision_headers = {
    'content-type': "application/json",
    'x-rapidapi-key': secrets.rapidapi_key,
    'x-rapidapi-host': "microsoft-computer-vision3.p.rapidapi.com"
    }

