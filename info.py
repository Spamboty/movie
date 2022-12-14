import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Bot information
SESSION = getenv('SESSION', 'Media_search')
API_ID = int(getenv("API_ID", "9751271"))
API_HASH = getenv("API_HASH", "e87e2408580dd82aa9946b5732db6553")
BOT_TOKEN = getenv("BOT_TOKEN", "5901655383:AAHJaLkJRdBk8J9OBihd7slkPuAbHP3NwQg")

# Bot settings
CACHE_TIME = int(getenv('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(getenv('USE_CAPTION_FILTER', False))
PICS = (getenv('PICS', 'https://telegra.ph//file/b12246b0780a927bc8190.jpg https://telegra.ph/file/b417bdd01331179d5787c.jpg https://telegra.ph/file/775ee57c7a7550ad611ed.jpg')).split()

# Admins, Channels & Users
ADMINS = getenv('ADMINS', '5463205082')
CHANNELS = getenv('CHANNELS', ' -1001863651025')
auth_users = getenv('AUTH_USERS', '5463205082')
auth_channel = getenv('AUTH_CHANNEL', ' -1001863651025')
auth_group = getenv('AUTH_GROUP', '-1001666282080')

# MongoDB information
DATABASE_URI = getenv('DATABASE_URI', "mongodb+srv://movies:7234049299@cluster0.mc1he3h.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = getenv('DATABASE_NAME', "cluster0")
COLLECTION_NAME = getenv('COLLECTION_NAME', 'Telegram_files')

# Others
LOG_CHANNEL = int(getenv('LOG_CHANNEL', '-1001553184345'))
SUPPORT_CHAT = getenv('SUPPORT_CHAT', 'Best_FriendsFor_Ever')
P_TTI_SHOW_OFF = (getenv('P_TTI_SHOW_OFF', "False"), False)
IMDB = (getenv('IMDB', "True"), True)
SINGLE_BUTTON = (getenv('SINGLE_BUTTON', "False"), False)
CUSTOM_FILE_CAPTION = getenv("CUSTOM_FILE_CAPTION", "๐ โ {file_name} @Star_MoviesHub\n๐ฆ ๐๐ถ๐ฟ๐๐ ๐ข๐ป ๐ง๐ฒ๐น๐ฒ๐ด๐ฟ๐ฎ๐บ ๐ฆ\n\n๐๐๐ช๐ฎ๐๐ฌ๐ญ ๐๐จ๐ฎ๐ซ ๐๐จ๐ฏ๐ข๐๐ฌ ๐๐๐ซ๐ ๐๐ง๐ ๐๐๐ญ ๐๐ง 1 ๐๐ข๐ง๐ฎ๐ญ๐ 100โ ๐\nhttps://t.me/Star_MoviesHub\nเคฏเคนเคพเค เคเคชเคจเฅ เคซเคฟเคฒเฅเคฎเฅเค เคเคพ เคเคจเฅเคฐเฅเคง เคเคฐเฅเค เคเคฐ 1 เคฎเคฟเคจเค เคฎเฅเค เคชเฅเคฐเคพเคชเฅเคค เคเคฐเฅเค 100โ ๐\nhttps://t.me/Star_MoviesHub\n\nโโโ ๐๐จ๐ข๐ง ๐๐ข๐ญ๐ก ๐๐ฌ โโโโ\nแดาาษชแดษชแดส @star_x_network\nMแดแด?ษชแดs @Star_X_Movies\nsแดแดแดแดสแด @Best_FriendsFor_Ever\nโโโ ๐๐จ๐ข๐ง ๐๐ข๐ญ๐ก ๐๐ฌ โโโโ\nโฏ โโโโโ โง โโโโโ โฏ")
BATCH_FILE_CAPTION = getenv("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = getenv("IMDB_TEMPLATE", "<b>Your Query: {query}</b> \nโIMDb Data by: @Star_X_Network \n\n๐ท Title: <a href={url}>{title}</a>\n๐ญ Genres: {genres}\n๐ Year: <a href={url}/releaseinfo>{year}</a>\n๐ Rating: <a href={url}/ratings>{rating}</a> / 10 \n\nโฅ๏ธ we are nothing without you โฅ๏ธ \n\n๐ Please Share Us ๐\n\nโ?๏ธClick on the button ๐ below to get your query privately")
LONG_IMDB_DESCRIPTION = (getenv("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = (getenv("SPELL_CHECK_REPLY", "True"), False)
MAX_LIST_ELM = getenv("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(getenv('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = (getenv('FILE_STORE_CHANNEL', '-1001682125120'))
MELCOW_NEW_USERS = (getenv('MELCOW_NEW_USERS', "True"), True)
PROTECT_CONTENT = (getenv('PROTECT_CONTENT', "True"), False)
PUBLIC_FILE_STORE = (getenv('PUBLIC_FILE_STORE', "False"), False)

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
