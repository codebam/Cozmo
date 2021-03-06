# Cozmo
Cozmo is a Telegram bot coded in Python, and uses the awesome [python-telegram-bot](https://python-telegram-bot.org) 
([Source Code](https://github.com/python-telegram-bot/python-telegram-bot)) library as a base. 

**Note**: Cozmo is still in development, and because of this, it may or may not contain bugs. We'll see.

## Installation
Python 3.4 or later is required for Cozmo to run. I personally recommend Python 3.5.2 for the best performance. 

**Note regarding Python 3.6 support**: 3.6 has no breaking changes in syntax and as such, Cozmo will be compatible with
3.6 on release.

### Clone the repository
```
git clone https://github.com/KamranMackey/Cozmo.git
cd Cozmo
```

### Install required dependencies
```
pip install -r requirements.txt
```

### Mark as excutable (Linux-only!)
```
chmod +x Cozmo.py
```
Or, if you don't want to mess with file permissions, you can also do this:
```
python Cozmo.py
```

### Run
Run `Cozmo.py` once so that it can generate the `config.ini` file. Then, edit `config.ini`, and under the `Basic Settings` section, 
set your token to the one you received from BotFather. You should now be able to run the bot!

## License
    Copyright © 2016 Kamran Mackey and contributors
    
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with This program. If not, see <http://www.gnu.org/licenses/>.
    
