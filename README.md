# ⚡ Telegram bot

It is a template you can use for creating telegram bot with aiogram 3

### Tools:

- 💪 Aiogram (v3)
- 🤹🏽 Loguru
- 📔 SqlAlchemy (ORM)
## 🧑‍💻 Changelog

### [1.0.3] - 2024-02-12
    1. 🐛 Fixed bug in feature Z.
    2. 📑Adding database
### [1.0.2] - 2023-12-08
    1. 🐛 Fixed bug in feature Z.

### [1.0.1] - 2023-11-23
    1.🐛 Fixed bug in feature Z.
    2.📚 Updated filters.

### [1.0.0] - 2023-11-20
    1.🎉 Initial release.

---

## 🔥 Getting started

### Requirements:

- Python

### Installing

###### For linux and macOS

```bash
cd aiogram-template
python3 -m venv env
. env/bin/activate
pip install -r requirements.txt
```

###### For windows

```bash
cd aiogram-template
python -m venv env
env\scripts\activate
pip install -r requirements.txt
```

### Starting

Create a file named `.env`.
Add the following line to the `.env` file: `BOT_TOKEN="TOKEN"`
Replace `TOKEN` with your actual bot token. If you have `admins` you need to add admin_users `id` to `ADMINS=[]`.
Save the `.env` file.
```bash
python src/bot.py
```

## ✍ Adding handlers

Just create new file in _src/handlers_ folder or its subfolder

#### Initialize router and use it to handle events:

```python
from aiogram import Router
my_router = Router()
```

#### Add created router to router list in _src/handlers/\_\_init\_\_.py_:

```python
from .my_file import my_router
routers = [my_router]
```

## 🙋🏽‍♂️ Contact me

[<img width="30px" title="lleballex | Telegram" src="https://raw.githubusercontent.com/github/explore/main/topics/telegram/telegram.png">](https://t.me/makhmud_dev)
