##Config

from os import getenv

from dotenv import load_dotenv

load_dotenv()
SESSION_NAME = getenv('SESSION_NAME', 'BQBOxFTaBuUaF4psKwBQe00BtD7WjnL57jUiScJ8o3rgcoAMV7jMbfI2nXL8F6JFNeRn2dA_1ic41XcACqP2hOeCMvp9HTYU03WyWq08CjGV_6m9xL3TptFNbiSxZyxU3B-WpgypU5K7cRscj-5gUvjW899J58FDVtw_rhgxZZZal0ZBmhjVh_C_MEbLlr43Bj7jymgH-0sOKFxEVsew1dT8Td0LidfdCaM-FYezKlw41ThSi1ofAjGpF-uO02S0mzDom8UST9blvfChI3aZkBmqa_uepFGH689e9CelszB1QneQKKAzJRytQRAEIpZNLilb_FkylabHiVDCGt72JRKFAAAAAWukHPAA')
BOT_TOKEN = getenv('BOT_TOKEN', '6844430863:AAHb5fws_ZQz5iVRSsI4EFNhraT225qID18')
API_ID = int(getenv('API_ID', '20865323'))
API_HASH = getenv('API_HASH','3dce0c91cda24747656e704808a684e8')
DURATION_LIMIT = int(getenv('DURATION_LIMIT', '54000'))
COMMAND_PREFIXES = list(getenv('COMMAND_PREFIXES', '/ . , : ; !').split())
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://SKARMAAN:jAXllZggCqEN3eLe@cluster0.vlcmrpo.mongodb.net/?retryWrites=true&w=majority")
SUDO_USERS = list(map(int, getenv('SUDO_USERS', '1103636187 5191699870').split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", '-1001932566732'))
ASS_ID = int(getenv("ASS_ID", '6100884720'))
OWNER_ID = list(map(int, getenv('OWNER_ID', '5332414680').split()))
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "Grab_Your_WH_Group")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "WOFBotsUpdates")
GROUP = getenv("GROUP", "Grab_Your_WH_Group"")
CHANNEL = getenv("CHANNEL", "WOFBotsUpdates")
