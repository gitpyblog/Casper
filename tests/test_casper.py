from algorithms.watson import Watson


class AuthorMock:
    def __init__(self, username):
        self.username = username

    def __repr__(self):
        return self.username


class MessageMock:
    def __init__(self, channel, author, content):
        self.channel = channel
        self.author = author
        self.content = content


def test_test():
    # given
    bot = Watson()

    # when
    response = bot.on_message(123, MessageMock(
        '#kanał',
        AuthorMock('Kacper'),
        '123 test'
    ))

    # then
    assert response == '👻'


def test_throw_a_dice():
    # given
    bot = Watson()

    # when
    response = bot.on_message(123, MessageMock(
        '#kanał',
        AuthorMock('Kacper'),
        '123 rzuć kością'
    ))

    # then
    assert 1 <= response <= 6

# def test_is_a_bootcamp_member():
#     # TDD - test driven development
#     # sprawdzam, czy dany email znajduje się na liście maili kursantów
#     # given
#     bot = Gutenberg()
#     bot.listaKursantow = []
#
#     response = bot.on_message(123, MessageMock(
#         '#'
#     ))
