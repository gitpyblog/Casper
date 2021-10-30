import discord
from dotenv import load_dotenv
from os import environ
from algorithms.gutenberg import *

load_dotenv()
DISCORD_TOKEN = environ.get('DISCORD_TOKEN')
casper = discord.Client()


# interaction_channels = ('testy', '🤖・poligon', '👻・casper-bot')  # kanały aktywności bota

@casper.event
async def on_ready():  # on_ready() wywoływane po połączeniu z discordem
    print(f'{casper.user.name} connected')
    print(f'Bot ID: {casper.user.id}')


@casper.event
async def on_message(message):  # on_message() wywoływane po nadejściu wiadomości
    if message.author.bot is not True:  # Zabezpieczenie przed sprzęźeniem zwrotnym
        await listonosz(message)


casper.run(DISCORD_TOKEN)
