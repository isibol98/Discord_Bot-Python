#!/usr/bin/env python3
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
from dc_token import token
import os
import asyncio

intents = discord.Intents.all() #or you can use "discord.Intents.default()" and add 

help_command = commands.DefaultHelpCommand(
    no_category = 'Other Commands')
Bot = commands.Bot("-", description="Discord Bot isibol98", help_command=help_command, intents=intents)

@Bot.event
async def on_ready():
    await Bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Calradia Online | -help", url="https://calradiaonline.com"))
    print("I'm ready!")

@Bot.command() #test your bot
async def ping(ctx):
    await ctx.send("pong!")

if __name__ == "__main__": 
    async def load_extensions(): # categorize bot commands /with cogs
        for filename in os.listdir("./cogs"): # find /cogs folder
            if filename.endswith(".py"): # find .py files in /cogs
                await Bot.load_extension(f"cogs.{filename[:-3]}") # remove .py from cog file and load
    
    async def main():
        async with Bot:
            await load_extensions()
            await Bot.start(token) # get your bot token from discord.com/developers


    asyncio.run(main())
