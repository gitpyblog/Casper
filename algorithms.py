import random


class Message:
    author = 'JohanesGutenberg'
    content = None

    @staticmethod
    def send(message):
        print(message)


def gutenberg():
    Message.content = input('Wiadomość: ').lower()

    if Message.content == 'test':
        Message.send('👻')

    if Message.content == 'rzuć kostką':
        Message.send(rol_the_dice())

    if Message.content == 'kto jest najlepszym programistą?':
        Message.send(the_best_dev())


def rol_the_dice():
    return random.choice(range(1, 6))


def the_best_dev():
    return 'Kacper Sieradzinski'
