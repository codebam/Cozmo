#
# Copyright (C) 2016 Kamran Mackey and contributors
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.


def truncate(content, length=100, suffix='...'):
    """
    Truncates a string after a certain number of characters.
    Function always tries to truncate on a word boundary.
    :rtype str
    """
    if len(content) <= length:
        return content
    else:
        return content[:length].rsplit(' ', 1)[0] + suffix
