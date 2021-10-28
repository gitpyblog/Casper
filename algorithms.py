import random
from termcolor import colored


class Message:
    author = 'JohanesGutenberg'
    content = None

    @staticmethod
    def send(message):
        print(colored(message, 'yellow', attrs=['bold']))


def gutenberg():
    Message.content = input('> ').lower()

    if Message.content == 'test':
        Message.send('👻')

    if Message.content == 'rzuć kostką':
        Message.send(rol_the_dice())

    if Message.content == 'kto jest najlepszym programistą?':
        Message.send(the_best_dev())

    if Message.content == 'opowiedz żart':
        Message.send(tell_me_a_joke())


def rol_the_dice():
    return random.choice(range(1, 6))


def the_best_dev():
    return 'Kacper Sieradzinski'


def tell_me_a_joke():
    pass
