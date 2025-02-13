import discord
from discord.ext import commands, tasks
import random

TOKEN = #'ТОКЕН БОТА'
GUILD_ID = #'АЙДИШНИК ГИЛЬДИИ'
ROLE_ID = #'АЙДИШНИК РОЛИ'

intents = discord.Intents.default()
client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    change_color.start()

@tasks.loop(minutes=5)
async def change_color():
    guild = client.get_guild(int(GUILD_ID))
    role = guild.get_role(int(ROLE_ID))

    color = discord.Color.from_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    await role.edit(color=color)

client.run(TOKEN)