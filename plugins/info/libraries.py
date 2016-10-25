#
# Copyright (C) 2016 Kamran Mackey and contributors
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see [http://www.gnu.org/licenses/].

from telegram import __version__ as tgver
from requests import __version__ as reqsver


def libraries(bot, update):
    """
    Plugin for sending a message containing
    the libraries the bot uses.
    """
    get_me = bot.getMe().first_name
    update.message.reply_text(parse_mode='Markdown',
                              text="*{}* runs on a number of libraries. Without these, it "
                                   "would not be where it is today. Libraries and the "
                                   "versions we use are listed below.\n\n"
                                   "*python-telegram-bot*: {}\n"
                                   "*requests*: {} ".format(get_me,
                                                            tgver,
                                                            reqsver))
