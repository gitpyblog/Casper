from random import choice


def notebook(m):
    with open('notebook.txt', "a", encoding="utf-8") as n:
        n.write(f'{m}\n')
    return str('📝 zanotowałem!')


def roll_dice():
    return str(f'🎲 **{choice(range(1, 6))}**')


def flip_coin():
    flip = [
        '🪙 **orzeł!**',
        '🪙 **reszka!**']
    return str(f'{choice(flip)}')


def hello_casper():
    hello = [
        'Cześć!',
        'Siemanko! 👋',
        'Dzień dobry! 😊',
        'Witaj!',
        'Co słychać?',
        'Piona! 🖐️',
        'Przybij żółwika! 👊 ',
        'Dobrze Cię wiedzieć 😀']
    return str(choice(hello))
