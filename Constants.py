import os

# TOKENS
BOT_TOKEN = os.getenv("BOT_TOKEN")
DREAMLO_URL = os.getenv("DREAMLO_URL")
REDDIT_KEY = os.getenv("REDDIT_KEY")
REDDIT_SECRET = os.getenv("REDDIT_SECRET")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

PREFIX = "="
DEVS_IDS = [669861531034583060]
ALL_EXTENSIONS = ["_help", "ban", "kick", "mute_unmute", "purge", "unban", "av"]

DATABASE_REPO_NAME = "bhendi-bot-data"
DATABASE_FILENAME = "ALL_DATA.json"

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
            "av" : f"See your or a user's profile picture.\nUse : ```{PREFIX}av```\n"\
            f"or use : ```{PREFIX}av [USER]```"
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

        "purge bot [AMOUNT]" : f"Purges the given amount of messages if the message is by a bot."\
        f"\nExample : ```{PREFIX}purge bot 100```",

        "purge human [AMOUNT]" : f"Purges the given amount of messages if the message is by a human."\
        f"\nExample : ```{PREFIX}purge human 100```",

        "purge user [USER] [AMOUNT]" : f"Purges the given amount of messages if the message is by the user provided."\
        f"\nExample : ```{PREFIX}purge user {TEST_ACCOUNT} 100```",

        "purge embeds [AMOUNT]" : f"Purges the given amount of messages if it contains any embeds."\
        f"\nExample : ```{PREFIX}purge embeds 100```",

        "purge images [AMOUNT]" : f"Purges the given amount of messages if it contains any attachments."\
        f"\nExample : ```{PREFIX}purge images 100```",

        "purge mentions [AMOUNT]" : f"Purges the given amount of messages if it contains any role or user mentions."\
        f"\nExample : ```{PREFIX}purge mentions 100```",

        "purge links [AMOUNT]" : f"Purges the given amount of messages if it contains any links."\
        f"\nExample : ```{PREFIX}purge links 100```"
    },

    "av" : {
        "av" : f"See your profile picture.\nExample : ```{PREFIX}av```",
        "av [USER]" : f"See a user's profile picture.\nExample : ```{PREFIX} {TEST_ACCOUNT}```"
    }
}

# Server Specific constants
SERVER_ID = 722336877524418620

ROLE_IDS = {

    "MUTE_ROLE_ID" : 722386628064182302,
    "REAL_SAIMAN" : 722395258209697802,
    "OWNER" : 722337186694955079,
    "TECHNIKAL" : 730045629572579348,
    "MODS" : 751326081159790682,
    "MODS_PERMS" : 722337381553799199,
    "SERVER_BOOSTERS" : 742429114463682705,
    "#1" : 722417503963447297,
    "TRUSTED" : 749312230843220049,
    "T_SERIES" : 722397327566045235,
    "DENK" : 722397252387209216,
    "Paraud_Bhendi_Eater" : 722397166060175401,
    "Lenovo_Ghoda_Owner" : 722397076637351973,
    "CHALLENGE_WINNER" :  722701607438909451,
    "CONTRIBUTOR" : 735083796910833685,
    "MONKE_GANG" : 722343355480014929,
    "ONE_SIDED_LOVER" : 722346295884382249,
    "BUTTON_CHOR" : 722351250326290453,
    "SAY_SENA" : 722338517329641493,
    "EDGY_PASS" : 730466271027789856
}
