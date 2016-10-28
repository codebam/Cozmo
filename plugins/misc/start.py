#
# Copyright (C) 2016 Kamran Mackey and contributors
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

from telegram import ChatAction, ParseMode


def start(bot, update):
    """
    Create a basic start command. Nothing fancy
    here folks.
    """
    update.message.chat.send_action(action=ChatAction.TYPING)
    update.message.reply_text(parse_mode=ParseMode.MARKDOWN,
                              text="Hi, I'm *{0}*! Please enter /about to view information about me.".format(
                                  bot.getMe().first_name))
