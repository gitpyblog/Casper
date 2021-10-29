from textdistance import hamming

class HelloResponse:
    def __init__(self, text):
        self.text = text

class ByeResponse:
    def __init__(self, text):
        self.text = text


class HelloCommand:
    def run(self):
        return HelloResponse('hello')


class ByeCommand:
    def run(self):
        return ByeResponse('bye!')



class Bot:

    COMMANDS = {
        'hello': HelloCommand(),
        'bye': ByeCommand()
    }

    def __init__(self):
        pass

    @staticmethod
    def on_command(text):
        try:
            return Bot.COMMANDS[text].run().text
        except KeyError:
            # przejde przez wszystkie komendy dostępne
            # i znajdę tę która jest najbardziej podobna
            possible_commands = []
            for command in Bot.COMMANDS:
                if hamming(command, text) <= 3:
                    possible_commands.append(command)

            print('Czy chodziło Ci o:')
            for command in possible_commands:
                print(command)

bot = Bot()
print(bot.on_command('bey'))