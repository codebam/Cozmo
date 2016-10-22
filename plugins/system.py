#
# Copyright (C) 2016 Kamran Mackey
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
import platform

from telegram import ParseMode

import EddieBot


def about(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id,
                    parse_mode=ParseMode.MARKDOWN,
                    disable_web_page_preview=True,
                    text="This bot is powered by *EddieBot* {}, the plugin-based bot written in Python 3.\n\n"
                         "*Source Code*: https://github.com/KamranMackey/EddieBot".format(EddieBot.__version__))


def system(bot, update):
    # Get general system info
    sys_os = (platform.system())
    sys_version = ''.join(platform.version())
    python_implementation = platform.python_implementation()
    python_version = platform.python_version()
    sys_architecture = platform.machine()

    bot.sendMessage(chat_id=update.message.chat_id,
                    parse_mode=ParseMode.MARKDOWN,
                    text="*Basic Info*:\n\n"
                         "*OS*: {} {}\n"
                         "*Python*: {} {}\n"
                         "*Architecture*: {}".format(sys_os,
                                                     sys_version,
                                                     python_implementation,
                                                     python_version,
                                                     sys_architecture))
