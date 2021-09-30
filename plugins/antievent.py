from userge import userge, Message, filters
import asyncio
import pyrogram
from pyrogram import Client, filters
from pyrogram.types import Message

# add command handler
@userge.on_cmd("delevent", about={
 'header': "to delete service messages",
'usage': "{tr}delevent"})
async def del_event(message: message):
  await c.send_message(text= "anti servive mode started",del_in=5)
  
#plugin code

@pyrogram.Client.on_message(pyrogram.Filters.service)
async def service(c: Client, m: Message):
    await c.delete_messages(chat_id=m.chat.id, message_ids=m.message_id)
   
 