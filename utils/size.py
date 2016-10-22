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

standard = [
    (1024 ** 5, ' PB'),
    (1024 ** 4, ' TB'),
    (1024 ** 3, ' GB'),
    (1024 ** 2, ' MB'),
    (1024 ** 1, ' KB'),
    (1024 ** 0, (' byte', ' bytes')),
]

verbose = [
    (1024 ** 5, (' petabyte', ' petabytes')),
    (1024 ** 4, (' terabyte', ' terabytes')),
    (1024 ** 3, (' gigabyte', ' gigabytes')),
    (1024 ** 2, (' megabyte', ' megabytes')),
    (1024 ** 1, (' kilobyte', ' kilobytes')),
    (1024 ** 0, (' byte', ' bytes')),
]

# aliases
S = standard
V = verbose


def size(b, system=standard):
    """Human-readable file sizes.
    This uses the standard system used in things like operating systems
    by default, but the system can be changed to verbose if desired.
    """
    for factor, suffix in system:
        if b >= factor:
            break
    amount = int(b / factor)
    if isinstance(suffix, tuple):
        singular, multiple = suffix
        if amount == 1:
            suffix = singular
        else:
            suffix = multiple
    return str(amount) + suffix
