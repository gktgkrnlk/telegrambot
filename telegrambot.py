from telegram import Updater , InLineQueryHandler , CommandHandler
import requests
import re
def get_url():
    contents = requests.get("https://random.dog/woof.json").json()
    url = contents['url']
    return url

def bop(bot, update):
    url = get_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat__id, photo=url)

def main():
    updater = Updater('YOUR_TOKEN')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_pulling()
    updater.idle()

if_name__ == '__main__'
main()
