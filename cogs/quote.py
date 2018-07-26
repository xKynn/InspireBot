from discord import Embed, Color
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType

class Quote:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['generate', 'gen', 'q', 'inspire', 'motivate'])
    @commands.cooldown(1, 2, BucketType.channel)
    async def quote(self, ctx):
        """ Add a new role or invite source to the database. """
        async with self.bot.ses.get('http://inspirobot.me/api?generate=true') as resp:
            lnk = await resp.text()
        emb = Embed(color=Color.dark_blue())
        emb.set_image(url=lnk)
        emb.set_footer(text='|  Powered by [InspiroBot](http://inspirobot.me)', icon_url='https://i.imgur.com/FDSkzYC.png')
        await ctx.channel.send(embed=emb)

def setup(bot):
    bot.add_cog(Quote(bot))
