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

import platform
from datetime import timedelta
import sys
from os import getpid
from time import time

from psutil import Process
from telegram import __version__ as tgver

from __init__ import __version__ as botver
from utils.size import size as format_bytes


def about(bot, update):
    """
    Sends a message giving info about the bot and linking
    to the bot's source code on GitHub.
    """
    get_me = bot.getMe().first_name
    bot.sendMessage(chat_id=update.message.chat_id,
                    parse_mode='Markdown',
                    disable_web_page_preview=True,
                    text="*{}* is powered by *EddieBot* {}, the plugin-based bot written in Python 3, and "
                         "is currently running on version {} of the python-telegram-bot library.\n\n"
                         "*Source Code*: https://github.com/KamranMackey/EddieBot".format(get_me,
                                                                                          botver,
                                                                                          tgver))


def system(bot, update):
    """
    Sends a message containing information about the system
    running the bot and the bot's process itself.

    Note: This command currently throws errors on *nix. Looking
    at a fix for this issue. Until then, avoid using this command
    on that platform.
    """

    # Get general system info
    sys_os = (platform.system())
    sys_version = ''.join(platform.version())
    python_version = platform.python_version()
    sys_architecture = platform.machine()

    # psutil-specific functionality
    process = Process(getpid())

    ram_usage = format_bytes(process.memory_info()[0])

    cpu_usage = process.cpu_percent()
    thread_count = process.num_threads()
    uptime = timedelta(seconds=round(time() - process.create_time()))

    if sys.platform == 'win32':
        bot.sendMessage(chat_id=update.message.chat_id,
                        parse_mode='Markdown',
                        text="*Basic Info*:\n\n"
                             "*OS*: {} {}\n"
                             "*Python Version*: {}\n"
                             "*Architecture*: {}\n\n"
                             "*Bot-specific Info*:\n\n"
                             "*Uptime*: {}\n"
                             "*Threads*: {}\n"
                             "*CPU Usage*: {}\n"
                             "*RAM Usage:* {}".format(sys_os,
                                                      sys_version,
                                                      python_version,
                                                      sys_architecture,
                                                      uptime,
                                                      thread_count,
                                                      cpu_usage,
                                                      ram_usage))
    else:
        bot.sendMessage(chat_id=update.message.chat_id,
                        parse_mode='Markdown',
                        text="Sorry, but this command is only supported if the bot is running on Windows due to issues "
                             "with the bot's current psutil implementation.")
