import discord
from discord.ext import commands
import os
import asyncio
import shutil
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import requests 

class INFO(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def info(self,ctx , user: discord.Member = None):
        if user == None:
            await ctx.send("At lest gimme member name you want to know about ;)")
        else:
            img = Image.open("images/infoimgimg.png")
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype("fonts/Modern_Sans_Light.otf", 110)
            fontbig = ImageFont.truetype("fonts/Fitamint Script.otf", 240)
            draw.text((200, 0), "Weeb Smashers:", (255, 50, 222), font=fontbig)
            draw.text((50, 500), "Username: {}".format(user.name), (28, 255, 0), font=font)
            draw.text((50, 700), "ID:  {}".format(user.id), (28, 255, 0), font=font)
            draw.text((50, 900), "User Status: {}".format(user.status), (28, 255, 0), font=font)
            draw.text((50, 1100), "Account created: {}".format(user.created_at), (28, 255, 0), font=font) 
            draw.text((50, 1300), "Nickname: {}".format(user.display_name),(28, 255, 0), font=font)
            draw.text((50, 1500), "User's Top Role: {}".format(user.top_role), (28, 255, 0), font=font)
            draw.text((50, 1700), "User Joined: {}".format(user.joined_at), (28, 255, 0), font=font)
            img.save('images/temp/change.png') 
            file = discord.File("images/temp/change.png",filename="change.png")
            await ctx.channel.send("",file=file)

    @commands.command(pass_context=True, aliases=['av','avtar',"avatar"])
    async def icon(self,ctx ,* ,user: discord.Member = None):
        if user == None:
            embed = discord.Embed(title=f"{ctx.message.author}",
                                color=0x00FFDA) 
            embed.set_image(
                url=ctx.message.author.avatar_url
            )
            await ctx.send(embed=embed)

        else :
            embed = discord.Embed(title=f"{user}",
                                color=0x00FFDA) 
            embed.set_image(
                url=user.avatar_url
            )
            await ctx.send(embed=embed)
    
    @commands.command(pass_context=True, aliases=["user"])
    async def users(self,ctx):
        await ctx.send(f"```Total no of current Members are : {len(list(ctx.guild.members))}```")
