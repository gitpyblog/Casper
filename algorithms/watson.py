import re
import textdistance

from algorithms.algorithms import *

casper_id = '853645195802181672'  # id caspra
helps = ('help', 'pomoc', 'komendy')
note = ('zanotuj',)
roll = ('rzuć', 'rzucaj', 'kulnij', 'kulaj')
dice = ('kostką', 'kością')
coin = ('monetą', 'monetka')
tests = ('test', 'testuj')
hello = ('cześć', 'witaj', 'hejka')


# klasa rozkminiająca co tak naprawdę ma zrobić bot i co ma zwrócić
class Watson:

    def __init__(self, message):
        self.message = message.content
        self.author = message.author
        self.channel = message.channel

    @staticmethod
    def compare(w, p=0):
        for word in w:
            if textdistance.hamming.normalized_distance(word, p) < 0.3:
                return True

    def find(self):
        action = None
        words = re.findall(r'[0-9]{18}|[\w]{4,}', self.message)  # TODO: Obsłużyć wyjątek regexa mniejszego niż 4 znaki

        if words[0] == casper_id:

            if words[1] in helps:
                action = 'O pomoc pytaj <@822457646589804585>'

            if Watson.compare(tests, words[1]) is True:
                action = '👻'

            if Watson.compare(note, words[1]) is True:
                action = notebook(f'{self.author}: {self.message}')

            if Watson.compare(hello, words[1]) is True:
                action = hello_casper()

            if Watson.compare(roll, words[1]) is True:

                if Watson.compare(dice, words[2]) is True:
                    action = roll_dice()

                if Watson.compare(coin, words[2]) is True:
                    action = flip_coin()

        if words[0] != casper_id and casper_id in words:
            action = 'Ktoś mnie szuka?'

        return action

    def show(self):
        print(f'Treść: {self.message}')
        print(f'Autor: {self.author}')
        print(f'Kanał: {self.channel}\n')
