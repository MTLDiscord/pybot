import logging

import discord
from discord.ext import commands

log = logging.getLogger(__name__)


class HelpCommand(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command(name='help', description='Discover what I can do!')
    async def globalHelpCommand(self, interaction: discord.Interaction):
        await self.handleHelpCommand(interaction)

    async def handleHelpCommand(self, ctx):
        embed = discord.Embed()
        embed.colour = 0x7289DA
        embed.set_author(name=f'Welcome to {self.bot.user.name}', icon_url=self.bot.user.display_avatar.url)
        embed.description = f"{self.bot.user.name} - бот с открытым исходным кодом.\n\n" \
                            "Для детальной информации о командах, посетите мой [GitHub](https://github.com/MTLDiscord/pybot)."
        embed.add_field(name="__Команды__", value=
        f'**/help** - Помощь по командам.\n'
        f'**/help** - Проверка задержки API.\n', inline=False)

        view = discord.ui.View()
        view.add_item(discord.ui.Button(label="GitHub", emoji="<:github:962089212365111327>", url="https://github.com/MTLDiscord/pybot"))
        view.add_item(discord.ui.Button(label="Invite", emoji="📩", url=discord.utils.oauth_url(self.bot.user.id, permissions=discord.Permissions(8))))
        await ctx.send(embed=embed, view=view, ephemeral=False)


async def setup(bot):
    await bot.add_cog(HelpCommand(bot))
