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

    uptime_text = "*Uptime*: ", pc_uptime
    uptime_text = "".join(uptime_text)

    # Retrieves the OS name and the version.
    os = platform.system()
    version = platform.version()

    # CPU information. Uses psutil facilities for
    # the CPU count for non logical CPU cores.
    cpus = psutil.cpu_count(logical=False)
    cpus_log = psutil.cpu_count(logical=True)
    cpu_string = str(psutil.cpu_percent(interval=0.5, percpu=True)).replace("[", " ").replace("]", " ")

    # Return CPU cores along with the load on the CPU(s).
    cpu_cores = "*CPU cores*: physical: ", str(cpus), ", logical: ", str(cpus_log)
    cpu_cores = "".join(cpu_cores)
    cpu_text = "*CPU load*: ", str(cpu_string)
    cpu_text = "".join(cpu_text)

    # HDD info such as total HDD space, percentage,
    # and used HDD space.
    hdd = psutil.disk_usage('/')
    hdd_total = round(hdd[0] / 1024 ** 3, 1)
    hdd_used = round(hdd[1] / 1024 ** 3, 1)
    hdd_percentage = hdd[3]

    hdd_text = "*HDD usage*: ", str(hdd_percentage), "% (", str(hdd_used), " GB of ", str(hdd_total), " GB)"
    hdd_text = "".join(hdd_text)

    update.message.reply_text(parse_mode='Markdown',
                              text="*System Info*:\n\n*OS*: " + os + " " + version + "\n" + cpu_cores + "\n" + cpu_text
                                   + "\n" + hdd_text + "\n" + uptime_text)
