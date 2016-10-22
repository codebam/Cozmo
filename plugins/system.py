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
import os
import platform
import time
from datetime import timedelta

import psutil
from telegram import ParseMode

import EddieBot
from utils.size import size as format_bytes


def about(bot, update):
    """
    Send a message giving info about the bot and contain
    a link to the bot's source code.
    """
    bot.sendMessage(chat_id=update.message.chat_id,
                    parse_mode=ParseMode.MARKDOWN,
                    disable_web_page_preview=True,
                    text="This bot is powered by *EddieBot* {}, the plugin-based bot written in Python 3.\n\n"
                         "*Source Code*: https://github.com/KamranMackey/EddieBot".format(EddieBot.__version__))


def system(bot, update):
    """
    Send a message containing information about the system
    running the bot. Also contains information about the bot's
    process.
    """

    # Get general system info
    sys_os = (platform.system())
    sys_version = ''.join(platform.version())
    python_version = platform.python_version()
    sys_architecture = platform.machine()

    # psutil-specific functionality
    process = psutil.Process(os.getpid())
    memory_usage = format_bytes(process.memory_info()[0])
    cpu_usage = process.cpu_percent()
    thread_count = process.num_threads()
    uptime = timedelta(seconds=round(time.time() - process.create_time()))

    bot.sendMessage(chat_id=update.message.chat_id,
                    parse_mode=ParseMode.MARKDOWN,
                    text="*Basic Info*:\n\n"
                         "*OS*: {} {}\n"
                         "*Python Version*: {}\n"
                         "*Architecture*: {}\n\n"
                         "*Bot-specific Info*:\n\n"
                         "*Uptime*: {}\n"
                         "*Threads*: {}\n"
                         "*CPU Usage*: {}\n"
                         "*Memory Usage:* {}".format(sys_os,
                                                     sys_version,
                                                     python_version,
                                                     sys_architecture,
                                                     uptime,
                                                     thread_count,
                                                     cpu_usage,
                                                     memory_usage))
