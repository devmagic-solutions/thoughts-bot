from services.database_handler import DatabaseHandler
from services.telegram_handler import TelegramHandler


def start(bot_token):
    database_handler = DatabaseHandler()
    database_handler.initialize()

    telegram_handler = TelegramHandler(database_handler)
    telegram_handler.initialize(bot_token)
