# Copyright (C) 2016 Kamran Mackey and contributors
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

import random

# Create a variable containing
# a whole bunch of lenny faces.
#
# Generously borrowed from a person
# who already had this variable created
# for one of their Python programs.
lenny_faces = [u'( \u0361\u00B0 \u035C\u0296 \u0361\u00B0)',
               u'( \u0360\u00B0 \u035F\u0296 \u0361\u00B0)',
               u'\u1566( \u0361\xb0 \u035c\u0296 \u0361\xb0)\u1564',
               u'( \u0361\u00B0 \u035C\u0296 \u0361\u00B0)',
               u'( \u0361~ \u035C\u0296 \u0361\u00B0)',
               u'( \u0361o \u035C\u0296 \u0361o)',
               u'\u0361\u00B0 \u035C\u0296 \u0361 -',
               u'( \u0361\u0361 \u00B0 \u035C \u0296 \u0361 \u00B0)\uFEFF',
               u'( \u0361 \u0361\u00B0 \u0361\u00B0  \u0296 \u0361\u00B0 \u0361\u00B0)',
               u'(\u0E07 \u0360\u00B0 \u035F\u0644\u035C \u0361\u00B0)\u0E07',
               u'( \u0361\u00B0 \u035C\u0296 \u0361 \u00B0)',
               u'( \u0361\u00B0\u256D\u035C\u0296\u256E\u0361\u00B0 )']


def lenny(_, update):
    """
    Returns a lennyface when /lenny is sent to
    please all those people out there who have
    a lenny fetish or rather, an obsession.
    """
    update.message.reply_text(text=random.choice(lenny_faces))
