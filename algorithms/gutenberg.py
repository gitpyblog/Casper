import random


def listonosz(message):
    return message.channel.send(f'{Gutenberg.command(message)}')


# klasa rozkminiająca co tak naprawdę ma zrobić bot i co ma zwrócić
class Gutenberg:
    @staticmethod
    def command(message):
        casper_id = '<@!853645195802181672>'  # id caspra
        print(f'({message.channel}) {message.author}: {message.content}')

        # await message.author.send(page)

        if f'{casper_id} test' == message.content.lower():
            return '👻'

        if f'{casper_id} message' in message.content.lower():
            return message.author.bot

        if f'{casper_id} rzuć kością' == message.content.lower():
            return random.choice(range(1, 6))

        if f'{casper_id} kto jest najlepszym programistą?' == message.content.lower():
            return 'Kacper \U0001F61B'

        #  @TODO: we have await here.. need to code
        # if f'{casper_id} embed' == message.content.lower():
        #     await message.channel.send(
        #         "Guziczki",
        #         components=[
        #             [
        #                 Button(label="⭐ WOW button!", style=1, custom_id="button1"),
        #                 Button(label="👻 Świetnie!", style=2, custom_id="button2"),
        #                 Button(label="💪 Lubię to", style=3, custom_id="button3"),
        #                 Button(label="🍓 Nieżle", style=4, custom_id="button4"),
        #             ]
        #         ],
        #     )
