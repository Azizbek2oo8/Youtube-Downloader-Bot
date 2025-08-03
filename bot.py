from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from pytube import YouTube

TOKEN = "8296126447:AAEuXrqw6A0SFl4qBPfK4E5QPlqKzXBeKjs"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("YouTube havolasini yuboring — men yuklab beraman.")

async def download_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text
    try:
        yt = YouTube(url)
        stream = yt.streams.get_lowest_resolution()
        video_path = stream.download()
        await update.message.reply_video(video=open(video_path, "rb"))
    except Exception as e:
        await update.message.reply_text("Xatolik: " + str(e))

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, download_video))
print("Bot ishlayapti...")
app.run_polling()
