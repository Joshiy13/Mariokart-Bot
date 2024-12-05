import discord
from discord.ext import commands

class Sourcecode(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.slash_command(name="sourcecode", description="Shows the Source Code of the bot")
    async def ping(self, ctx):
        code = discord.Embed(title=f"Source Code: https://github.com/Joshiy13/Mariokart-Bot", color=0xfa0505)
        await ctx.respond(embed = code)


def setup(bot): 
    bot.add_cog(Sourcecode(bot))