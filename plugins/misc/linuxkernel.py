#
# Copyright (C) 2016 Kamran Mackey and contributors
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

import re
import requests

from telegram import ParseMode


def kernel(_, update):
    """
    Retrieves a list of Linux kernel versions
    and then sends them as a message.

    Note: This uses a tiny bit of regex to get
    rid of the "The latest version of the Linux
    Linux kernel is" crap as we don't need it.
    """
    kernel_retrieval = requests.get("https://www.kernel.org/finger_banner").text
    kernel_ver_regex_a = re.sub(r"The latest(\s*)", '', kernel_retrieval)
    kernel_ver_regex_b = re.sub(r"version of the Linux kernel is:(\s*)", '- ', kernel_ver_regex_a)
    lines = kernel_ver_regex_b.split("\n")

    message = "*Linux kernel versions*:\n\n" \
              "{}".format("\n".join(line for line in lines[:-1]))
    update.message.reply_text(parse_mode=ParseMode.MARKDOWN,
                              text=message)
