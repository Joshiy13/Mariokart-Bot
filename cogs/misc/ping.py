import discord
from discord.ext import commands

class Ping(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.slash_command(name="ping", description="Shows the latency of the bot")
    async def ping(self, ctx):
        ping = discord.Embed(title=f"Ping: {round(self.bot.latency * 1000)} ms", color=0xfa0505)
        await ctx.respond(embed = ping)


def setup(bot): 
    bot.add_cog(Ping(bot))