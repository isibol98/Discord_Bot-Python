import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
from discord import Member



class Admin_Commands(commands.Cog, name="Admin Commands", description="Admin commands"):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    @has_permissions(manage_messages=True) # you can add spesific permissions so you can avoid to abuse. 
    async def clean(self, ctx, amount=5): # clean messages, bot delete last 5 messages if you dont give spesific number
        await ctx.channel.purge(limit=amount)

    @clean.error
    async def clean_error(self,ctx,error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have permissions!")

    @commands.command()
    @has_permissions(kick_members=True)
    async def kick(self, ctx, member:discord.Member, *, reason="None"):
        await member.kick(reason=reason)
        print("kicked")
        await ctx.send(f"{member} kicked!")

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have permissions!")

    @commands.command()
    @has_permissions(ban_members=True)
    async def ban(self, ctx, member:discord.Member, *, reason="None"): # you can add spesific reason of ban, default is none.
        await member.ban(reason=reason)
        await ctx.send(f"{member} banned!")

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have permissions!")

    @commands.command()
    @has_permissions(ban_members=True)
    async def unban(self, ctx, member:discord.User, reason="None"):
        await ctx.guild.unban(member,reason=reason)
        await ctx.send(f"{member.mention} unbanned!")

    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have permissions!")

async def setup(bot):
    await bot.add_cog(Admin_Commands(bot))