from EmiliaAnimeBot import dispatcher

from telegram import ParseMode, Update
from telegram.ext import CommandHandler, CallbackContext
from telegram.ext.dispatcher import  run_async

GIT_PIC = "https://telegra.ph/file/c5666c010f3ccc267719d.jpg"

GIT_TEXT = """
@boytapibot By @fl0werboy

*Contributors/Credits*

✨Special thanks✨
🔥 [IzumiCypherX]
🔥 [Nautilus]
🔥 [Kaneki]
🔥 [Paul-Larsen]
🔥 [TheHamkerCat]
🔥 [@Xflicks]
__________________________________
[Repository](https://www.xnxx.com)
[Support](https://t.me/cariteman_mutual)
[Instagram](https://www.instagram.com/ariiiiav)

"""

@run_async
def repo(update: Update, context: CallbackContext):
    update.effective_message.reply_photo(
        GIT_PIC,
        caption = GIT_TEXT,
        parse_mode=ParseMode.MARKDOWN
        )

REPO_HANDLER = CommandHandler("repo", repo)

dispatcher.add_handler(REPO_HANDLER)
