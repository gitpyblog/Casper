from discord.ext import commands
from discord_buttons_plugin import *
from dotenv import load_dotenv  # pip install python-dotenv
from os import environ
from algorithms.gutenberg import Gutenberg

########################################################################################################################
load_dotenv()
DISCORD_TOKEN = environ.get('DISCORD_TOKEN')  # Przypisanie DISCORD_TOKEN ze zmiennych środowiskowych
# obiekt reprezentujący połączenie z discordem:
casper = commands.Bot(command_prefix=commands.when_mentioned)
interaction_channels = ('testy', '🤖・poligon', '👻・casper-bot')  # kanały aktywności bota

# Link do repozytorium: https://github.com/DawidKos/Casper.git
# Poradnik o podstawach discord bota https://realpython.com/how-to-make-a-discord-bot-python/
# GitHub biblioteki discord.py: https://github.com/Rapptz/discord.py
# Dokumentacja discord.py https://discordpy.readthedocs.io/en/latest/api.html
# Metody obiektu message: https://discordpy.readthedocs.io/en/latest/api.html#discord.Message
########################################################################################################################

bot = Gutenberg()
buttons = ButtonsClient(casper)


@casper.event
async def on_ready():  # on_ready() wywoływane po połączeniu z discordem
    print(f'{casper.user.name} connected')
    print(f'Bot ID: {casper.user.id}')


@casper.event
async def on_message(message):  # on_message() wywoływane po nadejściu wiadomości
    print(f'({message.channel}) {message.author}: {message.content}')  # Print wszystkich nadchodzących wiadomości
    command = bot.on_message(message)
    if len(message.content) > 21 and message.content[23] != '^':
        if not message.author.bot and type(command) is str \
                and str(message.channel) in interaction_channels:
            await message.channel.send(command)
    else:
        await casper.process_commands(message)


#################### C O M M A N D S ####################
@casper.command(name='^witaj')
async def witaj(ctx):
    await buttons.send(
        content=f"Cześć, jak się masz?",
        channel=ctx.channel.id,
        components=[
            ActionRow([
                Button(
                    style=ButtonType().Primary,
                    label="Jest super!",
                    custom_id="greatbutton"
                ),
                Button(
                    style=ButtonType().Danger,
                    label="Niezbyt dobrze...",
                    custom_id="sucksbutton"
                )
            ])
        ]
    )

@buttons.click
async def greatbutton(ctx):
    await ctx.reply(f"Dobrze to słyszeć {ctx.member.name}! Trzymaj tak dalej.")

@buttons.click
async def sucksbutton(ctx):
    await ctx.reply(f"Przykro mi {ctx.member.name} :(")
    await buttons.send(
        content="Opowiedzieć Ci suchara?",
        channel=ctx.channel.id,
        components=[
            ActionRow([
                Button(
                    style=ButtonType().Primary,
                    label="Dajesz",
                    custom_id="yes_joke"
                ),
                Button(
                    style=ButtonType().Danger,
                    label="NIE",
                    custom_id="no_joke"
                )
            ])
        ]
    )

@buttons.click
async def yes_joke(ctx):
    await ctx.reply(f"Po co idzie ubezpieczyciel do lasu? \n- Polisa")

@buttons.click
async def no_joke(ctx):
    await ctx.reply(f"Dobra dobra, już nie przeszkadzam, jakby co wiesz gdzie mnie znaleźć ;)")


casper.run(DISCORD_TOKEN)
