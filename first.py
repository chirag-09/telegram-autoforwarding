from telethon import events
from telethon import TelegramClient

# Remember to use your own values from my.telegram.org!
f = open("api_id.txt", "r")
api_id = f.read()
f = open("api_hash.txt", "r")
api_hash = f.read()


client= TelegramClient('anon', api_id, api_hash)


@client.on(events.NewMessage)
async def handler(event):
    chat_id=event.chat_id
    msg=event.raw_text
    print(chat_id)

    if chat_id==-1001370241291 or chat_id==-1001174144067:
        if("Loot" in msg or "Gold" in msg or "gold" in msg):
             await client.send_message(1173123426, msg)
         

client.start()
client.run_until_disconnected()