import os
import re
import logging
from telegram import Update
from telegram.ext import Application, MessageHandler, CommandHandler, ContextTypes, filters

logging.basicConfig(level=logging.INFO)

TOKEN = os.environ.get("BOT_TOKEN", "")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
await update.message.reply_text(
"🕷️ SPIDEY ✘ PLAYER\n\n"
"TeraBox video link bhejo!"
)

async def handle_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
message = update.message
text = message.text or ""

match = re.search(r'https?://\S+', text)

if not match:
    await message.reply_text("❌ Valid link bhejo.")
    return

link = match.group(0).rstrip(".,)")
if "terabox" not in link.lower() and "terashare" not in link.lower():
    await message.reply_text("⚠️ TeraBox link bhejo.")
    return

await message.reply_text(
    "✅ TeraBox link mil gaya!\n\n"
    "Direct playable link feature abhi setup nahi hua.\n"
    "Original link:\n" + link
)

def main():
if not TOKEN:
raise RuntimeError("BOT_TOKEN environment variable missing")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_link))
app.run_polling()

if name == "main":
main()
