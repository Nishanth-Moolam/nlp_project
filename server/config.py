import os
import secrets

# sqlalchemy config
sql_alchemy_database_uri = "sqlite:///nlpproject.db"
secret_key = secrets.secret_key

# absolute path
server_path = os.path.abspath('')

# url hosted ( change if you ever deploy )
url = 'http://localhost:5000'

# environment variables with expertai credentials
os.environ["EAI_USERNAME"] = secrets.expertai_username
os.environ["EAI_PASSWORD"] = secrets.expertai_password