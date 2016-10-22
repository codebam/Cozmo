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

import requests
import json


def xkcd_plugin(bot, update, args):
    try:
        num = int(args[0])
        xkcd = requests.get('https://xkcd.com/%s/info.0.json' % num).text
        xkcd = json.loads(xkcd)

        title = xkcd['title']
        alt = xkcd['alt']

        # also sending the 'num' is too redundant in this case
        caption = '{0} - {1}'.format(title, alt)
        bot.sendPhoto(chat_id=update.message.chat_id,
                      photo=xkcd['img'], caption=caption)
    except ValueError:
        # NaN
        bot.sendMessage(chat_id=update.message.chat_id,
                        text="`Error: Improper format of xkcd ID. Only numbers are allowed.\n\n"
                             "Example xkcd ID: 378`", parse_mode='Markdown')
    except IndexError:
        # num not given, send latest
        xkcd = requests.get('https://xkcd.com/info.0.json').text
        xkcd = json.loads(xkcd)

        num = xkcd['num']

        title = xkcd['title']
        alt = xkcd['alt']

        caption = '{0} - {1} - {2}'.format(num, title, alt)

        bot.sendPhoto(chat_id=update.message.chat_id,
                      photo=xkcd['img'], caption=caption)
