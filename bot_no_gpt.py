import asyncio

from pyrogram import Client, filters, types, enums
from pyrogram.errors.exceptions.not_acceptable_406 import ChannelPrivate
from pyrogram.errors.exceptions.bad_request_400 import UserBannedInChannel
from pyrogram.errors.exceptions.forbidden_403 import Forbidden
from pyrogram.types import Chat

API_ID = 19309010
API_HASH = "dfdf154157cca400bd53b00100468fa5"

NAME = input("Напиши название сессии: ")
TIME_ = float(input("Задержка(должна быть > 0): "))

app = Client(NAME, api_id=API_ID, api_hash=API_HASH, parse_mode=enums.parse_mode.ParseMode.HTML)


@app.on_message(filters.channel)
async def getpost(client, message: types.Message):
    await asyncio.sleep(TIME_)
    chat_id = message.chat.id
    message_id = message.id
    try:
        msg = await app.get_discussion_message(chat_id, message_id)
        await msg.reply(text="🔥", quote=True)
        print(f"Ответил на пост: {message.text}")
    except ChannelPrivate:
        try:
            await app.leave_chat(chat_id)
        except:
            pass
        await app.send_message('@spambot', '/start')
        await asyncio.sleep(3)
        await app.send_message('@spambot', 'OK')
        await asyncio.sleep(3)
        await app.send_message('@spambot', '/start')

    except UserBannedInChannel:
        try:
            await app.leave_chat(chat_id)
        except:
            pass

        await app.send_message('@spambot', '/start')
        await asyncio.sleep(3)
        await app.send_message('@spambot', 'OK')
        await asyncio.sleep(3)
        await app.send_message('@spambot', '/start')

    except Forbidden:
        chat: Chat
        try:
            chat = await app.get_chat(chat_id)
            await chat.linked_chat.join()
        except Exception as e:
            print('Не удалось вступить в чат', e)
    except Exception as e:
        print('Ошибка', e)

app.run()
