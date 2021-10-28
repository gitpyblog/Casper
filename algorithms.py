class Stefek(object):
    author = 'JohanesGutenberg'
    content = None


def gutenberg():
    Stefek.content = input('Wiadomość: ').lower()

    if Stefek.content == 'message':
        print(f'{Stefek.author}: {Stefek.content}')

    if Stefek.content == 'test':
        print('testy ok')
