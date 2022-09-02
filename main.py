import discord
from dotenv import load_dotenv  # pip install python-dotenv
from os import environ
# from discord_components import Button
from algorithms.watson import Watson

########################################################################################################################
load_dotenv()
intents = discord.Intents.default()
intents.message_content = True
DISCORD_TOKEN = environ.get('DISCORD_TOKEN')  # Przypisanie DISCORD_TOKEN ze zmiennych środowiskowych
casper = discord.Client(intents=intents)  # obiekt reprezentujący połączenie z discordem
interaction_channels = ('testy', '🤖・poligon', '👻・casper-bot', '💼・oferty-pracy')  # kanały aktywności bota


# Link do repozytorium: https://github.com/DawidKos/Casper.git
# Poradnik o podstawach discord bota https://realpython.com/how-to-make-a-discord-bot-python/
# GitHub biblioteki discord.py: https://github.com/Rapptz/discord.py
# Dokumentacja discord.py https://discordpy.readthedocs.io/en/latest/api.html
# Metody obiektu message: https://discordpy.readthedocs.io/en/latest/api.html#discord.Message

########################################################################################################################


@casper.event
async def on_ready():  # on_ready() wywoływane po połączeniu z discordem
    print(f'{casper.user.name} connected (ID: {casper.user.id})\n')


@casper.event
async def on_message(message):  # on_message() wywoływane po nadejściu wiadomości
    msg = Watson(message)
    print(f'({msg.channel}) {msg.author}: {msg.message}')  # Print wszystkich nadchodzących wiadomości

    if msg.author.bot is False and msg.find() is not None:
        await msg.channel.send(msg.find())


casper.run(DISCORD_TOKEN)
