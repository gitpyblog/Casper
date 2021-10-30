import random


# klasa rozkminiająca co tak naprawdę ma zrobić bot i co ma zwrócić
class Gutenberg:
    @staticmethod
    def on_message(message):
        casper_id = '<@!853645195802181672>'  # id caspra

        if f'{casper_id} test' == message.content.lower():
            return '👻'

        if f'{casper_id} message' in message.content.lower():
            return message

        if f'{casper_id} rzuć kością' == message.content.lower():
            return random.choice(range(1, 6))

        if f'{casper_id} kto jest najlepszym programistą?' == message.content.lower():
            return 'Kacper \U0001F61B'
