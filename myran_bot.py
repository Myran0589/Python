import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

client = commands.Bot(command_prefix="?")

@client.event
async def on_ready():
	print("online")
	print(client.user.name)
	
client.run("NzE0Mzg5NTA3OTI3MDQ4MjA0.XwITGg.MMqxu4I9iWGN-DDOwuJaP0aoP7M")
