import random


class MessageType:
    def __init__(self, typ, mwssage):
        self.typ = typ
        self.message = mwssage

    # klasa rozkminiająca co tak naprawdę ma zrobić bot i co ma zwrócić


class Watson:
    def __init__(self, message):
        self.type = None
        self.action = None
        self.message = message.content
        self.author = message.author
        self.channel = message.channel

    async def find(self):
        casper_id = '<@!853645195802181672>'  # id caspra

        if f'{casper_id} test' == self.message:
            return '👻'

        if f'{casper_id} message' in self.message:
            return self.message

        if f'{casper_id} rzuć kością' == self.message:
            return random.choice(range(1, 6))

        if f'{casper_id} kto jest najlepszym programistą?' == self.message:
            return 'Kacper \U0001F61B'
