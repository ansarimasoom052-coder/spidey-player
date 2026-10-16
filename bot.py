
import os
import re
import logging
from urllib.parse import urlparse

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

logging.basicConfig(level=logging.INFO)

TOKEN = os.environ.get("BOT_TOKEN", "")

SUPPORTED_DOMAINS = {
    "terabox.com",
    "teraboxapp.com",
    "1024tera.com",
    "1024terabox.com",
    "terasharefile.com",
    "tersharefile.com",
    "terasharelink.com",
    "teraboxlink.com",
    "terafileshare.com",
}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🕷️ SPIDEY ✘ PLAYER\n\n"
        "TeraBox video link bhejo!"
    )


async def handle_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message
    text = message.text or ""
    match = re.search(r"https?://\S+", text)

    if not match:
        await message.reply_text("❌ Valid link bhejo.")
        return

    link = match.group(0).rstrip(".,)")

    try:
        host = (urlparse(link).hostname or "").lower()
        if host.startswith("www."):
            host = host[4:]
    except ValueError:
        host = ""

    if host not in SUPPORTED_DOMAINS:
        await message.reply_text("⚠️ Supported TeraBox link bhejo.")
        return

    await message.reply_text(
        "✅ TeraBox link mil gaya!\n"
        "⏳ Video extractor abhi connect karna baaki hai."
    )


def main():
    if not TOKEN:
        raise RuntimeError("BOT_TOKEN environment variable missing")

    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_link)
    )
    app.run_polling()


if __name__ == "__main__":
    main()
        
