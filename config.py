import re
import os
import time

id_pattern = re.compile(r'^.\d+$')


class Config(object):
    # pyro client config
    API_ID = os.environ.get("API_ID", "23941369")  # ⚠️ Required
    API_HASH = os.environ.get("API_HASH", "bbd37235e41a95d03bc144ea6bc7b2cd")  # ⚠️ Required
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6369881782:AAHo3a1F2NUoyNKo25yJ3RIayMrSXsImINE")  # ⚠️ Required

    # premium 4g renaming client
    STRING_API_ID = os.environ.get("STRING_API_ID", "23941369")
    STRING_API_HASH = os.environ.get("STRING_API_HASH", "bbd37235e41a95d03bc144ea6bc7b2cd")
    STRING_SESSION = os.environ.get("STRING_SESSION", "")

    # database config
    DB_NAME = os.environ.get("DB_NAME", "Snow_User_Data")
    DB_URL = os.environ.get("DB_URL", "mongodb+srv://ROKU:ROKU@cluster0.nxjre0s.mongodb.net/?retryWrites=true&w=majority")  # ⚠️ Required

    # other configs
    BOT_UPTIME = time.time()
    START_PIC = os.environ.get("START_PIC", "")
    ADMIN = [int(admin) if id_pattern.search(
        admin) else admin for admin in os.environ.get('ADMIN', '1966867320').split()]  # ⚠️ Required
    
    FORCE_SUB = os.environ.get("FORCE_SUB", "Rokubotz") # ⚠️ Required Username without @
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002046934698"))  # ⚠️ Required
    FLOOD = int(os.environ.get("FLOOD", '10'))
    BANNED_USERS = set(int(x) for x in os.environ.get(
        "BANNED_USERS", "1234567890").split())

    # wes response configuration
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    PORT = int(os.environ.get("PORT", "8080"))


