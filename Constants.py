import os

# TOKENS
BOT_TOKEN = os.getenv("BOT_TOKEN")
DREAMLO_URL = os.getenv("DREAMLO_URL")
REDDIT_KEY = os.getenv("REDDIT_KEY")
REDDIT_SECRET = os.getenv("REDDIT_SECRET")

PREFIX = "="
DEVS_IDS = [669861531034583060]
ALL_EXTENSIONS = ["_help"]

SUB_COMMANDS_TEXT = {
    "Fun" :
        {
            "insult" : "Incase you want to get roasted."
        },

    "Moderation" :
        {
            "ban" : f"Bans a member.\nUse : ```{PREFIX}ban [USER]```",
            "kick" : f"Kicks a member from the server.\nUser : ```{PREFIX}kick [USER]```"
        },

    "Utility" :
        {
            "av" : f"See your or a user's profile picture.\nUse : ```{PREFIX}av```\nor use : ```{PREFIX}av [USER]```"
        }

}
