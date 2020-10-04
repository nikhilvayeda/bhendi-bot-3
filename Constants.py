import os

# TOKENS
BOT_TOKEN = os.getenv("BOT_TOKEN")
DREAMLO_URL = os.getenv("DREAMLO_URL")
REDDIT_KEY = os.getenv("REDDIT_KEY")
REDDIT_SECRET = os.getenv("REDDIT_SECRET")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

PREFIX = "="
DEVS_IDS = [669861531034583060]
ALL_EXTENSIONS = ["_help", "ban", "kick", "mute_unmute", "purge", "unban"]

TEST_ACCOUNT = "@SaimanSays#3455"

SUB_COMMANDS_TEXT = {
    "Fun" :
        {
            "insult" : "Incase you want to get roasted."
        },

    "Moderation" :
        {
            "ban" : f"Bans a member.\nUse : ```{PREFIX}ban [USER]```",
            "unban" : f"Unbans a member.\nUse : ```{PREFIX}unban [USER]```",
            "kick" : f"Kicks a member from the server.\nUser : ```{PREFIX}kick [USER]```",
            "purge" : "Purges messages.\nUser `=help purge` to see a full help."
        },

    "Utility" :
        {
            "av" : f"See your or a user's profile picture.\nUse : ```{PREFIX}av```\nor use : ```{PREFIX}av [USER]```"
        }

}

SUB_SUB_COMMANDS_TEXT = {
    "insult" : {
        "insult" : f"Incase you want to get roasted.",
    },

    "ban" : {
        "ban [USER]" : f"Bans a member.\nExample : ```{PREFIX}ban {TEST_ACCOUNT}```"
    },

    "unban" : {
        "unban [USER]" : f"Unbans a banned member.\nExample : ```{PREFIX}unban {TEST_ACCOUNT}```"
    },

    "kick" : {
        "kick [USER]" : f"kicks a member from the server.\nExample : ```{PREFIX}kick {TEST_ACCOUNT}```"
    },

    "purge" : {
        "purge [AMOUNT]" : f"Purges the given amount of messages.\nExample : ```{PREFIX}purge 100```",
        "purge bot [AMOUNT]" : f"Purges the given amount of messages if the message is by a bot.\nExample : ```{PREFIX}purge bot 100```",
        "purge human [AMOUNT]" : f"Purges the given amount of messages if the message is by a human.\nExample : ```{PREFIX}purge human 100```",
        "purge user [USER] [AMOUNT]" : f"Purges the given amount of messages if the message is by the user provided.\nExample : ```{PREFIX}purge user {TEST_ACCOUNT} 100```"
    },

    "av" : {
        "av" : f"See your profile picture.\nExample : ```{PREFIX}av```",
        "av [USER]" : f"See a user's profile picture.\nExample : ```{PREFIX} {TEST_ACCOUNT}```"
    }
}

# Server Specific constants
SERVER_ID = 722336877524418620

ROLE_IDS = {
    "MUTE_ROLE_ID" : 722386628064182302
}
