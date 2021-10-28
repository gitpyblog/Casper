import random


class Message(object):
    author = 'JohanesGutenberg'
    content = None


def gutenberg():
    Message.content = input('Wiadomość: ').lower()

    if Message.content == 'test':
        print('👻')

    if Message.content == 'message':
        print(f'{Message.author}: {Message.content}')

    if Message.content == 'rzuć kostką':
        print(random.choice(range(1, 6)))

    if Message.content == 'kto jest najlepszym programistą?':
        print('Kacper Sieradzinski')
