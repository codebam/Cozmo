#
# Copyright (C) 2016 Kamran Mackey and contributors
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

import platform

import psutil
from telegram import ChatAction
from uptime import uptime


def seconds_to_str(seconds):
    """
    Converts seconds to a string as described
    in the function name.
    """
    days, remainder = divmod(seconds, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)
    return "{} day(s), up for {:02}:{:02}:{:02}".format(days, hours, minutes, seconds)


def system(_, update):
    """
    Plugin for retrieving information about the
    server/computer running the bot.
    """
    # Retrieve the uptime of the host system.
    uptimetostr = int(uptime())
    pc_uptime = seconds_to_str(uptimetostr)

    uptime_retrieval = "*Uptime*: ", pc_uptime
    uptime_text = "".join(uptime_retrieval)

    # Retrieves the OS name and the version.
    os = platform.system()
    pyver = platform.python_version()
    version = platform.version()

    # CPU information. Uses some psutil facilities for the
    # CPU count of logical and non-logical CPU cores.
    cpu_count = psutil.cpu_count(logical=False)
    cpus_log = psutil.cpu_count(logical=True)
    cpu_string = str(psutil.cpu_percent(interval=0.5, percpu=True)).replace("[", " ").replace("]", " ")

    # Return the number of CPU cores along with the
    # current load on the CPU(s).
    cpu_core_count = "*CPU cores*: ", str(cpu_count), " physical, ", str(cpus_log), " logical"
    cpu_cores = "".join(cpu_core_count)
    cpu_load_text = "*CPU load*: ", str(cpu_string)
    cpu_text = "".join(cpu_load_text)

    update.message.chat.send_action(action=ChatAction.TYPING)
    update.message.reply_text(parse_mode='Markdown',
                              text="*System Info*:\n\n" + "*OS*: " + os + " " + version + "\n" +
                                   "*Python Version*: " + pyver + "\n" + cpu_cores + "\n" + cpu_text
                                   + "\n" + uptime_text)
