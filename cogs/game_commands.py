#!/usr/bin/env python3
import discord
from discord.ext import commands
from random import randint as rd
import asyncio

class Game_Commands(commands.Cog, name="Game Commands", description="Game commands"):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def roll(self,ctx):
        await ctx.send(Game_Commands.roll_dice())
    @staticmethod
    def roll_dice():
        return rd(1,6)

    @commands.command()
    async def guess(self,ctx):
        number = rd(1, 100)
        await ctx.send(f'I held a number between 1 and 100. Can you find it? You have 5x chance!')

        def check(msg:discord.Message):
            return msg.author.id == ctx.author.id and msg.channel.id == ctx.channel.id and msg.content.isdigit()
        chance = 5

        while(True):
            try:    
                msg = await self.bot.wait_for('message', check=check, timeout=10.0)
                if (msg.content == str(number)) and (chance >0):
                    await ctx.send('You got it!')
                    await msg.add_reaction("<:cay:790243173107761213>") # you can add own custom emoji!
                    break

                elif (msg.content < str(number)) and (chance >0):
                    await msg.add_reaction("<:yukari:1009729225370120242>") # up emoji
                    chance-=1
                    print(chance)

                elif (msg.content > str(number)) and (chance >0):
                    await msg.add_reaction("<:asagi:1009729243103633478>") # down emoji
                    chance-=1
                    print(chance)

                elif chance==0:
                    await ctx.send(f"I won! Number: {number}")
                    break
                else:
                    await ctx.send("It seems something wrong...")
                    break
            except asyncio.TimeoutError:
                await ctx.send("You have to respond in 10 second!")
                break

async def setup(bot):
    await bot.add_cog(Game_Commands(bot))