

import discord
from discord.ext import commands
import datetime



class verify(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def verify_setup(self, ctx):
        embed = discord.Embed(
            title="Добро пожаловать на сервер **Polunna Community!**",
            description="Общение на нашем сервере является свободным, но для поддержания\n комфортной атмосферы мы просим Вас соблюдать некоторые правила. \nДля перехода к правилам нажмите кнопку под этим сообщением.",
            colour = 0x7289DA,
			timestamp = datetime.datetime.utcnow(),
		)
        view = discord.ui.View()    
        view.add_item(discord.ui.Button(label="Правила", emoji="📜", url = "https://discord.com/channels/969112189610905640/969112190156156975")) 
        await ctx.send(embed=embed, view=view)

async def setup(bot):
    await bot.add_cog(verify(bot))
