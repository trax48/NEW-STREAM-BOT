

from pyrogram import filters, emoji
from Adarsh.bot import StreamBot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

@StreamBot.on_message(filters.command(['start']))
async def start(_, m: Message):
    await m.reply(f'Hi {m.from_user.mention(style="md")}, Send me a file to get Download stream link.',
                
                  )

@StreamBot.on_message(filters.command(['help']))
async def help(_, m: Message):
    await m.reply(f'i can convert any file into Download or Streaming link, even more then 2GB files 😉. \n18+ Content Not Allowed So please Avoid it ⚠️. \nLinks are Permanent 🤗.',
                  )
    
