import logging
import json
from metadata import Metadata
from utils import get_planetary_hour, parse_day
from telegram.ext import (
  Updater,
  CommandHandler,
  MessageHandler,
  Filters,
  CallbackContext
)

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

metadata = Metadata.load_environment()

# Sends out a greeting when the start command is dispatched
def start(update, context):
  update.message.reply_text('Hello!')

def important(update, context):
  update.message.reply_text('O importante é comer paçoca')

def request_planetary_data(update, context):
  # Loads env data
  response = get_planetary_hour(metadata.api_url, metadata.date, metadata.location)
  update.message.reply_text(json.dumps(response, sort_keys=True, indent=2))

def get_day_info(update, context):
  response = get_planetary_hour(metadata.api_url, metadata.date, metadata.location)
  update.message.reply_text(parse_day(response))

# Echoes the user's message
def echo(update, context):
  update.message.reply_text(update.message.text)

# Logs errors caused by updates
def error(update, context):
  logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
   # Bot updater with BotFather token
  updater = Updater(metadata.token, use_context=True)
  # Dispatcher to register handlers
  dp = updater.dispatcher
  ## Command Handlers
  dp.add_handler(CommandHandler("start", start))
  dp.add_handler(CommandHandler("importante", important))
  dp.add_handler(CommandHandler("raw_hours", request_planetary_data))
  dp.add_handler(CommandHandler("day", get_day_info))
  # Echoes noncommand messages back to the user
  dp.add_handler(MessageHandler(Filters.text, echo))
  # Logs errors
  dp.add_error_handler(error)
  # Starts bot
  updater.start_polling()
  updater.idle()


if __name__ == '__main__':
    main()
