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

from init import __version__ as botver


def about(bot, update):
    """
    Sends a message giving info about the bot and linking
    to the bot's source code on GitHub.
    """
    get_me = bot.getMe().first_name
    update.message.reply_text(parse_mode='Markdown',
                              disable_web_page_preview=True,
                              text="*{0}* is powered by *EddieBot* {1}, the plugin-based bot built by @l3thal"
                                   " and @xenial. It is written in the Python programming language."
                                   "\n\n*python-telegram-bot version*: {2}\n"
                                   "*Source Code*: [GitHub](https://github.com/KamranMackey/EddieBot)".format(get_me,
                                                                                                              botver,
                                                                                                              tgver))
