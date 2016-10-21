# Eddie
Eddie is a Telegram bot coded in Python, and uses the awesome [python-telegram-bot](https://python-telegram-bot.org) 
library as a base. 

**Note**: Eddie is still in development, and because of this, it may or may not contain bugs. We'll see.

## Installation

### Clone the repository
```
git clone https://github.com/KamranMackey/EddieBot.git
cd EddieBot
```

### Install required dependencies
```
pip install -r requirements.txt
```

### Mark as excutable (Linux-only!)
```
chmod +x EddieBot.py
```

### Run
Run `EddieBot.py` once so that it can generate the `config.ini` file. You will get an "Invalid token" error due to the 
`token` setting being blank, but just ignore it for now. Now, edit `config.ini`, and under the `Basic Settings` section, 
set your token to the one you received from BotFather. You should now be able to run the bot!

## License
    Copyright © 2016 Kamran Mackey
    
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Lesser Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Lesser Public License for more details.

    You should have received a copy of the GNU Lesser Public License
    along with This program. If not, see <http://www.gnu.org/licenses/>.
    
