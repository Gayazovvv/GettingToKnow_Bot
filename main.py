import telebot
from info import character_description, contacts

bot = telebot.TeleBot("6760083375:AAEi1PKD10xe48k9xGX_sIqtMUCoYrCRvAU")


# /start command
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id,
                     "Привет, меня зовут Булат. На данный момент я учусь программировать на Python.\n"
                     "Введи /help чтобы посмотреть дополнительные команды.")


# /help command
@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, "Это бот-визитка, он нужен мне,\nчтоб пользователь знал - с кем имеет дело.\n"
                                      f"1. Посмотреть краткую информацию: /about\n"
                                      f"2. Мои контакты: /contacts\n"
                                      f"3. Мои хобби и развлечения: /hobby\n"
                                      f"4. Так же бот умеет распознавать сообщения 'привет' и 'покаn\n"
                                      f"5. Бот может распознавать картинки, видео\n"
                                      f"6. У бота есть 'секретное слово', угадайте 'секретное слово'\n"
                                      f"И бот выдаст секретную картинку скибиди-котиков\n"
                                      f"Подсказка: 'секретное слово'")


def filter_car(message):
    return "секретное слово" in message.text.lower()


@bot.message_handler(func=filter_car)
def send_secret_photo(message):
    # send photo
    photo = open('kandinsky-download-1702410706948 (1).png', 'rb')
    bot.send_photo(message.chat.id, photo)


# /about command
@bot.message_handler(commands=["about"])
def about(message):
    bot.send_message(message.chat.id, f'Моя краткая информация:\n'
                                      f'Меня зовут: {character_description["name"]}\n'
                                      f'Мне столько лет: {character_description["age"]}\n'
                                      f'Тут я живу: {character_description["city"]}\n'
                                      f'Тут я учусь: {character_description["study"]}\n'
                                      f'Остальные вопросы я жду от тебя на моей почте')


# answer for /contacts
@bot.message_handler(commands=["contacts"])
def contact(message):
    bot.send_message(message.chat.id, "Если вы хотите со мной связаться, вот мои контакты:\n"
                                      f'Моя почта: {contacts["email"]}\n'
                                      f'Мой Telegram: {contacts["Telegram"]}\n'
                                      f'Мой VK: {contacts["VK"]}\n'
                                      f'Мой GitHub: {contacts["GIT"]}')


# answer for /hobby
@bot.message_handler(commands=["hobby"])
def hobbys(message):
    bot.send_message(message.chat.id, "Я люблю играть в компьютерные игры, шахматы, шашки.\n"
                                      "Так же я люблю кататься на мотоцикле. ")


# filter for word "привет"
def filter_hello(message):
    return "привет" in message.text.lower()


@bot.message_handler(func=filter_hello)
def hello_handler(message):
    bot.send_message(message.chat.id, "Привет")


# filter for word "пока"
def filter_bye(message):
    return "пока" in message.text.lower()


@bot.message_handler(func=filter_bye)
def bye_filter(message):
    bot.send_message(message.chat.id, "Пока")


# answer for text
@bot.message_handler(content_types=['text'])
def text(message):
    bot.send_message(message.chat.id, f"Вы напечатали {message.text}")


# answer for photo
@bot.message_handler(content_types=["photo"])
def photo(message):
    bot.send_message(message.chat.id, f"Классная фотография, {message.from_user.first_name}")


# answer for sticker
@bot.message_handler(content_types=["sticker"])
def stick(message):
    bot.send_message(message.chat.id, f"Классный стикер, {message.from_user.first_name}")


# answer for pin message
@bot.message_handler(content_types=["pinned_message"])
def pin_message(message):
    bot.send_message(message.chat.id, "Ты закрепил сообщение в боте? Интересно...")


# answer for audio
@bot.message_handler(content_types=["audio"])
def audio(message):
    bot.send_message(message.chat.id, f"К сожалению я пока не могу прослушать аудио, но я обязательно научусь!")


# answer for video
@bot.message_handler(content_types=["video"])
def video(message):
    bot.send_message(message.chat.id, f"К сожалению я пока не могу обработать видео, но я обязательно научусь!")


bot.polling(none_stop=True)
