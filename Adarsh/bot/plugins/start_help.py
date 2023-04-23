

from pyrogram import filters, emoji
from Adarsh.bot import StreamBot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

@StreamBot.on_message(filters.command(['start']))
async def start(_, m: Message):
    await m.reply(f'Hi {m.from_user.mention(style="md")}, Send me a file to get Download stream link. \n\nIf You Want Help Press /help',
                
                  )

@StreamBot.on_message(filters.command(['help']))
async def help(_, m: Message):
    await StreamBot.send_photo(
                chat_id=message.chat.id,
                photo="https://telegra.ph/file/bb0d2a42531afe19f41d4.jpg",
                Caption=" I can convert any file into Download Link or Online Streaming Link! \n2GB+ files Supported ✅ \n18+ Content Not Allowed ⚠️ \nLinks are Permanent 🍀 \n\nFor More Help Press /players",
    reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('Any Queries DM Here ✅', url='https://t.me/syrus_143_hpy')]])
                  
                  )
    
@StreamBot.on_message(filters.command(['about']))
async def about(_, m: Message):
    await m.reply(f'✯ ᴍʏ ɴᴀᴍᴇ: Sandman \n✯ ᴍʏ ᴄʀᴇᴀᴛᴏʀ: Sandy \n✯ ᴘᴏᴡᴇʀᴇᴅ ʙʏ: [FM](https://t.me/filmy_men) \n✯ ʟɪʙʀᴀʀʏ: Pyrogram \n✯ ʟᴀɴɢᴜᴀɢᴇ: Python \n✯ ᴅᴀᴛᴀʙᴀꜱᴇ: Free \n✯ ʙᴏᴛ ꜱᴇʀᴠᴇʀ: Koyeb',
    reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('My Owner 😎', url='https://t.me/syrus_143_hpy')]])
                  
                  )

@StreamBot.on_message(filters.command(['players']))
async def players(_, m: Message):
    await m.reply(f'Dear Users, \n\nTo Streaming Your File in Players Open Links Through 1st Botton (ꜱᴛʀᴇᴀᴍ ɪɴ ᴘʟᴀʏᴇʀꜱ ⚡️) \nOpen in Chrome. \n\nMake Sure You have Good Internet Speed For Streaming On Players')
