import random


def notebook(m):
    with open('notebook.txt', "a") as n:
        n.write(f'{m}\n')
    return str('📝 zanotowałem!')


def roll_dice():
    return str(f'🎲 **{random.choice(range(1, 6))}**')


def flip_coin():
    flip = [
        '🪙 **orzeł!**',
        '🪙 **reszka!**']
    return str(f'{random.choice(flip)}')


def hello_casper():
    hello = [
        'Cześć!',
        'Siemanko! 👋',
        'Dzień dobry! 😊',
        'Witaj!',
        'Co słychać?',
        'Piona! 🖐️',
        'Przybij żółwika! 👊 ']
    return str(random.choice(hello))
