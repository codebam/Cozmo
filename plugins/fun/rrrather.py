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

import json

import requests


def rrrather(_, update):
    """
    Sends a message containing a question
    from the rrrather website.
    """
    rrrather_url = "https://www.rrrather.com/botapi"

    rrrather_request = requests.get(rrrather_url).text
    rrrather_json = json.loads(rrrather_request)

    # Variables
    title = rrrather_json["title"]
    choice_a = rrrather_json["choicea"]
    choice_b = rrrather_json["choiceb"]
    votes = rrrather_json["votes"]
    link = rrrather_json["link"].replace("http", "https")

    # Message text
    update.message.reply_text(parse_mode='Markdown',
                              disable_web_page_preview=True,
                              text="{0}: {1} or {2}?\n\n"
                                   "*Votes*: {3}\n"
                                   "*View question on rrrather*: {4}".format(title,
                                                                             choice_a,
                                                                             choice_b,
                                                                             votes,
                                                                             link))
