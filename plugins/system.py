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

import psutil
from uptime import uptime


def seconds_to_str(seconds):
    """
    Converts seconds to a string as described
    in the function name.
    """
    days, remainder = divmod(seconds, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)
    return "{} day(s) {:02}:{:02}:{:02}".format(days, hours, minutes, seconds)


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
    version = platform.version().strip('.')[:2]

    # CPU information. Uses some psutil facilities for the
    # CPU count of logical and non-logical CPU cores.
    cpu_count = psutil.cpu_count(logical=False)
    cpus_log = psutil.cpu_count(logical=True)
    cpu_string = str(psutil.cpu_percent(interval=0.5, percpu=True)).replace("[", " ").replace("]", " ")

    # Return the number of CPU cores along with the
    # current load on the CPU(s).
    cpu_core_count = "*CPU cores*: physical: ", str(cpu_count), ", logical: ", str(cpus_log)
    cpu_cores = "".join(cpu_core_count)
    cpu_load_text = "*CPU load*: ", str(cpu_string)
    cpu_text = "".join(cpu_load_text)

    # HDD info such as total HDD space, percentage, and
    # used HDD space.
    hdd_usage = psutil.disk_usage('/')
    hdd_total = round(hdd_usage[0] / 1024 ** 3, 1)
    hdd_used = round(hdd_usage[1] / 1024 ** 3, 1)
    hdd_percentage = hdd_usage[3]

    hdd_usage_text = "*HDD usage*: ", str(hdd_percentage), "% (", str(hdd_used), " GB of ", str(hdd_total), " GB)"
    hdd_text = "".join(hdd_usage_text)

    update.message.reply_text(parse_mode='Markdown',
                              text="*System Info*:\n\n" + "*OS*: " + os + " " + version + "\n" + cpu_cores + "\n" +
                                   cpu_text + "\n" + hdd_text + "\n" + uptime_text)
