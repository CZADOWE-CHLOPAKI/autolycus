import os

ALLOW_ORIGINS = os.environ.get("ALLOW_ORIGINS", "http://localhost:3000")
# MONGO_CONNECTION_URL = "mongodb://root:root@mongo:27017"
MONGO_CONNECTION_URL = "mongodb://localhost:27017"
