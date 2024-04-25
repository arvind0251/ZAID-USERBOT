import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "26495505")) #optional
API_HASH = getenv("API_HASH", "41ce1aa633c6ae79b928ddd4caefc245") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
OWNER_ID = int(getenv("OWNER_ID"))
MONGO_URL = getenv("mongodb+srv://BrandedSupportGroup:BRANDED_WORLD@cluster0.v4odcq9.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "6265302593:AAGiQvKqmgyunJcicKnfo4tD3CGy09HAlXc")
ALIVE_PIC = getenv("ALIVE_PIC", 'https://telegra.ph/file/ee5d441f240fdd88e5a8b.jpg')
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/prashantsahlot/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BQGUShEApZ498PW81hSMFLjTWstTwMNG-TYUuG4CYVx9GPz93AKmdUK9SpETruMAlGuMdMJUlpewewZ7qnBmMp4suhx1snZZFz6AeDkMx4i7pitgyR-056WcTkU2neGJ1x71_pCLD8m-gn7S-F0zZpekcbDwyXQxKO_DimPPE-PoHTmEUaLPmt03pIEHtjRYiEFeKO0l-uVH1XCCQXPO1F4PFvdgH7Kg1kvHsTMU69YxrFlMhlbTU6SwLm1UgpvsDBnjkIMZwySPoNz7M3nvQ9bFmKeGsUxSNpISEOPXZOkZdxLWGPJ6PR14MQY_iqhRfkGYSoqa5zK2NUYteKKMNPKWCrswAAAABjczLPAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
