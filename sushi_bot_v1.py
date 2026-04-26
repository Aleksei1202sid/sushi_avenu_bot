import logging
import os
import sys

from telebot import TeleBot, types
from dotenv import load_dotenv


load_dotenv()

# Взяли переменную TOKEN из пространства переменных окружения:
secret_token = os.getenv('TOKEN')
bot = TeleBot(token=secret_token)

logger = logging.getLogger(__name__)

logging.basicConfig(
        format='%(asctime)s; %(levelname)s; '
        '%(funcName)s; %(lineno)d; %(message)s',
        level=logging.DEBUG,
        handlers=[logging.StreamHandler(sys.stdout)]
    )

# Главное меню
main_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.row(
    types.KeyboardButton('роллы'),
    types.KeyboardButton('маки'),
    types.KeyboardButton('суши'),
)
# Меню "роллы"
rolls_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
rolls_menu.add(types.KeyboardButton('Филадельфия люкс (4 шт)'))
rolls_menu.add(types.KeyboardButton('Опаленый лосось'))
rolls_menu.add(types.KeyboardButton('Чикаго ролл'))
rolls_menu.add(types.KeyboardButton('Назад в главное меню'))

# Меню "маки"
maki_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
maki_menu.add(types.KeyboardButton('Маки огурец'))
maki_menu.add(types.KeyboardButton('Маки чукка'))
maki_menu.add(types.KeyboardButton('Маки авокадо'))
maki_menu.add(types.KeyboardButton('Назад в главное меню'))

# Меню "суши"
sushi_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
sushi_menu.add(types.KeyboardButton('Суши с тунцом'))
sushi_menu.add(types.KeyboardButton('Суши с угрем'))
sushi_menu.add(types.KeyboardButton('Суши с лососем'))
sushi_menu.add(types.KeyboardButton('Назад в главное меню'))


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(
        message.chat.id,
        'Выберите категорию:',
        reply_markup=main_menu
    )


