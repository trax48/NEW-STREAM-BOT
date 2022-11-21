

from pyrogram import filters, emoji
from Adarsh.bot import StreamBot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

@StreamBot.on_message(filters.command(['start']))
async def start(_, m: Message):
    await m.reply(f'Hi {m.from_user.mention(style="md")}, Send me a file to get Download stream link.',
                
                  )

@StreamBot.on_message(filters.command(['help']))
async def help(_, m: Message):
    await m.reply(f'i can convert any file into Download or Streaming link, even more then 2GB files 😉. \n18+ Content Not Allowed ⚠️. \nLinks are Permanent 🤗.',
                  )
    
@StreamBot.on_message(filters.command(['about']))
async def about(f'✯ 𝙼𝚈 𝙽𝙰𝙼𝙴: {} \n✯ 𝙲𝚁𝙴𝙰𝚃𝙾𝚁: <a href=https://t.me/Nexus_Shubhu>Shubham</a> \n✯ 𝙻𝙸𝙱𝚁𝙰𝚁𝚈: 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼 \n✯ 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴: 𝙿𝚈𝚃𝙷𝙾𝙽 𝟹 \n✯ 𝙳𝙰𝚃𝙰𝙱𝙰𝚂𝙴: 𝙳𝙴𝙳𝙸𝙲𝙰𝚃𝙴𝙳 \n✯ 𝙱𝙾𝚃 𝚂𝙴𝚁𝚅𝙴𝚁: 𝚅𝙿𝚂 \n✯ 𝙱𝚄𝙸𝙻𝙳 𝚂𝚃𝙰𝚃𝚄𝚂: 𝚂𝚄𝙲𝙲𝙴𝚂𝚂',
                  )
