#
# Copyright (C) 2016 Kamran Mackey and contributors
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

from telegram import ChatAction

def me(_, update, args):
    args = ' '.join(args)
    user = update.message.from_user.first_name
    update.message.chat.send_action(action=ChatAction.TYPING)
    update.message.reply_text(parse_mode='Markdown',
                              text='*{0}* {1}'.format(user, args))
