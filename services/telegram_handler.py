from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

from services.database_handler import DatabaseHandler


class TelegramHandler:
    def __init__(self, database_handler):
        self.database_handler: DatabaseHandler = database_handler

    def initialize(self, bot_token):
        application = ApplicationBuilder().token(bot_token).build()

        start_handler = CommandHandler('start', self.__start)
        # add_thought = CommandHandler('add_thought', self.__add_thought)
        # edit_thought = CommandHandler('edit_thought', self.__edit_thought)
        # delete_thought = CommandHandler('delete_thought', self.__delete_thought)

        application.add_handler(start_handler)

        application.run_polling()

    async def __start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        user_id = update.message.chat_id

        user = self.database_handler.get_user(user_id)
        if user is None:
            self.__register_user(user_id)

    def __register_user(self, user_id):
        user = self.database_handler.create_user(user_id)
        return user
