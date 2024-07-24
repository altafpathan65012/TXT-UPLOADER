import os

API_ID = API_ID =  

API_HASH = os.environ.get("API_HASH", "")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", ))

LOG = ,

# UPDATE_GRP = , # bot sat group

# auth_chats = []

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1923922961").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


