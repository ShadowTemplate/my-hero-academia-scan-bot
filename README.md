# My Hero Academia Scan Bot

A Telegram bot to receive notifications when new My Hero Academia weekly contents are available.
This bot periodically checks if new English chapters are released on
[MangaPlus (Shueisha)](https://mangaplus.shueisha.co.jp/).


---
## Information

**Status**: `Actively maintained`

**Type**: `Personal project`

**Development year(s)**: `2023+`

**Author(s)**: [ShadowTemplate](https://github.com/ShadowTemplate)

**Notes**: *For personal use.*

---
## Getting Started

This bot is for personal use only, but you can create your own Heroku project and reuse it. Please create a *secrets.py* file and set these 
two values:

```
op_bot_token = "your_telegram_bot_token"
telegram_chat_id = "your_telegram_chat_id"
```

### Prerequisites

Clone the repository and install the required Python dependencies:

```
$ git clone https://github.com/ShadowTemplate/my-hero-academia-scan-bot.git
$ cd my-hero-academia-scan-bot/
$ pip install --user -r requirements.txt
```

### Deployment

This repository includes the required Heroku configuration files. The project 
is thus ready to be deployed.


---
## Building tools

* [Python 3.9](https://www.python.org/downloads/release/python-390/) - 
Programming language
* [python-telegram-bot](https://python-telegram-bot.org/) - Telegram API 
wrapper 
* [pyquery](http://pyquery.readthedocs.io/en/latest/) - HTML parsing

---
## Contributing

Any contribution is welcome. Feel free to open issues or submit pull requests.

---
## License

This project is licensed under the GNU GPLv3 license.
Please refer to the [LICENSE.md](LICENSE.md) file for details.

---
*This README.md complies with [this project template](
https://github.com/ShadowTemplate/project-template). Feel free to adopt it
and reuse it.*
