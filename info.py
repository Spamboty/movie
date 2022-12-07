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
BOT_TOKEN = getenv("BOT_TOKEN', '5901655383:AAHJaLkJRdBk8J9OBihd7slkPuAbHP3NwQg")

# Bot settings
CACHE_TIME = int(getenv('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(getenv('USE_CAPTION_FILTER', False))
PICS = (getenv('PICS', 'https://telegra.ph//file/b12246b0780a927bc8190.jpg https://telegra.ph/file/b417bdd01331179d5787c.jpg https://telegra.ph/file/775ee57c7a7550ad611ed.jpg')).split()

# Admins, Channels & Users
ADMINS = getenv('ADMINS', '5463205082')
CHANNELS = getenv('CHANNELS', ' -1001863651025')
AUTH_USERS = getenv('AUTH_USERS', '5463205082')
AUTH_CHANNEL = getenv('AUTH_CHANNEL', ' -1001863651025')
AUTH_GROUP = getenv('AUTH_GROUP', '-1001666282080')

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
CUSTOM_FILE_CAPTION = getenv("CUSTOM_FILE_CAPTION", "📁 ➜ {file_name} @Star_MoviesHub\n🦋 𝗙𝗶𝗿𝘀𝘁 𝗢𝗻 𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗺 🦋\n\n𝐑𝐞𝐪𝐮𝐞𝐬𝐭 𝐘𝐨𝐮𝐫 𝐌𝐨𝐯𝐢𝐞𝐬 𝐇𝐞𝐫𝐞 𝐀𝐧𝐝 𝐆𝐞𝐭 𝐈𝐧 1 𝐌𝐢𝐧𝐮𝐭𝐞 100℅ 👇\nhttps://t.me/Star_MoviesHub\nयहां अपनी फिल्मों का अनुरोध करें और 1 मिनट में प्राप्त करें 100℅ 👇\nhttps://t.me/Star_MoviesHub\n\n╔══ 𝐉𝐨𝐢𝐧 𝐖𝐢𝐭𝐡 𝐔𝐬 ═══╗\nᴏғғɪᴄɪᴀʟ @star_x_network\nMᴏᴠɪᴇs @Star_X_Movies\nsᴜᴘᴘᴏʀᴛ @Best_FriendsFor_Ever\n╚══ 𝐉𝐨𝐢𝐧 𝐖𝐢𝐭𝐡 𝐔𝐬 ═══╝\n✯ ━━━━━ ✧ ━━━━━ ✯")
BATCH_FILE_CAPTION = getenv("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = getenv("IMDB_TEMPLATE", "<b>Your Query: {query}</b> \n‌IMDb Data by: @Star_X_Network \n\n🏷 Title: <a href={url}>{title}</a>\n🎭 Genres: {genres}\n📆 Year: <a href={url}/releaseinfo>{year}</a>\n🌟 Rating: <a href={url}/ratings>{rating}</a> / 10 \n\n♥️ we are nothing without you ♥️ \n\n💛 Please Share Us 💛\n\n⚠️Click on the button 👇 below to get your query privately")
LONG_IMDB_DESCRIPTION = (getenv("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = (getenv("SPELL_CHECK_REPLY", "True"), False)
MAX_LIST_ELM = getenv("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(getenv('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = int(getenv('FILE_STORE_CHANNEL', '-1001682125120')).split()
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
