import discord
from discord.ext import commands
import random


class Coinflip(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.slash_command(name="score", description="Score a game")
    async def coinflip(self, ctx):
        result = random.choice(["Heads", "Tails"])
        coinflip_embed = discord.Embed(title="Coinflip", description=f"The coin landed on **{result}**!", color=0xfa0505)
        await ctx.respond(embed=coinflip_embed)
        return


def setup(bot):
    bot.add_cog(Coinflip(bot))