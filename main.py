from algorithms import *
from dotenv import load_dotenv  # pip install python-dotenv
from os import environ
import random
from discord_components import Button

########################################################################################################################
load_dotenv()
DISCORD_TOKEN = environ.get('DISCORD_TOKEN')  # Przypisanie DISCORD_TOKEN ze zmiennych środowiskowych
casper = discord.Client()  # obiekt reprezentujący połączenie z discordem
casper_id = '<@!853645195802181672>'  # id caspra
interaction_channels = ('testy', '🤖・poligon', '👻・casper-bot')  # kanały aktywności bota


# Link do repozytorium: https://github.com/DawidKos/Casper.git
# Poradnik o podstawach discord bota https://realpython.com/how-to-make-a-discord-bot-python/
# GitHub biblioteki discord.py: https://github.com/Rapptz/discord.py
# Dokumentacja discord.py https://discordpy.readthedocs.io/en/latest/api.html
# Metody obiektu message: https://discordpy.readthedocs.io/en/latest/api.html#discord.Message

########################################################################################################################


@casper.event
async def on_ready():  # on_ready() wywoływane po połączeniu z discordem
    print(f'{casper.user.name} connected')
    print(f'Bot ID: {casper.user.id}')


@casper.event
async def on_message(message):  # on_message() wywoływane po nadejściu wiadomości
    print(f'({message.channel}) {message.author}: {message.content}')  # Print wszystkich nadchodzących wiadomości

    if message.author == casper.user:  # Zabezpieczenie przed sprzęźeniem zwrotnym
        return

    # Interakcje
    if str(message.channel) in interaction_channels:
        # if f'{casper_id} !GO' == message.content.lower():
        #     await message.channel.send('')

        if f'{casper_id} test' == message.content.lower():
            await message.channel.send('👻')

        if f'{casper_id} message' in message.content.lower():
            await message.channel.send(message)

        if f'{casper_id} rzuć kością' == message.content.lower():
            await message.channel.send(random.choice(range(1, 6)))

        if f'{casper_id} kto jest najlepszym programistą?' == \
                message.content.lower():
            await message.channel.send('Kacper \U0001F61B')

        if f'{casper_id} embed' == message.content.lower():
            await message.channel.send(
                "Guziczki",
                components=[
                    [
                        Button(label="⭐ WOW button!", style=1, custom_id="button1"),
                        Button(label="👻 Świetnie!", style=2, custom_id="button2"),
                        Button(label="💪 Lubię to", style=3, custom_id="button3"),
                        Button(label="🍓 Nieżle", style=4, custom_id="button4"),
                    ]
                ],
            )


casper.run(DISCORD_TOKEN)
