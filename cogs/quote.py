from discord import Embed, Color
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType

class Quote:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['generate', 'gen', 'q', 'inspire', 'motivate'])
    @commands.cooldown(1, 2, BucketType.channel)
    async def quote(self, ctx):
        """ Get and send a quote. """
        async with self.bot.ses.get('http://inspirobot.me/api?generate=true') as resp:
            lnk = await resp.text()
        emb = Embed(color=Color.dark_blue())
        emb.set_image(url=lnk)
        emb.set_footer(text='|  Powered by http://inspirobot.me', icon_url='https://i.imgur.com/FDSkzYC.png')
        await ctx.channel.send(embed=emb)
    @commands.command(aliases=['link', 'inv'])
    async def invite(self, ctx):
        """ Invite the bot. """
        await ctx.channel.send(embed=Embed(title='Invite me!', url='https://discordapp.com/oauth2/authorize?client_id=472095049405038594&permissions=84992&scope=bot)', 
                               color=Color.dark_blue()))

def setup(bot):
    bot.add_cog(Quote(bot))