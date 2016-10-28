#
# Copyright (C) 2016 Kamran Mackey and contributors
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

import json

import requests
from telegram import ChatAction, ParseMode


def xkcd_plugin(_, update, args):
    base_url = "https://xkcd.com/info.0.json"
    strip_url = 'https://xkcd.com/%s/info.0.json'

    try:
        num = int(args[0])
        xkcd = requests.get(strip_url % num).text
        xkcd = json.loads(xkcd)

        title = xkcd['title']
        alt = xkcd['alt']

        # also sending the 'num' is too redundant in this case
        caption = '{0} - {1}'.format(title, alt)
        update.message.chat.send_action(action=ChatAction.UPLOAD_PHOTO)
        update.message.reply_photo(photo=xkcd['img'],
                                   caption=caption)
    except ValueError:
        # Send an error message if the ID format is wrong.
        update.message.chat.send_action(action=ChatAction.TYPING)
        update.message.reply_text(parse_mode=ParseMode.MARKDOWN,
                                  text="*Error*: Improper format of xkcd ID. IDs are numeric. Please "
                                       "enter a numeric ID.\n\n"
                                       "*Example xkcd ID*: 378")
    except IndexError:
        # If ID is not given, send the latest xkcd image.
        xkcd = requests.get(base_url).text
        xkcd = json.loads(xkcd)

        num = xkcd['num']

        title = xkcd['title']
        alt = xkcd['alt']

        caption = '{0} - {1} - {2}'.format(num, title, alt)

        update.message.chat.send_action(action=ChatAction.UPLOAD_PHOTO)
        update.message.reply_photo(photo=xkcd['img'],
                                   caption=caption)
