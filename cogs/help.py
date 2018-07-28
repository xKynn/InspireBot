import discord
from discord.ext import commands


class Help:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        """ Shows the possible help categories """
        em = discord.Embed(title='Help',
                           description='**quote** - Have the inspirobot AI generate a quote for you and post it here.\n'
                                       '**invite** - Get the invite link for the bot if you want to invite it to wherever you want.\nPS. it also has many aliases like `q` for quote.',
                           color=discord.Color.dark_blue())

        await ctx.send(embed=em)


def setup(bot):
    bot.add_cog(Help(bot))
