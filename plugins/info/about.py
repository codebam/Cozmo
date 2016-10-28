#
# Copyright (C) 2016 Kamran Mackey and contributors
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

from init import __version__ as botver

from telegram import ChatAction, ParseMode


def about(bot, update):
    """
    Sends a message giving info about the bot and linking
    to the bot's source code on GitHub.
    """
    get_me = bot.getMe().first_name
    update.message.chat.send_action(action=ChatAction.TYPING)
    update.message.reply_text(parse_mode=ParseMode.MARKDOWN,
                              disable_web_page_preview=True,
                              text="*{0}* is powered by *Cozmo* {1}, the plugin-based bot built primarily by "
                                   "@l3thal. It is written in the Python programming language. You can "
                                   "view which libraries we use by doing /libraries.\n\n"
                                   "*Source Code*: [GitHub](https://github.com/KamranMackey/Cozmo)".format(get_me,
                                                                                                           botver))
