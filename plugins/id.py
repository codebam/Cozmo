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


def id_plugin(_, update):
    """
    Simple plugin used for retrieving a user's ID by doing
    the /id command.
    """
    uname = update.message.from_user.first_name
    uid = update.message.from_user.id

    update.message.reply_text(parse_mode='Markdown',
                              quote=True,
                              text="You are *{0}* with ID `{1}`.".format(uname, uid))
