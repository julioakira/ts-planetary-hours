import logging
from metadata import Metadata
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

# Sends out a greeting when the start command is dispatched
def start(update, context):
  update.message.reply_text('Hello!')

# Echoes the user's message
def echo(update, context):
  update.message.reply_text(update.message.text)

# Logs errors caused by updates
def error(update, context):
  logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
  # Loads Environment
  metadata = Metadata.load_environment()
   # Bot updater with BotFather token
  updater = Updater(metadata.token, use_context=True)
  # Dispatcher to register handlers
  dp = updater.dispatcher
  ## Command Handlers
  dp.add_handler(CommandHandler("start", start))
  # Echoes noncommand messages back to the user
  dp.add_handler(MessageHandler(Filters.text, echo))
  # Logs errors
  dp.add_error_handler(error)
  # Starts bot
  updater.start_polling()
  updater.idle()


if __name__ == '__main__':
    main()