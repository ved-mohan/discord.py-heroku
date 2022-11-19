import discord
import os
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}({bot.user.id})')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def edit(ctx):
    await ctx.edit(ctx, "No ")

@bot.command()
async def hello(ctx):
    await ctx.send('hi')

if __name__ == '__main__':
    bot.run(os.getenv('DISCORD_TOKEN'))
