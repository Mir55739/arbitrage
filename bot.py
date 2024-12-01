from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ConversationHandler, Updater, CommandHandler, MessageHandler, CallbackQueryHandler, Filters
from common import allowed_chat_ids, chat_settings, blacklist, start
from handle_message import handle_message


def button(update: Update, context):
    query = update.callback_query
    chat_id = query.message.chat_id
    query.answer()

    # Получение настроек для текущего чата
    settings = chat_settings.get(chat_id, {
        'bitget_buy_enabled': False,
        'bitget_sell_enabled': False,
        'bitmart_buy_enabled': False,
        'bitmart_sell_enabled': False,
        'mexc_buy_enabled': False,
        'mexc_sell_enabled': False,
        'binance_buy_enabled': False,
        'binance_sell_enabled': False,
        'gate_buy_enabled': False,
        'gate_sell_enabled': False,
        'huobi_buy_enabled': False,
        'huobi_sell_enabled': False,
        'kucoin_buy_enabled': False,
        'kucoin_sell_enabled': False,
    })
    if query.data == '1':
        settings['bitmart_buy_enabled'] = not settings['bitmart_buy_enabled']
    elif query.data == '2':
        settings['bitmart_sell_enabled'] = not settings['bitmart_sell_enabled']
    elif query.data == '3':
        settings['mexc_buy_enabled'] = not settings['mexc_buy_enabled']
    elif query.data == '4':
        settings['mexc_sell_enabled'] = not settings['mexc_sell_enabled']
    elif query.data == '5':
        settings['binance_buy_enabled'] = not settings['binance_buy_enabled']
    elif query.data == '6':
        settings['binance_sell_enabled'] = not settings['binance_sell_enabled']
    elif query.data == '7':
        settings['bitget_buy_enabled'] = not settings['bitget_buy_enabled']
    elif query.data == '8':
        settings['bitget_sell_enabled'] = not settings['bitget_sell_enabled']
    elif query.data == '9':
        settings['gate_buy_enabled'] = not settings['gate_buy_enabled']
    elif query.data == '10':
        settings['gate_sell_enabled'] = not settings['gate_sell_enabled']
    elif query.data == '11':
        settings['huobi_buy_enabled'] = not settings['huobi_buy_enabled']
    elif query.data == '12':
        settings['huobi_sell_enabled'] = not settings['huobi_sell_enabled']
    elif query.data == '13':
        settings['kucoin_buy_enabled'] = not settings['kucoin_buy_enabled']
    elif query.data == '14':
        settings['kucoin_sell_enabled'] = not settings['kucoin_sell_enabled']
    # Сохранение обновленных настроек для текущего чата
    chat_settings[chat_id] = settings

    keyboard = [
        [InlineKeyboardButton(f"Bitmart buy {'✅' if settings['bitmart_buy_enabled'] else ''}", callback_data='1'),
         InlineKeyboardButton(f"Bitmart Sell {'✅' if settings['bitmart_sell_enabled'] else ''}", callback_data='2')],
        [InlineKeyboardButton(f"Mexc buy {'✅' if settings['mexc_buy_enabled'] else ''}", callback_data='3'),
         InlineKeyboardButton(f"Mexc Sell {'✅' if settings['mexc_sell_enabled'] else ''}", callback_data='4')],
        [InlineKeyboardButton(f"Binance buy {'✅' if settings['binance_buy_enabled'] else ''}", callback_data='5'),
         InlineKeyboardButton(f"Binance Sell {'✅' if settings['binance_sell_enabled'] else ''}", callback_data='6')],
        [InlineKeyboardButton(f"Bitget buy {'✅' if settings['bitget_buy_enabled'] else ''}", callback_data='7'),
         InlineKeyboardButton(f"Bitget Sell {'✅' if settings['bitget_sell_enabled'] else ''}", callback_data='8')],
        [InlineKeyboardButton(f"Gate buy {'✅' if settings['gate_buy_enabled'] else ''}", callback_data='9'),
         InlineKeyboardButton(f"Gate Sell {'✅' if settings['gate_sell_enabled'] else ''}", callback_data='10')],
        [InlineKeyboardButton(f"Huobi buy {'✅' if settings['huobi_buy_enabled'] else ''}", callback_data='11'),
         InlineKeyboardButton(f"Huobi Sell {'✅' if settings['huobi_sell_enabled'] else ''}", callback_data='12')],
        [InlineKeyboardButton(f"Kucoin buy {'✅' if settings['kucoin_buy_enabled'] else ''}", callback_data='13'),
         InlineKeyboardButton(f"Kucoin Sell {'✅' if settings['kucoin_sell_enabled'] else ''}", callback_data='14')]

    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.edit_message_text(chat_id=chat_id, message_id=query.message.message_id,
                                  text="Выберите опцию:", reply_markup=reply_markup)


def main():

    updater = Updater("6113015383:AAF9bG_Fi6djX_p30GCEEIUKsrJ4Ac4gtPQ")
    job_queue = updater.job_queue
    #job_queue.run_repeating(update_data, interval=10)
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(MessageHandler(
        Filters.text & ~Filters.command, handle_message))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
