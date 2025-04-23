import os
from config import Config

class  Script(object):
  START_TXT = """<b>ʜɪ {}
  
ɪ'ᴍ ᴀ ᴀᴅᴠᴀɴᴄᴇᴅ ꜰᴏʀᴡᴀʀᴅ ʙᴏᴛ
ɪ ᴄᴀɴ ꜰᴏʀᴡᴀʀᴅ ᴀʟʟ ᴍᴇssᴀɢᴇ ꜰʀᴏᴍ ᴏɴᴇ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴀɴᴏᴛʜᴇʀ ᴄʜᴀɴɴᴇʟ</b>

**ᴄʟɪᴄᴋ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴋɴᴏᴡ ᴍᴏʀᴇ ᴀʙᴏᴜᴛ ᴍᴇ**"""
  HELP_TXT = """<b><u>🔆 Help</b></u>

<u>**📚 Available commands:**</u>
<b>⏣ __/start - check I'm alive__ 
⏣ __/forward - forward messages__
⏣ __/settings - configure your settings__
⏣ __ /unequify - delete duplicate media messages in chats__
⏣ __ /stop - stop your ongoing tasks__
⏣ __ /reset - reset your settings__</b>

<b><u>💢 Features:</b></u>
<b>► __Forward message from public channel to your channel without admin permission. if the channel is private need admin permission, if you can't give admin permission then use userbot, but in userbot there is a chance to get your account ban so use fake account__
► __custom caption__
► __custom button__
► __skip duplicate messages__
► __filter type of messages__</b>
"""
  
  HOW_USE_TXT = """<b><u>⚠️ Before Forwarding:</b></u>
<b>► __add a bot or userbot__
► __add atleast one to channel__ `(your bot/userbot must be admin in there)`
► __You can add chats or bots by using /settings__
► __if the **From Channel** is private your userbot must be member in there or your bot must need admin permission in there also__
► __Then use /forward to forward messages__"""
  
  ABOUT_TXT = """<b>
╔════❰ ғᴏʀᴡᴀʀᴅ ʙᴏᴛ ❱═❍⊱❁
║╭━━━━━━━━━━━━━━━➣
║┣⪼📃ʙᴏᴛ : ғᴏʀᴡᴀʀᴅ ʙᴏᴛ
║┣⪼📡ʜᴏsᴛᴇᴅ ᴏɴ : ʜᴇʀᴏᴋᴜ
║┣⪼🗣️ʟᴀɴɢᴜᴀɢᴇ : ᴘʏᴛʜᴏɴ3
║┣⪼📚ʟɪʙʀᴀʀʏ : ᴘʏʀᴏɢʀᴀᴍ
║┣⪼🗒️ᴠᴇʀsɪᴏɴ : 1.0.6
║╰━━━━━━━━━━━━━━━➣
╚══════════════════❍⊱❁</b>"""

  STATUS_TXT = """
╔════❰ ʙᴏᴛ sᴛᴀᴛᴜs  ❱═❍⊱❁۪۪
║╭━━━━━━━━━━━━━━━➣
║┣⪼**⏳ ʙᴏᴛ ᴜᴘᴛɪᴍᴇ:**`{}`
║┃
║┣⪼**👱 ᴛᴏᴛᴀʟ ᴜsᴇʀs:** `{}`
║┃
║┣⪼**🤖 ᴛᴏᴛᴀʟ ʙᴏᴛ:** `{}`
║┃
║┣⪼**🔃 ғᴏʀᴡᴀʀᴅɪɴɢs:** `{}`
║┃
║╰━━━━━━━━━━━━━━━➣
╚══════════════════❍⊱❁۪۪
"""
  FROM_MSG = "<b>❪ sᴇᴛ sᴏᴜʀᴄᴇ ᴄʜᴀᴛ (lAST MSG❫\n\nғᴏʀᴡᴀʀᴅ ᴛʜᴇ LAST ᴍᴇssᴀɢᴇ ᴏʀ ʟᴀsᴛ ᴍᴇssᴀɢᴇ ʟɪɴᴋ ᴏғ sᴏᴜʀᴄᴇ ᴄʜᴀᴛ.\n\n/cancel - cᴀɴᴄᴇʟ ᴛʜɪs ᴘʀᴏᴄᴇss</b>"
  
  LAZYFIRST_MSG = "<b>❪ sᴇᴛ sᴏᴜʀᴄᴇ ᴄʜᴀᴛ (fIRST MSG❫\n\nғᴏʀᴡᴀʀᴅ ᴛʜᴇ FIRST ᴍᴇssᴀɢᴇ ᴏʀ ʟᴀsᴛ ᴍᴇssᴀɢᴇ ʟɪɴᴋ ᴏғ sᴏᴜʀᴄᴇ ᴄʜᴀᴛ.\n\n/cancel - cᴀɴᴄᴇʟ ᴛʜɪs ᴘʀᴏᴄᴇss</b>"
  
  TO_MSG = "<b>❪ ᴄʜᴏᴏsᴇ ᴛᴀʀɢᴇᴛ ᴄʜᴀᴛ ❫\n\nᴄʜᴏᴏsᴇ ʏᴏᴜʀ ᴛᴀʀɢᴇᴛ ᴄʜᴀᴛ ғʀᴏᴍ ɢɪᴠᴇɴ ʙᴜᴛᴛᴏɴ.\n\n/cancel - cᴀɴᴄᴇʟ ᴛʜɪs ᴘʀᴏᴄᴇss</b>"
  
  SKIP_MSG = "<b>❪ sᴇᴛ ᴍᴇssᴀɢᴇ sᴋɪᴘᴘɪɴɢ ɴᴏ. ❫</b>\n\n<b>sᴋɪᴘ ᴛʜᴇ ᴍᴇssᴀɢᴇ ᴀs ᴍᴜᴄʜ ᴀs ʏᴏᴜ ᴇɴᴛᴇʀ ᴛʜᴇ ɴᴜᴍʙᴇʀ ᴀɴᴅ ᴛʜᴇ ʀᴇsᴛ oғ ᴛʜᴇ ᴍᴇssᴀɢᴇs ᴡɪʟʟ ʙᴇ ғᴏʀᴡᴀʀᴅᴇᴅ.\nᴅᴇғᴀᴜʟᴛ sᴋɪᴘ ɴᴜᴍʙᴇʀ=</b> <code>0</code>\n<code>ᴇx: ʏᴏᴜ ᴇɴᴛᴇʀ 0 = 0 ᴍᴇssᴀɢᴇ ᴡɪʟʟ sᴋɪᴘ.\nʏᴏᴜ ᴇɴᴛᴇʀ 5 = 5 ᴍᴇssᴀɢᴇs ᴡɪʟʟ sᴋɪᴘ.</code>\n/cancel <b>- cᴀɴᴄᴇʟ ᴛʜɪs ᴘʀᴏᴄᴇss</b>"
  
  CANCEL = "<b>ᴘʀᴏᴄᴇss ᴄᴀɴᴄᴇʟᴇᴅ sᴜᴄᴄᴇғᴜʟʟʏ./b>"
  
  BOT_DETAILS = "<b><u>📄 ʙᴏᴛ ᴅᴇᴛᴀɪʟs</b></u>\n\n<b>➣ ɴᴀᴍᴇ:</b> <code>{}</code>\n<b>➣ ʙᴏᴛ ɪᴅ:</b> <code>{}</code>\n<b>➣ ᴜsᴇʀɴᴀᴍᴇ:</b> @{}"
  
  USER_DETAILS = "<b><u>📄 ᴜsᴇʀʙᴏᴛ ᴅᴇᴛᴀɪʟs</b></u>\n\n<b>➣ ɴᴀᴍᴇ:</b> <code>{}</code>\n<b>➣ ᴜsᴇʀ ɪᴅ:</b> <code>{}</code>\n<b>➣ ᴜsᴇʀɴᴀᴍᴇ:</b> @{}"  
         
  TEXT = """
╔════❰ ғᴏʀᴡᴀʀᴅ sᴛᴀᴛᴜs  ❱═❍⊱❁۪۪
║╭━━━━━━━━━━━━━━━➣
║┣⪼<b>🕵 ғᴇᴄʜᴇᴅ Msɢ :</b> <code>{}</code>
║┃
║┣⪼<b>✅ sᴜᴄᴄᴇғᴜʟʟʏ Fᴡᴅ :</b> <code>{}</code>
║┃
║┣⪼<b>👥 ᴅᴜᴘʟɪᴄᴀᴛᴇ Msɢ :</b> <code>{}</code>
║┃
║┣⪼<b>🗑 ᴅᴇʟᴇᴛᴇᴅ Msɢ :</b> <code>{}</code>
║┃
║┣⪼<b>🔁 Fɪʟᴛᴇʀᴇᴅ Msɢ :</b> <code>{}</code>
║┃
║┣⪼<b>📊 Cᴜʀʀᴇɴᴛ Sᴛᴀᴛᴜs:</b> <code>{}</code>
║╰━━━━━━━━━━━━━━━➣ 
╚════❰ {} ❱══❍⊱❁۪۪
"""
  DUPLICATE_TEXT = """
╔════❰ ᴜɴᴇǫᴜɪғʏ sᴛᴀᴛᴜs ❱═❍⊱❁۪۪
║╭━━━━━━━━━━━━━━━➣
║┣⪼ <b>ғᴇᴛᴄʜᴇᴅ ғɪʟᴇs:</b> <code>{}</code>
║┃
║┣⪼ <b>ᴅᴜᴘʟɪᴄᴀᴛᴇ ᴅᴇʟᴇᴛᴇᴅ:</b> <code>{}</code> 
║╰━━━━━━━━━━━━━━━➣
╚════❰ {} ❱══❍⊱❁۪۪
"""
  DOUBLE_CHECK = """<b><u>ᴅᴏᴜʙʟᴇ ᴄʜᴇᴄᴋɪɴɢ 📋</b></u>

<b>ʙᴇꜰᴏʀᴇ ꜰᴏʀᴡᴀʀᴅɪɴɢ ᴛʜᴇ ᴍᴇssᴀɢᴇs ᴄʟɪᴄᴋ ᴛʜᴇ ʏᴇs ʙᴜᴛᴛᴏɴ ᴏɴʟʏ ᴀꜰᴛᴇʀ ᴄʜᴇᴄᴋɪɴɢ ᴛʜᴇ ꜰᴏʟʟᴏᴡɪɴɢ</b>


<b>★ ʏᴏᴜʀ ʙᴏᴛ: [{botname}](t.me/{botuname})</b>
<b>★ sᴏᴜʀᴄᴇ ᴄʜᴀᴛ: {from_chat}</b>
<b>★ ᴛᴀʀɢᴇᴛ ᴄʜᴀᴛ: {to_chat}</b>
<b>★ sᴋɪᴘ ᴍᴇssᴀɢᴇs: {skip}</b>

<i><b>° {botname} ᴍᴜsᴛ ʙᴇ ᴀᴅᴍɪɴ ɪɴ ᴛᴀʀɢᴇᴛ ᴄʜᴀᴛ</i> ({to_chat})</b>
<i><b>° ɪꜰ ᴛʜᴇ sᴏᴜʀᴄᴇ ᴄʜᴀᴛ ɪs ᴘʀɪᴠᴀᴛᴇ ʏᴏᴜʀ ᴜsᴇʀʙᴏᴛ ᴍᴜsᴛ ʙᴇ ᴍᴇᴍʙᴇʀ ᴏʀ ʏᴏᴜʀ ʙᴏᴛ ᴍᴜsᴛ ʙᴇ ᴀᴅᴍɪɴ ɪɴ ᴛʜᴇʀᴇ ᴀʟsᴏ</b></i>

<b>ɪꜰ ᴛʜᴇ ᴀʙᴏᴠᴇ ɪs ᴄʜᴇᴄᴋᴇᴅ ᴛʜᴇɴ ᴛʜᴇ ʏᴇs ʙᴜᴛᴛᴏɴ ᴄᴀɴ ʙᴇ ᴄʟɪᴄᴋᴇᴅ</b>"""
  
  SETTINGS_TXT = """<b>ᴄʜᴀɴɢᴇ ʏᴏᴜʀ sᴇᴛᴛɪɴɢs ᴀs ʏᴏᴜʀ ᴡɪsʜ.</b>"""

  DONATE_TXT = """⛱"""