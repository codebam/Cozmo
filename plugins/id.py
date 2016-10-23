def id_plugin(bot, update):
    uname = update.message.from_user.first_name
    uid = update.message.from_user.id

    bot.sendMessage(chat_id=update.message.chat_id, text="You are *{0}* with ID `{1}`.".format(
        uname, uid), parse_mode='Markdown')
