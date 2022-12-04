

from pyrogram import filters, emoji
from Adarsh.bot import StreamBot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

@StreamBot.on_message(filters.command(['start']))
async def start(_, m: Message):
    await m.reply(f'Hi {m.from_user.mention(style="md")}, Send me a file to get Download stream link.',
                
                  )

@StreamBot.on_message(filters.command(['help']))
async def help(_, m: Message):
    await m.reply(f'i can convert any file into Download Link or Online Streaming Link! \n2GB+ files Supported ✅ \n18+ Content Not Allowed ⚠️ \nLinks are Permanent 🍀',

                  )
    
@StreamBot.on_message(filters.command(['about']))
async def about(_, m: Message):
    await m.reply(f'✯ 𝙼𝚈 𝙽𝙰𝙼𝙴: Flash \n✯ 𝙼𝚈 𝙲𝚁𝙴𝙰𝚃𝙾𝚁: Shubham \n✯ 𝙿𝙾𝚆𝙴𝚁𝙴𝙳 𝙱𝚈: [Moviesss4ers](https://t.me/Moviesss4ers) \n✯ 𝙻𝙸𝙱𝚁𝙰𝚁𝚈: 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼 \n✯ 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴: Python \n✯ 𝙳𝙰𝚃𝙰𝙱𝙰𝚂𝙴: Free \n✯ 𝙱𝙾𝚃 𝚂𝙴𝚁𝚅𝙴𝚁: Koyeb',
    reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('My Owner 😎', url='https://t.me/Link_Reporter_Bot')]])
                  
                  )

@StreamBot.on_message(filters.command(['players']))
async def players(_, m: Message):
    await m.reply(f'Dear Users, \n\nTo Streaming Your File in Players Open Links Through 1st Botton (ꜱᴛʀᴇᴀᴍ ɪɴ ᴘʟᴀʏᴇʀꜱ ⚡️) \nOpen in Chrome. \n\nMake Sure You Have Good Internet Speed For Streaming On Players’)
