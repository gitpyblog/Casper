import random


class Message(object):
    author = 'JohanesGutenberg'
    content = None

    @staticmethod
    def send(message):
        print(message)


def gutenberg():
    Message.content = input('Wiadomość: ').lower()

    if Message.content == 'test':
        Message.send('👻')

    if Message.content == 'message':
        Message.send(f'{Message.author}: {Message.content}')

    if Message.content == 'rzuć kostką':
        Message.send(random.choice(range(1, 6)))

    if Message.content == 'kto jest najlepszym programistą?':
        Message.send('Kacper Sieradzinski')
