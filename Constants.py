import os

# TOKENS
BOT_TOKEN = os.getenv("BOT_TOKEN")
DREAMLO_URL = os.getenv("DREAMLO_URL")
REDDIT_KEY = os.getenv("REDDIT_KEY")
REDDIT_SECRET = os.getenv("REDDIT_SECRET")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

PREFIX = "="
DEVS_IDS = [669861531034583060]
ALL_EXTENSIONS = ["_help", "ban", "kick", "mute_unmute", "purge", "unban", "av", "insult", "config",
            "report", "welcome_goodbye", "reddit_memes", "member_count", "deleted_edited", "counters",
            "random_replies"]

SOURCE_URL = "https://github.com/nikhilvayeda/bhendi-bot-3"

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
            "kick" : f"Kicks a member from the server.\nUse : ```{PREFIX}kick [USER]```",
            "purge" : "Purges messages.\nUser `=help purge` to see a full help."
        },

    "Utility" :
        {
            "av" : f"See your or a user's profile picture.\nUse : ```{PREFIX}av```\n"\
            f"or use : ```{PREFIX}av [USER]```",
            "report" : f"Report something to the moderators.\nUse ```{PREFIX}report [CONTEXT]```",
            "edited" : f"See that last 5 edited messages.\nUse : ```{PREFIX}edited``` ( Mods only )",
            "deleted" : f"See the last 5 deleted messages.\nUse : ```{PREFIX}deleted``` ( Mods only )"
        },

    "config" :
        {
            "all_channels" : "To see all the channel name with their IDs",
            "all_roles" : "To see all the role name with their IDs",
            "all_emojis" : "To see all the emojis with their IDs",
            "all_cogs" : "To see all the cogs present"
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
        "unban [USER]" : f"Unbans a banned member.\nExample : ```{PREFIX}unban {TEST_ACCOUNT[1:]}```"
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

    "report" : {
        "report" : f"Report something to the moderators.\nUse ```{PREFIX}report [CONTEXT]```"
    },

    "av" : {
        "av" : f"See your profile picture.\nExample : ```{PREFIX}av```",
        "av [USER]" : f"See a user's profile picture.\nExample : ```{PREFIX} {TEST_ACCOUNT}```"
    },

    "edited" : {
        "edited" : f"See that last 5 edited messages.\nUse : ```{PREFIX}edited``` ( Mods only )"
    },

    "deleted" : {
        "deleted" : f"See the last 5 deleted messages.\nUse : ```{PREFIX}deleted``` ( Mods only )"
    }
}

RANDOM_REPLIES = {

    "fuck haters" : "Ab Saiman ki baari hai",
    "yalgaar hoe" : "Hoes mad :flushed:",
    "carry tera baap hai" : "Ok mom",
    "carry sabka baap hai" : "Ok mom",
    "curry bhoi tera baap hai" : "Ok mom",
    "keri tera baap hai" : "Ok mom",
    "curry tera baap hai" : "Ok mom",
    "six" : "Teri shaadi fix :joy:",
    "pencil" : "Teri shaadi cancel :joy:",
    "ok mom" : "Wait thats illegal",
    "i wanna kill myself" : "**Dont do it you have more to accomplish suicide help line India 091529 87821**",
    "chief" : "He died :pensive:",
    "monke" : "He died :pensive:"
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

CHANNEL_IDS = {
    "MEMES" : 738268425511501874,
    "COMMANDS" : 738637064740012043,
    "CHALLENGES" : 738284054352232498,
    "SUGGESTIONS" : 748074647592894545,
    "WELCOME_GOODBYE" : 738264222387142697,
    "MUSIC_2" : 722356472008147186,
    "NO_RULES_CHAT" : 738777775225176064,
    "PICTURES" : 753771880196079637,
    "SUBSCRIBERS" : 730396610030469130,
    "CREATIVITY" : 753771693603815444,
    "SELF_PROMO" : 738710818937503745,
    "MEMBER_LOG" : 752906631368409088,
    "BOT" : 738284995818422313,
    "MEDIA_SUGGESTIONS" : 748078525931585546,
    "REPORTS" : 755738027929894983,
    "CRITICISMS" : 757658686507319517,
    "ROAST" : 743068962148974663,
    "GENERAL" : 722356890205683725,
    "BADE_LOG" : 738279954109693984,
    "TESTING" : 762242298662617131,
    "MOD_LOG" : 755372674116485160,
    "MESSAGE_LOG" : 752906630324289556,
    "MEMBERS" : 738664927853805608,
    "RULES" : 738264521784950784,
    "SPAM" : 756457192550301726,
    "ANNOUCEMENTS" : 738264759505518643,
    "SERVER_LOG" : 752906631796228126,
    "STARBOARD" : 752230707836747858,
    "SUGGESTION_STATUS" : 748233654794453032,
    "BHENDI_LOGS" : 741837952723714180,
    "GENERAL" : 738265340718350377,
    "REDDIT_MEMES" : 738272583165935706,
    "MUSIC_1" : 722346516962082858,
    "VOICE_CHANNELS" : 722356853253865513,
    "SAIMAN_DISCUSSIONS" : 757658282805428295,
    "SAIMAN_TALKS" : 757658348156878900,
    "FAN_ART" : 757658405191024721
}
