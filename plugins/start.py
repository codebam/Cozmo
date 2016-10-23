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


def start(bot, update):
    """
    Create a basic start command. Nothing fancy
    here folks.
    """
    bot.sendMessage(chat_id=update.message.chat_id,
                    parse_mode='Markdown',
                    disable_web_page_preview=True,
                    text="Hi! Please enter /about to view information about me.")
