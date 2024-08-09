from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext
from dateutil.relativedelta import relativedelta
from datetime import datetime

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
TOKEN = 'YOUR_BOT_TOKEN'

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Hi! Send me a date in the format /calculate YYYY-MM-DD and I will tell you how much time has passed since then.')

async def calculate(update: Update, context: CallbackContext) -> None:
    try:
        input_date = datetime.strptime(context.args[0], '%Y-%m-%d')
        current_date = datetime.now()
        difference = relativedelta(current_date, input_date)
        
        years = difference.years
        months = difference.months
        days = difference.days
        total_months = years * 12 + months
        total_days = (current_date - input_date).days
        
        await update.message.reply_text(
            f'''
            {years} years, {months} months, and {days} days have passed since {input_date.date()}.
            \nTotal of months: {total_months}
            \nTotal of days: {total_days}
            '''
        )
    except (IndexError, ValueError):
        await update.message.reply_text('Please provide a valid date in the format YYYY-MM-DD.')

def main() -> None:
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('calculate', calculate))

    application.run_polling()

if __name__ == '__main__':
    main()
