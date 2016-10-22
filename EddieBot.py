#!/usr/bin/env python
#
# Copyright (C) 2016 Kamran Mackey
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

import configparser
import logging
import os
import sys

from telegram.ext import Updater

# Check if the Python version is 3.4 or higher, otherwise the bot
# will not run.
if sys.version_info < (3, 4, 0):
    print("Python 3.4 or later is required. Please update your Python version.")
    sys.exit(1)

__version__ = "0.0.1"

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def main():
    # Initialize a config file, so that way the user doesn't have to worry
    # about creating a config file manually.
    config = configparser.ConfigParser(allow_no_value=True)

    # Create a 'Basic Settings' section and add a setting to it. This is
    # where the user's token will be stored.
    config['Basic Settings'] = {'; This configures basic settings such as your token.\n'
                                'token': ''}

    # Generate the config file as config.ini. If the file already exists,
    # do not overwrite it, as we don't want the user to lose their existing
    # configuration.
    if not os.path.exists('config.ini'):
        with open('config.ini', 'w') as configfile:
            config.write(configfile)

    config.read('config.ini')

    token = config.get('Basic Settings', 'token')

    # Create an Updater and pass it to the bot's token.
    updater = Updater(token)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    def error(update, err):
        logger.warn('Update "%s" caused error "%s"' % (update, err))

    # log all errors
    dp.add_error_handler(error)

    # Start the bot
    updater.start_polling()

    # Run the bot until the you presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
