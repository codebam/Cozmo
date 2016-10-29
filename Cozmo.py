#!/usr/bin/env python
#
# Copyright (C) 2016 Kamran Mackey and contributors
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

import logging as log
import sys
from configparser import ConfigParser
from os.path import exists

from telegram.ext import (CommandHandler, Updater)

from plugins.fun.wouldyourather import wouldyourather
from plugins.fun.xkcd import xkcd_plugin as xkcd
from plugins.info.about import about
from plugins.info.libraries import libraries
from plugins.minecraft.mcstatus import mc_status
from plugins.misc.id import id_plugin
from plugins.misc.kernel import kernel
from plugins.misc.me import me
from plugins.misc.start import start
from plugins.shitposts.lenny import lenny
from plugins.util.system import system

# Require Python version to be 3.4 or higher.
minpython = (3, 4, 0)
if sys.version_info < minpython:
    print("Python 3.4 or later is required. Please update your Python version.")
    sys.exit(1)

# Enable logging
log.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                level=log.INFO)

logger = log.getLogger("Cozmo")


def main():
    """
    Main method of the bot. It initializes the configuration system,
    sets up basic log messages, creates a dispatcher/updater, and
    registers plugins. It also keeps the bot from killing itself.
    """
    # Initialize a config file, so that way the user doesn't have to worry
    # about creating a config file manually.
    logger.info("Initializing config system.")
    config = ConfigParser(allow_no_value=True)

    # Create a 'Basic Settings' section and add a setting to it. This is
    # where the user's token will be stored.
    config['Basic Settings'] = {'; This configures basic settings such as your token.\n'
                                'token': ''}

    # Generate the config file as config.ini. If the file already exists,
    # do not overwrite it, as we don't want the user to lose their existing
    # configuration.
    if not exists('config.ini'):
        with open('config.ini', 'w') as configfile:
            logger.info("Generating the config file.")
            config.write(configfile)
            logger.info("Generated the config file.")
            exit(0)  # Exit after the config file has generated.
    else:
        logger.info("Config file found. Not overwriting existing file.")

    config.read('config.ini')

    token = config.get('Basic Settings', 'token')
    logger.info("Config system initialized. Loading the bot.")

    # Create an Updater and pass it to the bot's token.
    updater = Updater(token)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Register plugins and their applicable commands.
    logger.info("Starting plugin loading sequence.")

    dp.add_handler(CommandHandler('about', about))
    dp.add_handler(CommandHandler('libraries', libraries))
    dp.add_handler(CommandHandler('me', me, pass_args=True))
    dp.add_handler(CommandHandler('xkcd', xkcd, pass_args=True))
    dp.add_handler(CommandHandler('wyr', wouldyourather))
    dp.add_handler(CommandHandler('mcstatus', mc_status))
    dp.add_handler(CommandHandler('linux', kernel))
    dp.add_handler(CommandHandler('id', id_plugin))
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('system', system))
    dp.add_handler(CommandHandler('lenny', lenny))

    logger.info("Plugin loading sequence complete. All plugins loaded.")

    def error(_, update, err):
        logger.warn('Update "%s" caused error "%s"' % (update, err))

    # Create an error handler
    dp.add_error_handler(error)

    # Start polling for updates
    updater.start_polling()

    # Run the bot until the you presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
