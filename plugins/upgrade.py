"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**User ID : {message.from_user.id}\nName : {message.from_user.mention}\n\n💠 Free \n\n✓ Upload 2GB Files\n✓ Daily Upload 5GB\n✓ Parallel process : 2\n✓ Timeout : NO\n✓ Validity : Lifetime\n\nFor Buy Premium Plans Checkout Our Plan!**"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("Chek Premium Plans",url = "https://telegra.ph/BUY-PREMIUM-PLAN-01-21-2")], 
        			[InlineKeyboardButton("Movies Channel",url = "https://t.me/wombackup"),
        			InlineKeyboardButton("Support",url = "https://t.me/royaldwip")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["buy"]))
async def upgradecm(bot,message):
	text = """**User ID : {message.from_user.id}\nName : {message.from_user.mention}\n\n💠 Free \n\n✓ Upload 2GB Files\n✓ Daily Upload 5GB\n✓ Parallel process : 2\n✓ Timeout : NO\n✓ Validity : Lifetime\n\nFor Buy Premium Plans Checkout Our Plan!**"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("Chek Premium Plans",url = "https://telegra.ph/BUY-PREMIUM-PLAN-01-21-2")], 
        			[InlineKeyboardButton("Updates Channel",url = "https://t.me/wombackup"),
        			InlineKeyboardButton("Support",url = "https://t.me/royaldwip")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await message.reply_text(text = text,reply_markup = keybord)
