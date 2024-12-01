from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from Mexc import send_profit27_messages, send_profit26_messages, send_profit25_messages, send_profit24_messages, send_profit23_messages, send_profit21_messages, get_ticker_data2, get_prices_mexc
from BitMart import send_profit17_messages, send_profit16_messages, send_profit15_messages, send_profit14_messages, send_profit13_messages, send_profit12_messages, get_ticker_data, get_prices_bitmart
from Binance import send_profit37_messages, send_profit36_messages, send_profit35_messages, send_profit34_messages, send_profit31_messages, send_profit32_messages, get_ticker_data3, get_prices_binance
from Bitget import send_profit47_messages, send_profit46_messages, send_profit45_messages, send_profit43_messages, send_profit42_messages, send_profit41_messages, get_ticker_data43, get_prices_bitget
from Gate import send_profit57_messages, send_profit56_messages, send_profit51_messages, send_profit52_messages, send_profit53_messages, send_profit54_messages, get_ticker_data5, get_prices_gate
from Huobi.Huobi import send_profit67_messages, send_profit65_messages, send_profit64_messages, send_profit63_messages, send_profit62_messages, send_profit61_messages, get_prices_huobi, get_ticker_data6
from Kucoin import send_profit76_messages, send_profit75_messages, send_profit74_messages, send_profit73_messages, send_profit72_messages, send_profit71_messages, get_ticker_data7, get_prices_kucoin
from common import start, allowed_chat_ids, chat_settings, current_state, ADD_TO_BLACKLIST, REMOVE_FROM_BLACKLIST, blacklist
from telegram.ext import ConversationHandler
# Импорт переменных из основного скрипта
api_key = "e2ce0607ec00afed2176c7e8e9eb6b25d4fd921b"
secret_key = "a8ba97b8fd1cb5393a25812fefa82c0171871474d9dbdae5e6e5bc573421e5b2"
memo = "Your Memo"


