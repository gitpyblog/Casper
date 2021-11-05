import random
import re


# klasa rozkminiająca co tak naprawdę ma zrobić bot i co ma zwrócić
class Watson:

    def __init__(self, message):
        self.message = message.content
        self.author = message.author
        self.channel = message.channel

    def szukaj(self, command):
        if command == self.message:
            pass

    def find(self):
        action = None
        casper_id = '853645195802181672'  # id caspra
        words = re.findall(r'[0-9]{18}|[\w]{4,}', self.message)

        helps = ('help', 'pomoc', 'komendy')
        roll = ('rzuć', 'roll', 'rzóć', 'rzóc', 'rzoc', 'kulnij')
        dice = ('kostką', 'kostkom', 'kością', 'kościom', 'kościa', 'koscią')
        coin = ('monetą', 'coin', 'monetom')
        tests = ('test', 'testy', 'cześć', 'czesc', 'hej')

        if words[0] == casper_id:
            if words[1] in helps:
                action = 'O pomoc pytaj <@822457646589804585>'

            if words[1] in tests:
                action = '👻'

            if words[1] in roll:
                if words[2] in dice:
                    action = f'🎲 **{random.choice(range(1, 6))}**'
                if words[2] in coin:
                    x = ('🪙 **orzeł!**', '🪙 **reszka!**')
                    action = f'{random.choice(x)}'

        if words[0] != casper_id and casper_id in words:
            action = 'Ktoś mnie szuka?'

        return action

        # if f'{casper_id} test' == self.message:
        #     action = '👻'
        #
        # if f'{casper_id} embed' == self.message:
        #     pass
        #
        # if f'{casper_id} rzuć kością' == self.message:
        #     action = f'🎲 {random.choice(range(1, 6))}'
        #
        # if f'{casper_id} rzuć monetą' == self.message:
        #     coin = ('🪙 orzeł!', '🪙 reszka!')
        #     action = f'{random.choice(coin)}'
        #
        # if f'{casper_id} kto jest najlepszym programistą?' == self.message:
        #     action = '<@!400403900039168000> :first_place:'
        #
        # return action

    def show(self):
        print(f'Treść: {self.message}')
        print(f'Autor: {self.author}')
        print(f'Kanał: {self.channel}\n')
