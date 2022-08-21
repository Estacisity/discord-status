import discord, os, asyncio, datetime

from discord.ext import tasks, commands

client = commands.Bot(
  command_prefix=':',
  self_bot=True
)


Token = "Discord Token here"
URL = "https://google.com"


@client.event
async def on_connect():
  await client.change_presence(activity = discord.Streaming(name = "AFK", url = URL))


client.run(Token, bot=False)