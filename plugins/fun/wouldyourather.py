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

try:
    import ujson as json
except ImportError:
    import json

import requests


def wouldyourather(_, update):
    """
    Sends a message containing a question
    from the rrrather website.
    """
    wyr_url = "https://www.rrrather.com/botapi"

    wyr_request = requests.get(wyr_url).text
    wyr_json = json.loads(wyr_request)

    wyr_vars = {
        "title": wyr_json["title"].capitalize(),
        "choices":
            {
                "A": wyr_json["choicea"].replace("?", ""),
                "B": wyr_json["choiceb"].replace("?", "")
            },
        "votes": '{0:,}'.format(wyr_json["votes"]),
        "tags": wyr_json["tags"].replace(",", ", "),
        "view_text": "*View this question on rrrather*",
        "link": wyr_json["link"].replace("http", "https"),
    }
    
    try:
        update.message.reply_text(parse_mode='Markdown',
                                  disable_web_page_preview=True,
                                  text="{}:\n"
                                       "*Choice A*: {}\n"
                                       "*Choice B*: {}\n\n"
                                       "*Votes*: {}\n"
                                       "*Tags*: {}\n"
                                       "{}: {}".format(wyr_vars['title'],
                                                       wyr_vars['choices']['A'],
                                                       wyr_vars['choices']['B'],
                                                       wyr_vars['votes'],
                                                       wyr_vars['tags'],
                                                       wyr_vars['view_text'],
                                                       wyr_vars['link']))
    except AttributeError:
        update.message.reply_text(text="`Error trying to retrieve a would you "
                                       "rather question. Please try again.`")
