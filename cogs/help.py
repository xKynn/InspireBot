import discord
from discord.ext import commands


class Help:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        """ Shows the possible help categories """
        em = discord.Embed(title='Help',
                           description='The bot only has one command.\n**quote** - Have the inspirobot AI generate a quote for you and post it here.\nPS it also has many aliases/shortcuts for you to find i guess.',
                           color=discord.Color.dark_blue())

        await ctx.send(embed=em)


def setup(bot):
    bot.add_cog(Help(bot))
