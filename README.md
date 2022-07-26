# Customizable behaviour in Python Telegram Bots

## Introduction

This bot has two commands, `/commandA` that prints on the screen `Handler A completed` and `/commandB` that prints `Handler B completed`. The goal is to make this bot customizable so that this behaviour can be extended and one can add some extra tasks before these commands.

Let's make it print `Hey, I am a customized handler A` while command A runs and also `Hey, I am a customized handler B yolo!` when command B runs.

```python
from src.bot import MyBot


def CustomizedA(update, context):
    chat_id = update.effective_chat.id
    reply_text = 'Hey, I am a customized handler A'
    return context.bot.send_message(
        chat_id=chat_id,
        text=reply_text)

def CustomizedB(update, context):
    chat_id = update.effective_chat.id
    reply_text = 'Hey, I am a customized handler B yolo!'
    return context.bot.send_message(
        chat_id=chat_id,
        text=reply_text)


B = MyBot('Bob', '<your API key>',
          callbackA=CustomizedA, callbackB=CustomizedB)
B.initiate()
B.run()
```

## Use case

We are designing a bot to handle GRIN payments as it is specified [here](https://forum.grin.mw/t/telegram-bot-progress-thread-by-renzokuken/9882/11). While working on it we keep getting more ideas about what more this bot could do. From simple tipping bot we arrived at support reward bot and a faucet bot. So why not simply make a GRIN-capable bot that has commands for withdrawal and deposits and allow user to specify the conditions on who can withdraw or deposit to make the logic customizable?
