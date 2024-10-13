import os
from dotenv import load_dotenv

#Loading env variables from .env file
#Use git secret intead
# load_dotenv()

print(os.getenv("NGROK_AUTHTOKEN"))

for key, value in os.environ.items():
    print(f'{key}: {value}')