def handle_message(update: Update, context):
    global current_state
    text = update.message.text
    chat_id = update.message.chat_id

    # Проверка, является ли текущий чат разрешенным
    if chat_id not in allowed_chat_ids:
        # Не отвечать на сообщения из неразрешенного чата
        return

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

    if text == 'Биржи':
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
        update.message.reply_text('Выберите опцию:', reply_markup=reply_markup)

    elif text == 'Спред':
        ticker_data = get_ticker_data()
        ticker_data2 = get_ticker_data2()
        ticker_data3 = get_ticker_data3()
        ticker_data43 = get_ticker_data43()
        ticker_data5 = get_ticker_data5()
        ticker_data6 = get_ticker_data6()
        ticker_data7 = get_ticker_data7()
 ##########################################
        ask_prices_bitmart, bid_prices_bitmart, ask_prices_bitmart1, bid_prices_bitmart1 = get_prices_bitmart(
            ticker_data)
        ask_prices_mexc, bid_prices_mexc, ask_prices_mexc1, bid_prices_mexc1 = get_prices_mexc(
            ticker_data2)
        ask_prices_binance, bid_prices_binance = get_prices_binance(
            ticker_data3)
        ask_prices_bitget, bid_prices_bitget = get_prices_bitget(ticker_data43)
        ask_prices_gate, bid_prices_gate, ask_prices_gate1, bid_prices_gate1 = get_prices_gate(
            ticker_data5)
        ask_prices_huobi, bid_prices_huobi = get_prices_huobi(ticker_data6)
        ask_prices_kucoin, bid_prices_kucoin, ask_prices_kucoin1, bid_prices_kucoin1 = get_prices_kucoin(
            ticker_data7)
        #################################################
        # Фильтрация символов из черного списка
        ask_prices_bitmart = {
            k: v for k, v in ask_prices_bitmart.items() if k not in blacklist}
        bid_prices_bitmart = {
            k: v for k, v in bid_prices_bitmart.items() if k not in blacklist}
        ask_prices_mexc = {k: v for k,
                           v in ask_prices_mexc.items() if k not in blacklist}
        bid_prices_mexc = {k: v for k,
                           v in bid_prices_mexc.items() if k not in blacklist}
        ask_prices_binance = {
            k: v for k, v in ask_prices_binance.items() if k not in blacklist}
        bid_prices_binance = {
            k: v for k, v in bid_prices_binance.items() if k not in blacklist}
        ask_prices_bitget = {
            k: v for k, v in ask_prices_bitget.items() if k not in blacklist}
        bid_prices_bitget = {
            k: v for k, v in bid_prices_bitget.items() if k not in blacklist}
        ask_prices_gate = {
            k: v for k, v in ask_prices_gate.items() if k not in blacklist}
        bid_prices_gate = {
            k: v for k, v in bid_prices_gate.items() if k not in blacklist}
        ask_prices_huobi = {
            k: v for k, v in ask_prices_huobi.items() if k not in blacklist}
        bid_prices_huobi = {
            k: v for k, v in bid_prices_huobi.items() if k not in blacklist}
        ask_prices_kucoin = {
            k: v for k, v in ask_prices_kucoin.items() if k not in blacklist}
        bid_prices_kucoin = {
            k: v for k, v in bid_prices_kucoin.items() if k not in blacklist}
    ################################################

        common_symbols = set(ask_prices_bitmart.keys()
                             ) & set(ask_prices_mexc.keys())
        common_symbols1 = set(ask_prices_bitmart1.keys()
                              ) & set(ask_prices_binance.keys())
        common_symbols2 = set(ask_prices_mexc1.keys()
                              ) & set(ask_prices_binance.keys())
        common_symbols41 = set(ask_prices_bitmart1.keys()
                               ) & set(ask_prices_bitget.keys())
        common_symbols24 = set(ask_prices_mexc1.keys()
                               ) & set(ask_prices_bitget.keys())
        common_symbols34 = set(ask_prices_binance.keys()
                               ) & set(ask_prices_bitget.keys())
        common_symbols51 = set(ask_prices_gate.keys()
                               ) & set(ask_prices_bitmart.keys())
        common_symbols52 = set(ask_prices_gate.keys()
                               ) & set(ask_prices_mexc.keys())
        common_symbols53 = set(ask_prices_gate1.keys()
                               ) & set(ask_prices_binance.keys())
        common_symbols54 = set(ask_prices_gate1.keys()
                               ) & set(ask_prices_bitget.keys())
        common_symbols61 = set(ask_prices_huobi.keys()
                               ) & set(ask_prices_bitmart1.keys())
        common_symbols62 = set(ask_prices_huobi.keys()
                               ) & set(ask_prices_mexc1.keys())
        common_symbols63 = set(ask_prices_huobi.keys()
                               ) & set(ask_prices_binance.keys())
        common_symbols64 = set(ask_prices_huobi.keys()
                               ) & set(ask_prices_bitget.keys())
        common_symbols65 = set(ask_prices_huobi.keys()
                               ) & set(ask_prices_gate1.keys())
        common_symbols71 = set(ask_prices_kucoin1.keys()
                               ) & set(ask_prices_bitmart1.keys())
        common_symbols72 = set(ask_prices_kucoin1.keys()
                               ) & set(ask_prices_mexc1.keys())
        common_symbols73 = set(ask_prices_kucoin1.keys()
                               ) & set(ask_prices_binance.keys())
        common_symbols74 = set(ask_prices_kucoin1.keys()
                               ) & set(ask_prices_bitget.keys())
        common_symbols75 = set(ask_prices_kucoin1.keys()
                               ) & set(ask_prices_gate1.keys())
        common_symbols76 = set(ask_prices_kucoin1.keys()
                               ) & set(ask_prices_huobi.keys())
        ###############################################
        if settings['bitmart_buy_enabled'] and settings['mexc_sell_enabled']:
            send_profit12_messages(update, common_symbols, ask_prices_bitmart,
                                   bid_prices_mexc, api_key, secret_key, memo)
        elif settings['bitmart_buy_enabled'] and settings['binance_sell_enabled']:
            send_profit13_messages(update, common_symbols1, ask_prices_bitmart1,
                                   bid_prices_binance, api_key, secret_key, memo)
        elif settings['bitmart_buy_enabled'] and settings['bitget_sell_enabled']:
            send_profit14_messages(update, common_symbols41, ask_prices_bitmart1,
                                   bid_prices_bitget, api_key, secret_key, memo)
        elif settings['bitmart_buy_enabled'] and settings['gate_sell_enabled']:
            send_profit15_messages(
                update, common_symbols51, ask_prices_bitmart, bid_prices_gate, api_key, secret_key, memo)
        elif settings['bitmart_buy_enabled'] and settings['huobi_sell_enabled']:
            send_profit16_messages(
                update, common_symbols61, ask_prices_bitmart1, bid_prices_huobi, api_key, secret_key, memo)
        elif settings['bitmart_buy_enabled'] and settings['kucoin_sell_enabled']:
            send_profit17_messages(update, common_symbols71, ask_prices_bitmart1,
                                   bid_prices_kucoin, api_key, secret_key, memo)
        elif settings['mexc_buy_enabled'] and settings['bitmart_sell_enabled']:
            send_profit21_messages(update, common_symbols,
                                   ask_prices_mexc, bid_prices_bitmart)
        elif settings['mexc_buy_enabled'] and settings['binance_sell_enabled']:
            send_profit23_messages(
                update, common_symbols2, ask_prices_mexc1, bid_prices_binance)
        elif settings['mexc_buy_enabled'] and settings['bitget_sell_enabled']:
            send_profit24_messages(
                update, common_symbols24, ask_prices_mexc1, bid_prices_bitget)
        elif settings['mexc_buy_enabled'] and settings['gate_sell_enabled']:
            send_profit25_messages(
                update, common_symbols52, ask_prices_mexc, bid_prices_gate)
        elif settings['mexc_buy_enabled'] and settings['huobi_sell_enabled']:
            send_profit26_messages(
                update, common_symbols62, ask_prices_mexc1, bid_prices_huobi)
        elif settings['mexc_buy_enabled'] and settings['kucoin_sell_enabled']:
            send_profit27_messages(
                update, common_symbols72, ask_prices_mexc1, bid_prices_kucoin1)
        elif settings['binance_buy_enabled'] and settings['bitmart_sell_enabled']:
            send_profit31_messages(update, common_symbols1,
                                   ask_prices_binance, bid_prices_bitmart1)
        elif settings['binance_buy_enabled'] and settings['gate_sell_enabled']:
            send_profit35_messages(
                update, common_symbols53, ask_prices_binance, bid_prices_gate1)
        elif settings['binance_buy_enabled'] and settings['mexc_sell_enabled']:
            send_profit32_messages(
                update, common_symbols2, ask_prices_binance, bid_prices_mexc1)
        elif settings['binance_buy_enabled'] and settings['bitget_sell_enabled']:
            send_profit34_messages(
                update, common_symbols34, ask_prices_binance, bid_prices_bitget)
        elif settings['binance_buy_enabled'] and settings['huobi_sell_enabled']:
            send_profit36_messages(
                update, common_symbols63, ask_prices_binance, bid_prices_huobi)
        elif settings['binance_buy_enabled'] and settings['kucoin_sell_enabled']:
            send_profit37_messages(
                update, common_symbols73, ask_prices_binance, bid_prices_kucoin1)
        elif settings['bitget_buy_enabled'] and settings['bitmart_sell_enabled']:
            send_profit41_messages(
                update, common_symbols41, ask_prices_bitget, bid_prices_bitmart1)
        elif settings['bitget_buy_enabled'] and settings['mexc_sell_enabled']:
            send_profit42_messages(
                update, common_symbols24, ask_prices_bitget, bid_prices_mexc1)
        elif settings['bitget_buy_enabled'] and settings['binance_sell_enabled']:
            send_profit43_messages(
                update, common_symbols34, ask_prices_bitget, bid_prices_binance)
        elif settings['bitget_buy_enabled'] and settings['gate_sell_enabled']:
            send_profit45_messages(
                update, common_symbols54, ask_prices_bitget, bid_prices_gate1)
        elif settings['bitget_buy_enabled'] and settings['huobi_sell_enabled']:
            send_profit46_messages(
                update, common_symbols64, ask_prices_bitget, bid_prices_huobi)
        elif settings['bitget_buy_enabled'] and settings['kucoin_sell_enabled']:
            send_profit47_messages(
                update, common_symbols74, ask_prices_bitget, bid_prices_kucoin1)
        elif settings['gate_buy_enabled'] and settings['bitmart_sell_enabled']:
            send_profit51_messages(
                update, common_symbols51, ask_prices_gate, bid_prices_bitmart)
        elif settings['gate_buy_enabled'] and settings['mexc_sell_enabled']:
            send_profit52_messages(
                update, common_symbols52, ask_prices_gate, bid_prices_mexc)
        elif settings['gate_buy_enabled'] and settings['binance_sell_enabled']:
            send_profit53_messages(
                update, common_symbols53, ask_prices_gate1, bid_prices_binance)
        elif settings['gate_buy_enabled'] and settings['bitget_sell_enabled']:
            send_profit54_messages(
                update, common_symbols54, ask_prices_gate1, bid_prices_bitget)
        elif settings['gate_buy_enabled'] and settings['huobi_sell_enabled']:
            send_profit56_messages(
                update, common_symbols65, ask_prices_gate1, bid_prices_huobi)
        elif settings['gate_buy_enabled'] and settings['kucoin_sell_enabled']:
            send_profit57_messages(
                update, common_symbols75, ask_prices_gate1, bid_prices_kucoin1)
        elif settings['huobi_buy_enabled'] and settings['bitmart_sell_enabled']:
            send_profit61_messages(
                update, common_symbols61, ask_prices_huobi, bid_prices_bitmart1)
        elif settings['huobi_buy_enabled'] and settings['mexc_sell_enabled']:
            send_profit62_messages(
                update, common_symbols62, ask_prices_huobi, bid_prices_mexc1)
        elif settings['huobi_buy_enabled'] and settings['binance_sell_enabled']:
            send_profit63_messages(
                update, common_symbols63, ask_prices_huobi, bid_prices_binance)
        elif settings['huobi_buy_enabled'] and settings['bitget_sell_enabled']:
            send_profit64_messages(
                update, common_symbols64, ask_prices_huobi, bid_prices_bitget)
        elif settings['huobi_buy_enabled'] and settings['gate_sell_enabled']:
            send_profit65_messages(
                update, common_symbols65, ask_prices_huobi, bid_prices_gate1)
        elif settings['huobi_buy_enabled'] and settings['kucoin_sell_enabled']:
            send_profit67_messages(
                update, common_symbols76, ask_prices_huobi, bid_prices_kucoin1)
        elif settings['kucoin_buy_enabled'] and settings['bitmart_sell_enabled']:
            send_profit71_messages(
                update, common_symbols71, ask_prices_kucoin1, bid_prices_bitmart1)
        elif settings['kucoin_buy_enabled'] and settings['mexc_sell_enabled']:
            send_profit72_messages(
                update, common_symbols72, ask_prices_kucoin1, bid_prices_mexc1)
        elif settings['kucoin_buy_enabled'] and settings['binance_sell_enabled']:
            send_profit73_messages(
                update, common_symbols73, ask_prices_kucoin1, bid_prices_binance)
        elif settings['kucoin_buy_enabled'] and settings['bitget_sell_enabled']:
            send_profit74_messages(
                update, common_symbols74, ask_prices_kucoin1, bid_prices_bitget)
        elif settings['kucoin_buy_enabled'] and settings['gate_sell_enabled']:
            send_profit75_messages(
                update, common_symbols75, ask_prices_kucoin1, bid_prices_gate1)
        elif settings['kucoin_buy_enabled'] and settings['huobi_sell_enabled']:
            send_profit76_messages(
                update, common_symbols76, ask_prices_kucoin1, bid_prices_huobi)
        pass

    elif text == 'Черный список':
        if blacklist:
            update.message.reply_text(
                f'Текущий черный список: {", ".join(blacklist)}')
        else:
            update.message.reply_text('Черный список пуст.')

        keyboard = [
            [KeyboardButton("Добавить"), KeyboardButton("Удалить")],
            [KeyboardButton("Возврат")]
        ]
        reply_markup = ReplyKeyboardMarkup(keyboard)
        update.message.reply_text('Выберите опцию:', reply_markup=reply_markup)
    elif text == 'Добавить':
        current_state = ADD_TO_BLACKLIST
        update.message.reply_text(
            'Введите символ для добавления в черный список:', reply_markup=ReplyKeyboardRemove())
    elif text == 'Удалить':
        current_state = REMOVE_FROM_BLACKLIST
        update.message.reply_text(
            'Введите символ для удаления из черного списка:', reply_markup=ReplyKeyboardRemove())
    elif text == 'Возврат':
        current_state = None
        start(update, context)
    elif current_state == ADD_TO_BLACKLIST:
        # Добавляем символ в черный список
        blacklist.append(text)
        update.message.reply_text(f'Символ {text} добавлен в черный список.')
        current_state = None
        # Возвращаемся в меню черного списка
        if blacklist:
            update.message.reply_text(
                f'Текущий черный список: {", ".join(blacklist)}')
        else:
            update.message.reply_text('Черный список пуст.')

        keyboard = [
            [KeyboardButton("Добавить"), KeyboardButton("Удалить")],
            [KeyboardButton("Возврат")]
        ]
        reply_markup = ReplyKeyboardMarkup(keyboard)
        update.message.reply_text('Выберите опцию:', reply_markup=reply_markup)
    elif current_state == REMOVE_FROM_BLACKLIST:
        # Удаляем символ из черного списка
        if text in blacklist:
            blacklist.remove(text)
            update.message.reply_text(
                f'Символ {text} удален из черного списка.')
        else:
            update.message.reply_text(
                f'Символ {text} не найден в черном списке.')
        current_state = None
        # Возвращаемся в меню черного списка
        if blacklist:
            update.message.reply_text(
                f'Текущий черный список: {", ".join(blacklist)}')
        else:
            update.message.reply_text('Черный список пуст.')

        keyboard = [
            [KeyboardButton("Добавить"), KeyboardButton("Удалить")],
            [KeyboardButton("Возврат")]
        ]
        reply_markup = ReplyKeyboardMarkup(keyboard)
        update.message.reply_text('Выберите опцию:', reply_markup=reply_markup)
