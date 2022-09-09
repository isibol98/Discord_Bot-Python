#!/usr/bin/env python3
import asyncio
from datetime import datetime
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
from discord import Embed


numbers = ("1️⃣","2️⃣","3️⃣","4️⃣","5️⃣")

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

    @commands.command(description="Give information about server.")
    @has_permissions(manage_messages=True)
    async def server_info(self, ctx):
        guild = ctx.guild
        embed = Embed(title=f"{guild} Discord Server Info", timestamp=datetime.utcnow(), color=discord.Color.red())
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/657921190936969217/669885095041171486/ft2.png")
        embed.add_field(name="Date of Foundation:", value=guild.created_at.strftime("%d/%m/%Y %H:%M:%S"))
        embed.add_field(name="Owner:", value=guild.owner)
        embed.add_field(name="Member Count", value=len(guild.members))
        embed.add_field(name="Bot Count", value=len(list(filter(lambda m: m.bot, guild.members))))
        embed.set_footer(text=f"Command has used by {ctx.author}.")

        await ctx.send(embed=embed)

    @commands.command(description="Start a poll.")
    @has_permissions(manage_messages=True)
    async def poll(self, ctx, question:str, *options):
        if len(options) > 5:
            await ctx.send("Maximum choice is 5.")
        else:
            await ctx.channel.purge(limit=1)
            embed = Embed(title="Poll", description=question, timestamp=datetime.utcnow(), color=discord.Color.blue())
            fields = [("Options", "\n".join([f"{numbers[i]} {options[i]}" for i in range(len(options))]), False), 
                      ("Directive", "Click the emoji.", False)]
            embed.set_footer(text=f"Poll has started by {ctx.author}.")
            
            for name, value, inline in fields:
                embed.add_field(name=name, value=value, inline=inline)

            message = await ctx.send(embed=embed)

            for emoji in numbers[:len(options)]:
                await message.add_reaction(emoji)


async def setup(bot):
    await bot.add_cog(Admin_Commands(bot))