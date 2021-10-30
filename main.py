import discord
from dotenv import load_dotenv  # pip install python-dotenv
from os import environ
# from discord_components import Button
from algorithms.gutenberg import Gutenberg

########################################################################################################################
load_dotenv()
DISCORD_TOKEN = environ.get('DISCORD_TOKEN')  # Przypisanie DISCORD_TOKEN ze zmiennych środowiskowych
casper = discord.Client()  # obiekt reprezentujący połączenie z discordem
interaction_channels = ('testy', '🤖・poligon', '👻・casper-bot')  # kanały aktywności bota

# Link do repozytorium: https://github.com/DawidKos/Casper.git
# Poradnik o podstawach discord bota https://realpython.com/how-to-make-a-discord-bot-python/
# GitHub biblioteki discord.py: https://github.com/Rapptz/discord.py
# Dokumentacja discord.py https://discordpy.readthedocs.io/en/latest/api.html
# Metody obiektu message: https://discordpy.readthedocs.io/en/latest/api.html#discord.Message

########################################################################################################################
bot = Gutenberg()


@casper.event
async def on_ready():  # on_ready() wywoływane po połączeniu z discordem
    print(f'{casper.user.name} connected')
    print(f'Bot ID: {casper.user.id}')


@casper.event
async def on_message(message):  # on_message() wywoływane po nadejściu wiadomości
    print(f'({message.channel}) {message.author}: {message.content}')  # Print wszystkich nadchodzących wiadomości

    if message.author.bot is not True and str(message.channel) in interaction_channels:
        if type(bot.on_message(message)) is str:
            await message.channel.send(bot.on_message(message))


casper.run(DISCORD_TOKEN)
