#
# Copyright (C) 2016 Kamran Mackey and contributors
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

import json

import requests
from telegram import ChatAction


def wouldyourather(_, update):
    """
    Sends a message containing a question
    from the rrrather website.
    """
    wyr_url = "https://www.rrrather.com/botapi"

    wyr_request = requests.get(wyr_url).text
    wyr_json = json.loads(wyr_request)

    # Dictionary containing variables used in
    # the wyr message text.
    wyr = {
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
        update.message.chat.send_action(action=ChatAction.TYPING)
        update.message.reply_text(parse_mode='Markdown',
                                  disable_web_page_preview=True,
                                  text="{}:\n"
                                       "*Choice A*: {}\n"
                                       "*Choice B*: {}\n\n"
                                       "*Votes*: {}\n"
                                       "*Tags*: {}\n"
                                       "{}: {}".format(wyr['title'],
                                                       wyr['choices']['A'],
                                                       wyr['choices']['B'],
                                                       wyr['votes'],
                                                       wyr['tags'],
                                                       wyr['view_text'],
                                                       wyr['link']))
    except AttributeError:
        update.message.chat.send_action(ChatAction.TYPING)
        update.message.reply_text(text="`Error trying to retrieve a would you rather "
                                       "question due to an AttributeError or a connection "
                                       "problem with the rrrather json API. Please try "
                                       "again later.`")
