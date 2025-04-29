from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# IPL winners dictionary
winners = {
    "2008": "Rajasthan Royals",
    "2009": "Deccan Chargers",
    "2010": "Chennai Super Kings",
    "2011": "Chennai Super Kings",
    "2012": "Kolkata Knight Riders",
    "2013": "Mumbai Indians",
    "2014": "Kolkata Knight Riders",
    "2015": "Mumbai Indians",
    "2016": "Sunrisers Hyderabad",
    "2017": "Mumbai Indians",
    "2018": "Chennai Super Kings",
    "2019": "Mumbai Indians",
    "2020": "Mumbai Indians",
    "2021": "Chennai Super Kings",
    "2022": "Gujarat Titans",
    "2023": "Chennai Super Kings",
    "2024": "Kolkata Knight Riders"
}

# Respond to messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    year = update.message.text.strip()
    winner = winners.get(year)
    if winner:
        await update.message.reply_text(f"The IPL winner in {year} was {winner}.")
    else:
        await update.message.reply_text("Sorry, I don't have data for that year.")

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi! Send me an IPL year (e.g. 2020) and I'll tell you the winner.")
    

# Main function
def main():
    app = ApplicationBuilder().token("7851212791:AAGYlB1oqN-gx6xePSaqRJPaQOOCBtHtQCs").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
