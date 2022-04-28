
import discord
from discord.ext import commands

class ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # New async cog_load special method is automatically called
    @commands.command()
    async def ping(self, ctx):
        embed = discord.Embed(
            title="Pong!",
            description="Задержка: ",
            colour = 0x7289DA   
        )
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(ping(bot))

