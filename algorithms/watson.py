import random
import re

import textdistance


# klasa rozkminiająca co tak naprawdę ma zrobić bot i co ma zwrócić
class Watson:

    def __init__(self, message):
        self.message = message.content
        self.author = message.author
        self.channel = message.channel

    @staticmethod
    def compare(a, b=0):
        for word in a:
            if textdistance.hamming.normalized_distance(word, b) < 0.3:
                return True

    def find(self):
        action = None
        casper_id = '853645195802181672'  # id caspra
        words = re.findall(r'[0-9]{18}|[\w]{4,}', self.message)

        helps = ('help', 'pomoc', 'komendy')
        roll = ('rzuć', 'kulnij', 'kulaj')
        dice = ('kostką', 'kością')
        coin = ('monetą', 'monetke')
        tests = ('test', 'testuj')
        find = ('szukaj', 'poszukaj', 'znajdź', 'odszukaj', 'wyszukaj')

        if words[0] == casper_id:

            if words[1] in helps:
                action = 'O pomoc pytaj <@822457646589804585>'

            if Watson.compare(tests, words[1]) is True:
                action = '👻'

            if Watson.compare(find, words[1]) is True:
                action = 'znaleziono'

            if Watson.compare(roll, words[1]) is True:
                if Watson.compare(dice, words[2]) is True:
                    action = f'🎲 **{random.choice(range(1, 6))}**'
                if Watson.compare(coin, words[2]) is True:
                    x = ('🪙 **orzeł!**', '🪙 **reszka!**')
                    action = f'{random.choice(x)}'

        if words[0] != casper_id and casper_id in words:
            action = 'Ktoś mnie szuka?'

        return action

    def show(self):
        print(f'Treść: {self.message}')
        print(f'Autor: {self.author}')
        print(f'Kanał: {self.channel}\n')
