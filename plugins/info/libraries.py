#
# Copyright (C) 2016 Kamran Mackey and contributors
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

from requests import __version__ as reqsver
from telegram import (__version__ as tgver, ChatAction,
                      ParseMode)


def libraries(bot, update):
    """
    Plugin for sending a message containing
    the libraries the bot uses.
    """
    get_me = bot.getMe().first_name
    update.message.chat.send_action(action=ChatAction.TYPING)
    update.message.reply_text(parse_mode=ParseMode.MARKDOWN,
                              text="*{}* runs on a number of libraries. The names and "
                                   "versions of the libraries we use are listed below.\n\n"
                                   "*python-telegram-bot*: {}\n"
                                   "*requests*: {} ".format(get_me,
                                                            tgver,
                                                            reqsver))
