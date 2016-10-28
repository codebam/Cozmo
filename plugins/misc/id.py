#
# Copyright (C) 2016 Kamran Mackey and contributors
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

from telegram import ChatAction, ParseMode


def id_plugin(_, update):
    """
    Simple plugin used for retrieving a user's ID by doing
    the /id command.
    """
    name = update.message.from_user.first_name
    uid = update.message.from_user.id

    update.message.chat.send_action(action=ChatAction.TYPING)
    update.message.reply_text(parse_mode=ParseMode.MARKDOWN,
                              quote=True,
                              text="You are *{0}* with ID `{1}`.".format(name,
                                                                         uid))
