# bot.py
from ast import alias
import os
import json
from attr import field
import discord
from discord.ext import commands
from discord.ext.commands import command, Cog
from discord.ext.commands import CommandNotFound, CommandInvokeError
import datetime as datetime
from dotenv import load_dotenv
import platform
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.all()
bot = commands.Bot(command_prefix ="1", help_command=None, intents=discord.Intents.all())

#work with cogs (load, unload, reload)



@bot.command(description="Loads an extention")
@commands.has_permissions(administrator=True)
async def load(ctx, extention):
    embed1 = discord.Embed(
            title=f"Команда {extention} подгружена!",
            description=f"Задержка API: {bot.latency}",
            colour = 0x7289DA   
        )
    await bot.load_extension(f'client.cogs.{extention}')
    await ctx.send(embed=embed1)

@bot.command(description="Unloads an extention")
@commands.has_permissions(administrator=True)
async def unload(ctx, extention):
    embed2 = discord.Embed(
            title=f"Команда {extention} выгружена!",
            description=f"Задержка API: {bot.latency}",
            colour = 0x7289DA   
        )
    await bot.unload_extension(f'client.cogs.{extention}')
    await ctx.send(embed=embed2)

@bot.command(description="Reloads an extention")
@commands.has_permissions(administrator=True)
async def reload(ctx, extention):
    embed3 = discord.Embed(
            title=f"Команда {extention} перезагружена!",
            description=f"Задержка API: {bot.latency}",
            colour = 0x7289DA   
        )
    await bot.unload_extension(f'client.cogs.{extention}')
    await bot.load_extension(f'client.cogs.{extention}')
    await ctx.send(embed=embed3)
#on_ready
@bot.event
async def on_ready():
    for extenison in os.listdir('client/cogs'):
        if extenison[-3:] == '.py':
           await  bot.load_extension('client.cogs.' + extenison[:-3])
    print("---------Бот запущен!--------")
    print("----------Информация----------")
    print(f"Имя бота: {bot.user.name} | ID: {bot.user.id}")
    print(f"Token: {TOKEN}")
    print(f"Python version: {platform.python_version()} | Platform: {platform.system()} {platform.release()} ({os.name}) ")
    print("------------------------------")
    print('Поддерживаемые сервера:')
    for guild in bot.guilds:
        print(guild.name)
    print("------------------------------")
    print()
    await bot.change_presence(activity=discord.Game(name="Test Prescence"))

class Confirm(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    
    @discord.ui.button(label='MagicRPG 1.12.2', style=discord.ButtonStyle.green)
    async def cancel(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('Согласен с Вами! Вперёд, Новус!', ephemeral=True)
        self.value = True
        self.stop()

    # This one is similar to the confirmation button except sets the inner value to `False`
    @discord.ui.button(label='Остальное говно, где тех уебан', style=discord.ButtonStyle.grey)
    async def cancel(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('Cancelling', ephemeral=True)
        self.value = False
        self.stop()

@bot.command()
async def ask(ctx: commands.Context):
    """Asks the user a question to confirm something."""
    # We create the view and assign it to a variable so we can wait for it later.
    view = Confirm()
    await ctx.send('Какой сервер выберете?', view=view)
    # Wait for the View to stop listening for input...
    await view.wait()
    if view.value is None:
        print('Timed out...')
    elif view.value:
        print('Согласен с Вами! Вперёд, Новус!')
    else:
        print('Cancelled...')




#command not found
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send(f"**Ошибка**: {error}")
    raise error

bot.run(TOKEN)
        