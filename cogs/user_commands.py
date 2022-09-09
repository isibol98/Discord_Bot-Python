#!/usr/bin/env python3
from discord.ext import commands

class User_Commands(commands.Cog, name="User Commands", description="User Commands"):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(description="Send link")
    async def link(self, ctx):
        await ctx.channel.purge(limit=1)
        await ctx.send("https://calradiaonline.com")