class Txt(object):
    # part of text configuration
    START_TXT = """<b>Hɪ {} 👋,
Tʜɪs Is Aɴ Aᴅᴠᴀɴᴄᴇᴅ Aɴᴅ Yᴇᴛ Pᴏᴡᴇʀꜰᴜʟ Rᴇɴᴀᴍᴇ Bᴏᴛ
Usɪɴɢ Tʜɪs Bᴏᴛ Yᴏᴜ Cᴀɴ Rᴇɴᴀᴍᴇ & Cʜᴀɴɢᴇ Tʜᴜᴍʙɴᴀɪʟ Oꜰ Yᴏᴜʀ Fɪʟᴇ
Yᴏᴜ Cᴀɴ Aʟsᴏ Cᴏɴᴠᴇʀᴛ Vɪᴅᴇᴏ Tᴏ Fɪʟᴇ & Fɪʟᴇ Tᴏ Vɪᴅᴇᴏ
Tʜɪs Bᴏᴛ Aʟꜱᴏ Sᴜᴘᴘᴏʀᴛs Cᴜsᴛᴏᴍ Tʜᴜᴍʙɴᴀɪʟ Aɴᴅ Cᴜsᴛᴏᴍ Cᴀᴘᴛɪᴏɴ

➜ <a href=https://telegra.ph/File-Bot-11-28>𝖤𝗑𝗍𝗋𝖺 𝖥𝖾𝖺𝗍𝗎𝗋𝖾</a>
"""

    ABOUT_TXT = """<b>🤖 𝖬𝗒 𝗇𝖺𝗆𝖾: <a href=http://t.me/FZXUltraRenameBot>𝖥𝖹𝖷 𝖴𝗅𝗍𝗋𝖺 𝖱𝖾𝗇𝖺𝗆𝖾 𝖡𝗈𝗍</a>
📚 𝖫𝗂𝖻𝗋𝖺𝗋𝗒: <a href=https://github.com/pyrogram>𝖯𝗒𝗋𝗈𝗀𝗋𝖺𝗆</a>
🚀 𝖲𝖾𝗋𝗏𝖾𝗋 : <a href=https://www.cloudflare.com>𝖢𝗅𝗈𝗎𝖽𝖿𝗅𝖺𝗋𝖾</a>
📝 𝖫𝖺𝗇𝗀𝗎𝖺𝗀𝖾: <a href=https://www.python.org>𝖯𝗒𝗍𝗁𝗈𝗇3</a>
💾 𝖣𝖺𝗍𝖺𝖡𝖺𝗌𝖾: <a href=https://cloud.mongodb.com>𝖬𝗈𝗇𝗀𝗈𝖣𝖡</a>
🧑‍💻 𝖣𝖾𝗏𝖾𝗅𝗈𝗉𝖾𝗋: <a href=https://telegram.me/MysterySD>꧁❏รเlєภt ๔є๓๏ภ❏꧂</a>

♻️ 𝖯𝗈𝗐𝖾𝗋𝖾𝖽 𝖡𝗒: <a href=https://telegram.me/Rokubotz>𝖱𝗈𝗄𝗎𝖻𝗈𝗍𝗓</a> </b>
 """

    HELP_TXT = """
🌌 <b><u>Hᴏᴡ Tᴏ Sᴇᴛ Tʜᴜᴍʙɴɪʟᴇ</u></b>
  
<b>•></b> /start Tʜᴇ Bᴏᴛ Aɴᴅ Sᴇɴᴅ Aɴy Pʜᴏᴛᴏ Tᴏ Aᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟy Sᴇᴛ Tʜᴜᴍʙɴɪʟᴇ.
<b>•></b> /del_thumb Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Dᴇʟᴇᴛᴇ Yᴏᴜʀ Oʟᴅ Tʜᴜᴍʙɴɪʟᴇ.
<b>•></b> /view_thumb Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Vɪᴇᴡ Yᴏᴜʀ Cᴜʀʀᴇɴᴛ Tʜᴜᴍʙɴɪʟᴇ.


📑 <b><u>Hᴏᴡ Tᴏ Sᴇᴛ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ</u></b>

<b>•></b> /set_caption - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Sᴇᴛ ᴀ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ
<b>•></b> /see_caption - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Vɪᴇᴡ Yᴏᴜʀ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ
<b>•></b> /del_caption - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Dᴇʟᴇᴛᴇ Yᴏᴜʀ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ
Exᴀᴍᴩʟᴇ:- <code> /set_caption 📕 Fɪʟᴇ Nᴀᴍᴇ: {filename}
💾 Sɪᴢᴇ: {filesize}
⏰ Dᴜʀᴀᴛɪᴏɴ: {duration} </code>

✏️ <b><u>Hᴏᴡ Tᴏ Rᴇɴᴀᴍᴇ A Fɪʟᴇ</u></b>
<b>•></b> Sᴇɴᴅ Aɴy Fɪʟᴇ Aɴᴅ Tyᴩᴇ Nᴇᴡ Fɪʟᴇ Nɴᴀᴍᴇ \nAɴᴅ Aᴇʟᴇᴄᴛ Tʜᴇ Fᴏʀᴍᴀᴛ [ document, video, audio ].           


<b>⦿ Developer:</b> <a href=https://telegram.me/MysterySD>꧁❏รเlєภt ๔є๓๏ภ❏꧂</a>

"""

    SEND_METADATA = """
<b>𝖬𝖾𝗍𝖺𝖽𝖺𝗍𝖺 𝖲𝖾𝗍𝗍𝗂𝗇𝗀 𝖥𝗈𝗋𝗆𝖺𝗍: »</b> <code>-map 0 -c:s copy -c:a copy -c:v copy -metadata title=value -metadata author=value -metadata:s:s title=value -metadata:s:a title=value -metadata:s:v title=value</code>

<b>‣ 𝖳𝗈 𝖲𝖾𝗍 𝖸𝗈𝗎𝗋 𝖢𝗎𝗌𝗍𝗈𝗆 𝖬𝖾𝗍𝖺𝖽𝖺𝗍𝖺 𝖳𝖾𝗑𝗍 𝖱𝖾𝗉𝗅𝖺𝖼𝖾 𝖳𝗁𝖾 '𝗏𝖺𝗅𝗎𝖾𝗌' 𝗐𝗂𝗍𝗁 𝗒𝗈𝗎𝗋 𝗆𝖾𝗍𝖺𝖽𝖺𝗍𝖺 𝗍𝖾𝗑𝗍</b>

<b>𝖤𝗑: »</b> <code>-map 0 -c:s copy -c:a copy -c:v copy -metadata title=@Rokubotz -metadata author=@Rokubotz -metadata:s:s title=@Rokubotz -metadata:s:a title=@Rokubotz -metadata:s:v title=@Rokubotz</code>

<b>‣ 𝖨𝖿 𝖸𝗈𝗎𝗋 𝖬𝖾𝗍𝖺𝖽𝖺𝗍𝖺 𝖳𝖾𝗑𝗍 𝖧𝖺𝗌 𝖲𝗉𝖺𝖼𝖾 𝗂𝗇 𝖡𝖾𝗍𝗐𝖾𝖾𝗇 𝖳𝗁𝖾𝗆 𝗒𝗈𝗎 𝗁𝖺𝗏𝖾 𝗍𝗈 𝗂𝗇𝗌𝖾𝗋𝗍 ' 𝖺𝗍 𝗍𝗁𝖾 𝖻𝖾𝗀𝗂𝗇𝗇𝗂𝗇𝗀 𝖺𝗇𝖽 𝗍𝗁𝖾 𝖾𝗇𝖽 𝗈𝖿 𝖾𝖺𝖼𝗁 𝗍𝖾𝗑𝗍</b>

<b>𝖤𝗑: »</b> <code>-map 0 -c:s copy -c:a copy -c:v copy -metadata title='Powered By Rokubotz' -metadata author='Powered By Rokubotz' -metadata:s:s title='Powered By Rokubotz' -metadata:s:a title='Powered By Rokubotz' -metadata:s:v title='Powered By Rokubotz'</code>


📥 𝖥𝗈𝗋 𝖬𝗈𝗋𝖾 𝖧𝖾𝗅𝗉 𝖦𝖾𝗍 𝗂𝗇 𝖳𝗈𝗎𝖼𝗁 𝖶𝗂𝗍𝗁 𝖴𝗌 𝖠𝗍 𝖮𝗎𝗋 𝖲𝗎𝗉𝗉𝗈𝗋𝗍 𝖦𝗋𝗈𝗎𝗉 @Team_Roku"""

    
    PROGRESS_BAR = """<b>\n
╭━━『𝖯𝗋𝗈𝗀𝗋𝖾𝗌𝗌 𝖡𝖺𝗋』━━➣
┣⪼ 🗃️ 𝖲𝗂𝗓𝖾: {1} | {2}
┣⪼ ⏳️ 𝖣𝗈𝗇𝖾 : {0}%
┣⪼ 🚀 𝖲𝗉𝖾𝖾𝖽: {3}/s
┣⪼ ⏰️ 𝖤𝖳𝖠: {4}
╰━━━━━━━━━━━━━━━➣ </b>"""