@bot.message_handler(func=lambda message: True)
def handle_menu(message):
    text = message.text.lower()
    if text == 'роллы':
        bot.send_message(
            message.chat.id,
            'Выберите роллы:',
            reply_markup=rolls_menu
        )
    elif text == 'маки':
        bot.send_message(
            message.chat.id,
            'Выберите маки:',
            reply_markup=maki_menu
        )
    elif text == 'суши':
        bot.send_message(
            message.chat.id,
            'Выберите суши:',
            reply_markup=sushi_menu
        )
    elif text == 'филадельфия люкс (4 шт)':
        photo_url = (
            'https://sushiav.ru//test//tproduct//'
            '518177776-530979368792-filadelfiya-lyuks-4-sht'
        )
        # with open(photo_path, 'rb') as photo:
        bot.send_photo(message.chat.id, photo=photo_url)
        bot.send_message(
            message.chat.id, (
              'Описание тех карты Филадельфия люкс (4 шт):\n'
              'японский рис,\n'
              'лосось ,\n'
              'водоросли нори,\n'
              'сыр творожный Cremette.',
            ),
            reply_markup=rolls_menu
        )
    elif text == 'опаленый лосось':
        photo_url = (
            'https://sushiav.ru//test//tproduct/'
            '518177776-847122351832-opalennii-losos'
        )
        # with open(photo_path, 'rb') as photo:
        bot.send_photo(message.chat.id, photo=photo_url)
        bot.send_message(
            message.chat.id, (
              'Описание тех карты Опаленый лосось:\n'
              'японский рис,\n'
              'лосось опаленый ,\n'
              'спайси соус ,\n'
              'унаги соус ,\n'
              'огурец ,\n'
              'авокадо,\n'
              'сыр Филадельфия.',
            ),
            reply_markup=rolls_menu
        )
    elif text == 'чикаго ролл':
        photo_url = (
            'https://sushiav.ru//newmenu//tproduct/'
            '500778547-421451143681-chikago-roll-new'
        )
        # with open(photo_path, 'rb') as photo:
        bot.send_photo(message.chat.id, photo=photo_url)
        bot.send_message(
            message.chat.id, (
              'Описание тех карты Чмкаго ролл:\n'
              'японский рис,\n'
              'тигровые креветки темпура,\n'
              'снежный краб спайси,\n'
              'васаби сливочный соус (сладко-острый),\n'
              'огурец,\n'
              'икра масаго,\n'
              'авокадо,\n'
              'сыр сливочный.',
            ),
            reply_markup=rolls_menu
        )
    elif text == 'маки огурец':
        photo_url = (
            'https://sushiav.ru//maki//tproduct//'
            '500784044-997210585301-maki-ogurets'
        )
        # with open(photo_path, 'rb') as photo:
        bot.send_photo(message.chat.id, photo=photo_url)
        bot.send_message(
            message.chat.id, (
              'Описание тех карты Маки огурец:\n'
              'японский рис,\n'
              'огурец,\n'
              'кунжут.',
            ),
            reply_markup=maki_menu
        )
    elif text == 'маки чукка':
        photo_url = (
            'https://sushiav.ru//maki//tproduct//'
            '500784044-774516500101-maki-chukka'
        )
        # with open(photo_path, 'rb') as photo:
        bot.send_photo(message.chat.id, photo=photo_url)
        bot.send_message(
            message.chat.id, (
              'Описание тех карты Маки чукка:\n'
              'японский рис,\n'
              'водоросли чукка.',
            ),
            reply_markup=maki_menu
        )
    elif text == 'маки авокадо':
        photo_url = (
            'https://sushiav.ru//maki//tproduct//'
            '500784044-385082516191-maki-avokado'
        )
        # with open(photo_path, 'rb') as photo:
        bot.send_photo(message.chat.id, photo=photo_url)
        bot.send_message(
            message.chat.id, (
              'Описание тех карты Маки авокадо:\n'
              'японский рис,\n'
              'авокадо.',
            ),
            reply_markup=maki_menu
        )
    elif text == 'суши с тунцом':
        photo_url = (
            'https://sushiav.ru//sushi//tproduct//'
            '500785053-389202040571-sushi-s-tuntsom'
        )
        # with open(photo_path, 'rb') as photo:
        bot.send_photo(message.chat.id, photo=photo_url)
        bot.send_message(
            message.chat.id, (
              'Описание тех карты Суши с тунцом:\n'
              'японский рис,\n'
              'тунец.',
            ),
            reply_markup=sushi_menu
        )
    elif text == 'суши с угрем':
        photo_url = (
            'https://sushiav.ru/sushi/tproduct/'
            '500785053-176204096911-sushi-s-ugrem'
        )
        # with open(photo_path, 'rb') as photo:
        bot.send_photo(message.chat.id, photo=photo_url)
        bot.send_message(
            message.chat.id, (
              'Описание тех карты Суши с угрем:\n'
              'японский рис,\n'
              'угорь.',
            ),
            reply_markup=sushi_menu
        )
    elif text == 'суши с лососем':
        photo_url = (
            'https://sushiav.ru/sushi/tproduct/'
            '500785053-213385830261-sushi-s-lososem'
        )
        # with open(photo_path, 'rb') as photo:
        bot.send_photo(message.chat.id, photo=photo_url)
        bot.send_message(
            message.chat.id, (
              'Описание тех карты Суши с лососем:\n'
              'японский рис,\n'
              'лосось.',
            ),
            reply_markup=sushi_menu
        )
    elif text == 'назад в главное меню':
        bot.send_message(
            message.chat.id,
            'Возврат в главное меню.',
            reply_markup=main_menu
        )
    else:
        bot.send_message(
            message.chat.id,
            'Пожалуйста, выберите опцию с клавиатуры.',
            reply_markup=main_menu
        )


def main():
    try:
        bot.polling()
    except Exception as e:
        logger.error('Произошла ошибка при запуске бота: %s', type(e).__name__)


if __name__ == '__main__':
    main()
