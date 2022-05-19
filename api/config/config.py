import os

ALLOW_ORIGINS = os.environ.get("ALLOW_ORIGINS", "http://localhost:3000")
MONGO_CONNECTION_URL = "mongodb://root:root@db:27017/autolycus?retryWrites=true&w=majority&authSource=admin"
