import discord
from discord.ext import commands
import praw
import os
import random
import datetime

reddit = praw.Reddit(client_id='FNpct8XLVG2LTg',
                     client_secret='UeA14hUpw7LoKlkqFU2QDLoWu8M',
                     username='CrimsonDevil333',
                     password='shashikant@1',
                     user_agent='my user agent')

memes_ctrl = ["memes"]

class Meme(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, aliases=['memes'])
    async def meme(self,ctx):
        if str(ctx.channel) in memes_ctrl:
            memes_submissions = memes_submissions = reddit.subreddit('Memes').hot()
            post_to_pick = random.randint(1, 100)
            for i in range(0, post_to_pick):
                submission = next(x for x in memes_submissions if not x.stickied)

            embed = discord.Embed(title="Meme Smashhhh....",
                                description=f'Todays meme coming right up on request of \n{ctx.message.author}',
                                color=0x00FFDA) 
            embed.set_thumbnail(
                url="https://i.ibb.co/cX0qSkJ/http-pluspng-com-img-png-meme-png-lol-png-transparent-image-931.png"
            )
            embed.set_image(
                url=submission.url
            )
            embed.set_footer(text=f"{ctx.guild}", icon_url=f"{ctx.guild.icon_url}")
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)

    
    @commands.command(pass_context=True, aliases=['marvelmemes','mavelmeme'])
    async def marvel(self,ctx):
        if str(ctx.channel) in memes_ctrl:
            memes_submissions = memes_submissions = reddit.subreddit('marvelmemes').hot()
            post_to_pick = random.randint(1, 100)
            for i in range(0, post_to_pick):
                submission = next(x for x in memes_submissions if not x.stickied)

            embed = discord.Embed(title="Marvel Meme Smashhhh....",
                                description=f'Todays marvel meme coming right up on request of \n{ctx.message.author}',
                                color=0x47FF00) 
            embed.set_thumbnail(
                url="https://i.ibb.co/zRJydjc/pngguru-com.png"
            )
            embed.set_image(
                url=submission.url
            )
            embed.set_footer(text=f"{ctx.guild}", icon_url=f"{ctx.guild.icon_url}")
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)

    @commands.command(pass_context=True, aliases=['animes'])
    async def anime(self,ctx):
        if str(ctx.channel) in memes_ctrl:
            memes_submissions = memes_submissions = reddit.subreddit('Animemes').hot()
            post_to_pick = random.randint(1, 100)
            for i in range(0, post_to_pick):
                submission = next(x for x in memes_submissions if not x.stickied)

            embed = discord.Embed(title="Kawaii Animes Memes",
                                description=f'Kawaii Memes coming right up on request of \n{ctx.message.author}',
                                color=0xF91CD4) 
            embed.set_thumbnail(
                url="https://i.ibb.co/SyqCmJd/pngguru-com-1.png"
            )
            embed.set_image(
                url=submission.url
            )
            embed.set_footer(text=f"{ctx.guild}", icon_url=f"{ctx.guild.icon_url}")
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)

    @commands.command(pass_context = True,aliases=["dank"])
    async def dank_memes(self,ctx):
        if str(ctx.channel) in memes_ctrl:
            memes_submissions = memes_submissions = reddit.subreddit('dankmemes').hot()
            post_to_pick = random.randint(1, 100)
            for i in range(0, post_to_pick):
                submission = next(x for x in memes_submissions if not x.stickied)

            embed = discord.Embed(title="Dank Memes",
                                description=f'Ya danker here is your dank meme .... \n',
                                color=0xF91CD4) 
            embed.set_thumbnail(
                url="https://i.ibb.co/rtGzWNN/Png-Item-29573.png"
            )
            embed.set_image(
                url=submission.url
            )
            embed.set_footer(text=f"{ctx.guild}", icon_url=f"{ctx.guild.icon_url}")
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)