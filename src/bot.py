from __future__ import unicode_literals

from telegram.ext import Updater, CommandHandler


class MyBot:
    def __init__(self, name, api_key, callbackA=None, callbackB=None):
        self.name = name
        self.api_key = api_key
        self.callbackA = callbackA
        self.callbackB = callbackB

    def handlerA(self, update, context):
        chat_id = update.effective_chat.id

        if self.callbackA is not None:
            self.callbackA(update, context)

        reply_text = 'Handler A completed'
        return context.bot.send_message(
            chat_id=chat_id,
            text=reply_text)

    def handlerB(self, update, context):
        chat_id = update.effective_chat.id

        if self.callbackB is not None:
            self.callbackB(update, context)

        reply_text = 'Handler B completed'
        return context.bot.send_message(
            chat_id=chat_id,
            text=reply_text)

    def initiate(self):
        self.updater = Updater(self.api_key, use_context=True)
        self.updater.dispatcher.add_handler(
            CommandHandler('commandA', self.handlerA))
        self.updater.dispatcher.add_handler(
            CommandHandler('commandB', self.handlerB))

    def run(self):
        self.updater.start_polling()
        self.updater.idle()


