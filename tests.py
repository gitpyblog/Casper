from algorithms.gutenberg import *
bot = Gutenberg()


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
    bot

    # when
    kk = bot.command(MessageMock(
        '#kanał', AuthorMock('Dawid'), 'test'
    ))

    # then
    assert kk == '👻'

print(bot.command(MessageMock('#kanał', AuthorMock('Dawid'), 'test')))

# < Message
#     id = 903821401369235576
#     channel = <
#         TextChannel
#         id = 903014255928938507
#         name = 'testy'
#         position = 5
#         nsfw = False
#         news = False
#         category_id = 850123941883281429
#     >
#     type =
#         < MessageType.default: 0>
#     author = <
#         Member
#         id = 822457646589804585
#         name = 'Dawid.S'
#         discriminator = '8205'
#         bot = False
#         nick = None
#             guild = < Guild
#             id = 850123941883281428
#             name = 'Casper BOT'
#             shard_id = None
#             chunked = False
#             member_count = 11
#         >
#     >
#     flags = <
#         MessageFlags
#         value = 0
#     >
# >
