import random


# klasa rozkminiająca co tak naprawdę ma zrobić bot i co ma zwrócić
class Gutenberg:
    @staticmethod
    def on_message(message):
        casper_id = '<@!853645195802181672>'  # id caspra
        msg = message.content.lower()

        if f'{casper_id} test' == msg:
            return '👻'

        if f'{casper_id} message' in msg:
            return message

        if f'{casper_id} rzuć kością' == msg:
            return random.choice(range(1, 6))

        if f'{casper_id} kto jest najlepszym programistą?' == msg:
            return 'Kacper \U0001F61B'
