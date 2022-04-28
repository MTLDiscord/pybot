
import discord
from discord.ext import commands



class test2(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def test2(self, ctx):

        await ctx.send()

async def setup(bot):
    await bot.add_cog(test2(bot))
