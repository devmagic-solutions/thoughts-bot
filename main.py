import bot
import asyncio
from configparser import ConfigParser


def main():
    parser = ConfigParser()
    parser.read('config.ini')
    bot_token = parser['default']['bot_token']

    print('Starting bot')
    bot.start(bot_token)


main()

