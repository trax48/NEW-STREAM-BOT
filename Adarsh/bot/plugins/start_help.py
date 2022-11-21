

from pyrogram import filters, emoji
from Adarsh.bot import StreamBot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

@StreamBot.on_message(filters.command(['start']))
async def start(_, m: Message):
    await m.reply(f'Hi {m.from_user.mention(style="md")}, Send me a file to get Download stream link.',
                
                  )

@StreamBot.on_message(filters.command(['help']))
async def help(_, m: Message):
    await m.reply(f'i can convert any file into Download Link or Online Streaming Link! \n2GB+ files Supported ✅ \n18+ Content Not Allowed ⚠️ \nLinks are Permanent 🍀.
                  ',
                 
                  )
    
@StreamBot.on_message(filters.command(['about']))
async def about(_, m: Message):
    await m.reply(f'✯ 𝙼𝚈 𝙽𝙰𝙼𝙴: Flash \n✯ 𝙲𝚁𝙴𝙰𝚃𝙾𝚁: href=https://t.me/Nexus_Shubhu>Shubham</a>',
                  
                  )
