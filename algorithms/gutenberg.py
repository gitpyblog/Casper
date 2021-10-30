import random


# klasa rozkminiająca co tak naprawdę ma zrobić bot i co ma zwrócić
# to to jest właśnie Gutenberg :)
# @TODO:

class Gutenberg:
    @staticmethod
    def on_message(casper_id, message):


        if f'{casper_id} test' == message.content.lower():
            return '👻'

        if f'{casper_id} message' in message.content.lower():
            return message

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
