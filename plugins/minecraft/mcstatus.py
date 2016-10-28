import json

import requests
from telegram import ParseMode
from telegram.ext.dispatcher import run_async


@run_async
def mc_status(_, update):
    """
    This plugin fetches the status of the Minecraft/Mojang
    servers and then posts the retrieved status information
    as a Telegram message.
    """
    mcstatus_baseurl = "https://status.mojang.com/check"
    mcstatus_request = requests.get(mcstatus_baseurl).text

    try:
        mcstatus_request
    except (requests.exceptions.HTTPError, requests.exceptions.ConnectionError) as e:
        update.message.reply_text(text="Unable to get Minecraft server status: {}".format(e))

    # Take the JSON Mojang's status site gives me
    # and turn it into a nice format.
    data = json.loads(mcstatus_request.replace("}", "").replace("{", "").replace("]", "}").replace("[", "{"))
    out = []

    # Use a fancy loop so I don't have to update
    # this when Mojang adds new servers.
    green = []
    yellow = []
    red = []
    for server, status in list(data.items()):
        if status == "green":
            green.append(server)
        elif status == "yellow":
            yellow.append(server)
        else:
            red.append(server)

    if green:
        green.sort()
        out.append("*The following Mojang services are online*:\n" +
                   "\n".join(green))
    if yellow:
        yellow.sort()
        out.append("*The following Mojang services are currently having issues*:\n" +
                   ",\n".join(yellow))
    if red:
        red.sort()
        out.append("*The following Mojang services are currently offline*:" +
                   ",\n".join(red))

    out = " ".join(out)

    update.message.reply_text(parse_mode=ParseMode.MARKDOWN,
                              disable_web_page_preview=True,
                              text=out)
