from os import environ

API_HASH = environ.get("API_HASH", "e35a05d338376cbcd8162f810aed878d")
API_ID = int(environ.get("API_ID", "29483517"))
BOT_TOKEN = environ.get("BOT_TOKEN", "7650392649:AAH3kTZMo2uOtOjM0x6Ur4JUeVdP_RzS1Xc")
BOT_OWNER = int(environ.get("BOT_OWNER", "5756495153"))
BOT_USERNAME = environ.get("BOT_USERNAME", "Feedbackdenabot")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002616517280"))
AUTH_CHANNEL = int(environ.get("AUTH_CHANNEL", "-1002497873969"))
DATABASE_URL = environ.get("DATABASE_URL", "mongodb+srv://user1:abhinai.2244@cluster0.7oaqx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# Define default emojis list
EMOJIS = [
    "👍", "🤷‍♂", "❤", "🔥", "🥰", "👏", "😁", "🤔", "🤯", "😱", "🤬", "😢", 
    "🥶", "🤩", "🥳", "😎", "🙏", "👌", "🤣", "😇", "🥱", "🥴", "😍", "🤓", 
    "❤‍🔥", "🌚", "😐", "💯", "🦄", "⚡", "👾", "🏆", "💔", "🤨", "🌟", "😡", 
    "👅", "🆒", "😘", "😈", "😴", "😭", "👻", "🌈", "👨‍💻", "👀", "🎃", "🙄", 
    "🤧", "😨", "🤝", "🤐", "🤗", "🫡", "🤭", "🥸", "🤫", "😶‍🌫", "🤪", "😏"
]
