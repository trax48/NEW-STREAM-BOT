

from pyrogram import filters, emoji
from Adarsh.bot import StreamBot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

@StreamBot.on_message(filters.command(['start']))
async def start(_, m: Message):
    await StreamBot.send_photo(
                chat_id=m.chat.id,
                photo="https://telegra.ph/file/94c74580a918cb9e6b18e.jpg",
                caption="""
                 ʜᴇʟʟᴏ {} 🥀
ɪ ᴀᴍ ᴛᴇʟᴇɢʀᴀᴍ ғɪʟᴇ ᴛᴏ ʟɪɴᴋ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ ᴡɪᴛʜ ᴄʜᴀɴɴᴇʟ sᴜᴘᴘᴏʀᴛ.
sᴇɴᴅ ᴍᴇ ᴀɴʏ ғɪʟᴇ ᴀɴᴅ ɢᴇᴛ ᴀ ᴅɪʀᴇᴄᴛ ғᴀsᴛ ᴅᴏᴡɴʟᴏᴀᴅ & sᴛʀᴇᴀᴍ ʟɪɴᴋ ʙᴇᴛᴛᴇʀ ᴛʜᴇɴ ᴏᴛʜᴇʀs ʙᴏᴛs.!
\n\nsᴇɴᴅ ᴍᴇ ᴀ ғɪʟᴇ ᴏʀ ʏᴏᴜ ᴄᴀɴ ᴊᴜsᴛ ᴀᴅᴅ ᴍᴇ ᴀɴʏ ᴛᴇʟᴇɢʀᴀᴍ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴜsᴇ ᴍᴇ 🥰
\n\n©️ ᴘᴏᴡᴇʀᴇᴅ ʙʏ :- @Filmy_Men""",
                
                  )


@StreamBot.on_message(filters.command(['help']))
async def help(_, m: Message):
    await m.reply(f'i can convert any file into Download Link or Online Streaming Link! \n2GB+ files Supported ✅ \n18+ Content Not Allowed ⚠️ \nLinks are Permanent 🍀 \n\nFor More Help Press /players',
    reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('Any Queries DM Here ✅', url='https://t.me/syrus_143_hpy')]])
                  
                  )
    
    
@StreamBot.on_message(filters.command(['link']))
async def link(_, m: Message):
    await m.reply_text(
            text=msg_text.format(get_name(log_msg), humanbytes(get_media_file_size(m)), online_link, stream_link, stream_link2),
            quote=True,
            disable_web_page_preview=True,
    reply_markup=InlineKeyboardMarkup(
              [
                    [InlineKeyboardButton("🖥 ꜱᴛʀᴇᴀᴍ ɪɴ ᴘʟᴀʏᴇʀꜱ 🖥", url=stream_link)], #Stream Link
                    [InlineKeyboardButton('📩 ᴅᴏᴡɴʟᴏᴀᴅ 📩', url=online_link), #Download Link
                    InlineKeyboardButton("📺 ꜱᴛʀᴇᴀᴍ 📺", url=stream_link2)]]), #Stream Link 2

              )
    
@StreamBot.on_message(filters.command(['mybio']))
async def about(_, m: Message):
    await m.reply("""<b>✯ Mʏ Nᴀᴍᴇ : {}</b>
✯ ʟᴏᴠᴇ: <a href=https://t.me/Syrus_143_hpy>ᴋs</a>
✯ ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ: <a href=https://t.me/Filmy_men>ғɪʟᴍʏ ᴍᴇɴ</a>
✯ ᴍʏ ʜᴜsʙᴀɴᴅ: <a href=https://t.me/Syrus_143_hpy>亗 𝗧𝗛𝗘 𝗦𝗔𝗡ᕲ𝗠𝗔𝗡</a>
✯ ʟɪʙʀᴀʀʏ: ᴘʏʀᴏɢʀᴀᴍ
✯ ʟᴀɴɢᴜᴀɢᴇ: ᴘʏᴛʜᴏɴ 𝟹
✯ ᴅᴀᴛᴀʙᴀsᴇ: ᴍᴏɴɢᴏᴅʙ
✯ sᴇʀᴠᴇʀ: ᴘʀᴠᴛ
✯ ʙᴜɪʟᴅ sᴛᴀᴛᴜs: v2.0.1 [ ʙᴇᴛᴀ ]</b>"""
    reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('My Owner 😎', url='https://t.me/syrus_143_hpy')]])
                  
                  )

@StreamBot.on_message(filters.command(['players']))
async def players(_, m: Message):
    await m.reply(f'Dear Users, \n\nTo Streaming Your File in Players Open Links Through 1st Botton (ꜱᴛʀᴇᴀᴍ ɪɴ ᴘʟᴀʏᴇʀꜱ ⚡️) \nOpen in Chrome. \n\nMake Sure You have Good Internet Speed For Streaming On Players')
