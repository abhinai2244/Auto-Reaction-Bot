from os import environ

API_HASH = environ.get("API_HASH", "b98dff566803b43b3c3120eec537fc1d")
API_ID = int(environ.get("API_ID", "27152769"))
BOT_TOKEN = environ.get("BOT_TOKEN", "7650392649:AAHPpHvaHsjFtl27-q_ImkE1ZeHsGkls8kE")
BOT_OWNER = int(environ.get("BOT_OWNER", "5756495153"))
BOT_USERNAME = environ.get("BOT_USERNAME", "Feedbackdenabot")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002298830187"))
AUTH_CHANNEL = int(environ.get("AUTH_CHANNEL", "-4601190800"))
DATABASE_URL = environ.get("DATABASE_URL", "mongodb+srv://user1:abhinai.2244@cluster0.7oaqx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# Define default emojis list
EMOJIS = [
    "👍", "🤷‍♂", "❤", "🔥", "🥰", "👏", "😁", "🤔", "🤯", "😱", "🤬", "😢", 
    "🥶", "🤩", "🥳", "😎", "🙏", "👌", "🤣", "😇", "🥱", "🥴", "😍", "🤓", 
    "❤‍🔥", "🌚", "😐", "💯", "🦄", "⚡", "👾", "🏆", "💔", "🤨", "🌟", "😡", 
    "👅", "🆒", "😘", "😈", "😴", "😭", "👻", "🌈", "👨‍💻", "👀", "🎃", "🙄", 
    "🤧", "😨", "🤝", "🤐", "🤗", "🫡", "🤭", "🥸", "🤫", "😶‍🌫", "🤪", "😏"
]
