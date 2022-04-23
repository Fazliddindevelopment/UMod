#	████░████░███░███░██░██░████░
#    ░██░░██░░░██░█░██░██░██░███░░
#    ░██░░████░██░░░██░█████░█████
#    ═════════════════════════════════════════
#    ████░████░░██░██░██░███░░██░█████░██░░░██
#    ██░░░███░░░████░░██░██░█░██░██░██░░██░██░
#    ████░█████░██░██░██░██░░███░█████░░░███░░
#    ═════════════════════════════════════════
#    Litsenziya: https://t.me/UModules/112
#    Taqdim qilingan manzil: https://telegram.me/umodules
#    ═════════════════════════════════════════
#    GeekTG yoki FTG oʻrnatish qoʻllanmasi: https://t.me/TGraphUz/1620

from telethon import events
from .. import loader, utils
from asyncio import sleep
from telethon.tl.functions.users import GetFullUserRequest
import random

__version__ = (1, 0, 0)

# meta developer: @netuzb
# meta channel: @umodules

def register(cb):
	cb(HaqiqatMod())
	
class HaqiqatMod(loader.Module):
	"""Haqiqat yoki yolgʻon moduli"""
	
	strings = {
		"name": "Haqiqat",
		"soz_kiriting": "",
		}
		
	async def haqcmd(self, message):
		"""<buyruq> soʻz yoki gap"""
		
		reply = await message.get_reply_message()
		text = utils.get_args_raw(message)
		soz_kiriting = "<b>📖 Iltimos, buyruqdan keyin soʻzni kiriting!</b>"
		haq_natija = ["😑 - YOLGʻON", "😎 - HAQIQAT",]
		haq = [f"{random.choice(haq_natija)}"]
		if not text and not reply:
			await message.edit(soz_kiriting)
		else:
			await message.edit("📖<b> Javob izlanmoqda... 🕒</b>")
			await sleep (0.6)
			await message.edit("📖<b> Javob izlanmoqda... 🕓</b>")
			await sleep (0.6)
			await message.edit("📖<b> Javob izlanmoqda... 🕔</b>")
			await sleep (0.6)
			await message.edit(f"📖<b> - Berilgan mavzu:</b>\n📖 <b>- ''{text}''</b>")
			await sleep (2.0)
			await message.reply(f"📖 <b>- ''{text}'':</b>" + "\n" + f"<b>{random.choice(haq)}</b>")
			return

	async def инфаcmd(self, message):
		"""<команда> текст или слова"""
		
		reply = await message.get_reply_message()
		text = utils.get_args_raw(message)
		soz_kiriting = "<b>📖 Пожалуйста, введите слово после команды!</b>"
		haq_natija = ["😑 - ЛОЖЬ", "😎 - ПРАВДА",]
		haq = [f"{random.choice(haq_natija)}"]
		if not text and not reply:
			await message.edit(soz_kiriting)
		else:
			await message.edit("📖<b> Ответ ищется... 🕒</b>")
			await sleep (0.6)
			await message.edit("📖<b> Ответ ищется... 🕓</b>")
			await sleep (0.6)
			await message.edit("📖<b> Ответ ищется... 🕔</b>")
			await sleep (0.6)
			await message.edit(f"📖<b> - Указанная тема:</b>\n📖 <b>- ''{text}''</b>")
			await sleep (2.0)
			await message.reply(f"📖 <b>- ''{text}'':</b>" + "\n" + f"<b>{random.choice(haq)}</b>")
			return