import os
import discord
from discord.ext import commands
import asyncio

client = commands.Bot()
token = os.getenv("TOKEN")
intents = discord.Intents.none()
intents.members = True
intents.guilds = True
intents.messages = True
intents.reactions = True
intents.voice_states = True

cogs_list_fun = [
    "score",
    "leaderboard",
    "player"
]

cogs_list_misc = [
    "help",
    "ping"
]

for cog in cogs_list_fun:
    client.load_extension(f"cogs.fun.{cog}")



@client.event
async def on_ready():
    client.loop.create_task(status_task())
    print("Bot is ready! Logged in as {0.user}".format(client))



async def status_task():
    while True:
        await client.change_presence(activity=discord.Game(name="/help"))
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Game(name="Celestix.dev"))
        await asyncio.sleep(10)


client.run(token) 