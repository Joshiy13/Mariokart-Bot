import discord
from discord.ext import commands


fun_help = discord.Embed(title="Fun Commands", color=0xfa0505)
fun_help.add_field(name="/coinflip", value="Flip a Coin", inline=False)
fun_help.add_field(name="/tictactoe", value="Play Tic Tac Toe against someone", inline=False)
fun_help.add_field(name="/rps", value="Play Rock Paper Scissors against the Bot", inline=False)

misc_help = discord.Embed(title="Miscellaneous Commands", color=0xfa0505)
misc_help.add_field(name="/help", value="Shows this page", inline=False)
misc_help.add_field(name="/ping", value="Shows the latency of this Bot", inline=False)
misc_help.add_field(name="/support", value="Use this command to send a message to the dev", inline=False)
misc_help.add_field(name="/level", value="Shows your current level", inline=False)


moderation_help = discord.Embed(title="Moderation Commands", color=0xfa0505)
moderation_help.add_field(name="/ban", value="Ban a user", inline=False)
moderation_help.add_field(name="/unban", value="Unbans a user", inline=False)
moderation_help.add_field(name="/purge", value="Delete a specified number of messages in the channel", inline=False)
moderation_help.add_field(name="/kick", value="Kick a user", inline=False)
moderation_help.add_field(name="/slowmode", value="Set slowmode in the current channel (turn off by typing off)", inline=False)
moderation_help.add_field(name="/lock", value="Lock or unlock a channel for a specified duration (turn off by typing off)", inline=False)
moderation_help.add_field(name="/tempban", value="Temporarily ban a user from the server", inline=False)

help_pages = [misc_help, moderation_help, fun_help]

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.page_index = 0

    @commands.slash_command(name="help", description="Use this command to get help")
    async def customhelp(self, ctx):
        message = await ctx.send(embed=help_pages[self.page_index])
        await ctx.defer()

        emojis = ["⏪", "⬅️", "➡️", "⏩"]

        for emoji in emojis:
            await message.add_reaction(emoji)

        def check(reaction, user):
            return user == ctx.author and reaction.message == message

        while True:
            try:
                reaction, user = await self.bot.wait_for("reaction_add", timeout=60.0, check=check)

                if str(reaction.emoji) == "⬅️":
                    self.page_index = max(0, self.page_index - 1)
                elif str(reaction.emoji) == "➡️":
                    self.page_index = min(len(help_pages) - 1, self.page_index + 1)
                elif str(reaction.emoji) == "⏪":
                    self.page_index = 0
                elif str(reaction.emoji) == "⏩":
                    self.page_index = len(help_pages) - 1

                await message.edit(embed=help_pages[self.page_index])
                await message.remove_reaction(reaction, user)
            except TimeoutError:
                break

def setup(bot):
    bot.add_cog(Help(bot))