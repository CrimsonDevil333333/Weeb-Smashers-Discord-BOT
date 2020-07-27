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

class Adult(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.color_codes = [0x00FFDA,0x0DFF00,0xFFEB00,0x00FFD7,0x004CFF,0xC600FF,0xFF00AA,0xFF0004,0xCF9292]

    @commands.command(pass_context=True )
    async def adult(self,ctx):
        if ctx.channel.is_nsfw():
            await ctx.send(f"you can use that command here! with others like boobs/hentai/nsfw/milf/bj/nude/ass/pussy/slut/porn !!!!!!!!! Don't frgt to use prefix = '.' its a dot ofcz....")
        else:
            await ctx.send("It's Not an NSFW channel! You big dummy :face_with_hand_over_mouth:")

    @commands.command(pass_context=True,aliases = ["Boob","bews","boobies","bwwbs","beebs"])
    async def boobs(self,ctx):
        if ctx.channel.is_nsfw():
            memes_submissions = memes_submissions = reddit.subreddit('boobs').hot()
            post_to_pick = random.randint(1, 100)
            for i in range(0, post_to_pick):
                submission = next(x for x in memes_submissions if not x.stickied)

            embed = discord.Embed(title="Adults session(Boob's)",
                                description=f'You naughty little....',
                                color=random.choice(self.color_codes)) 
            embed.set_thumbnail(
                url="https://styles.redditmedia.com/t5_2qji2/styles/communityIcon_xqpoacl50r051.png?width=256&s=8a1acd3fb6b3e7b731f6b17b9cd25d39896dc0a5"
            )
            embed.set_image(
                url=submission.url
            )
            embed.set_footer(text=f"{ctx.guild}", icon_url=f"{ctx.guild.icon_url}")
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)
        else:
            await ctx.send("Ya wan't to see some boobs:hot_face::hot_face::hot_face: go to any NSFW channel than .NO Adult stuff here! :triumph:")

    @commands.command(pass_context=True,aliases = ["hentai","henta","animeporn","henti"])
    async def hentais(self,ctx):
        if ctx.channel.is_nsfw():
            memes_submissions = memes_submissions = reddit.subreddit('hentai').hot()
            post_to_pick = random.randint(1, 100)
            for i in range(0, post_to_pick):
                submission = next(x for x in memes_submissions if not x.stickied)

            embed = discord.Embed(title="Adults session(Hentai)",
                                description=f"Some hot hentai pics for you...",
                                color=random.choice(self.color_codes) ) 
            embed.set_thumbnail(
                url="https://styles.redditmedia.com/t5_2qj7g/styles/communityIcon_mrjglaz5bp931.png?width=256&s=12891b0358965c3a4a9e325552a66d403a3a28f0"
            )
            embed.set_image(
                url=submission.url
            )
            embed.set_footer(text=f"{ctx.guild}", icon_url=f"{ctx.guild.icon_url}")
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)
        else:
            await ctx.send("So you want to see some awesome hentai pics but for that use that same command in some NSFW Channels not here!")

    @commands.command(pass_context=True)
    async def nsfw(self,ctx):
        if ctx.channel.is_nsfw():
            memes_submissions = memes_submissions = reddit.subreddit('Nudes').hot()
            post_to_pick = random.randint(1, 100)
            for i in range(0, post_to_pick):
                submission = next(x for x in memes_submissions if not x.stickied)

            embed = discord.Embed(title="NSFW",
                                description=f"Some NSFW pics for you ",
                                color=random.choice(self.color_codes) ) 
            embed.set_thumbnail(
                url="https://i.pinimg.com/236x/aa/91/ac/aa91ac9a54d09aacb9478f77dec187c5.jpg"
            )
            embed.set_image(
                url=submission.url
            )
            embed.set_footer(text=f"{ctx.guild}", icon_url=f"{ctx.guild.icon_url}")
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)
        else:
            await ctx.send("Ya seemed very ||horney|| to me go to NSFW Channels.")

    @commands.command(pass_context=True , aliases = ["milfs","mils"])
    async def milf(self,ctx):
        if ctx.channel.is_nsfw():
            memes_submissions = memes_submissions = reddit.subreddit('milf').hot()
            post_to_pick = random.randint(1, 100)
            for i in range(0, post_to_pick):
                submission = next(x for x in memes_submissions if not x.stickied)

            embed = discord.Embed(title="MILF!",
                                description=f"Seriously well its fine.",
                                color=random.choice(self.color_codes) ) 
            embed.set_thumbnail(
                url="https://pbs.twimg.com/profile_images/1238456111889596418/pw4XDi_j_400x400.jpg"
            )
            embed.set_image(
                url=submission.url
            )
            embed.set_footer(text=f"{ctx.guild}", icon_url=f"{ctx.guild.icon_url}")
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)
        else:
            await ctx.send("||Milf ||what! go to NSFW For that kind of stuff...... ")

    @commands.command(pass_context=True , aliases = ["Blowjobs","blowj","bjob","blow","BJ"])
    async def blowjob(self,ctx):
        if ctx.channel.is_nsfw():
            memes_submissions = memes_submissions = reddit.subreddit('Blowjobs').hot()
            post_to_pick = random.randint(1, 100)
            for i in range(0, post_to_pick):
                submission = next(x for x in memes_submissions if not x.stickied)

            embed = discord.Embed(title="Blow....",
                                description=f"Some bj pics for ya!",
                                color=random.choice(self.color_codes) ) 
            embed.set_thumbnail(
                url="https://68.media.tumblr.com/cb39dd021041b44b48721df5b7d17b95/tumblr_n38z82mq9B1rujy5mo1_1280.jpg"
            )
            embed.set_image(
                url=submission.url
            )
            embed.set_footer(text=f"{ctx.guild}", icon_url=f"{ctx.guild.icon_url}")
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)
        else:
            await ctx.send("Not here pls Goto NSFW .")

    @commands.command(pass_context=True , aliases = ["nudes","nudes_selfie","nude_selfie","selfie","selfi"])
    async def nude(self,ctx):
        if ctx.channel.is_nsfw():
            memes_submissions = memes_submissions = reddit.subreddit('Nude_Selfie').hot()
            post_to_pick = random.randint(1, 100)
            for i in range(0, post_to_pick):
                submission = next(x for x in memes_submissions if not x.stickied)

            embed = discord.Embed(title="Nudes",
                                description=f"ya wanna see some nude selfies ohh ya !!!!!!",
                                color=random.choice(self.color_codes) ) 
            embed.set_thumbnail(
                url="https://styles.redditmedia.com/t5_3ff69/styles/communityIcon_gull08kob4r41.jpg?width=256&format=pjpg&s=b1aba019d8185ecedbd41073f8ec07465c282ff0"
            )
            embed.set_image(
                url=submission.url
            )
            embed.set_footer(text=f"{ctx.guild}", icon_url=f"{ctx.guild.icon_url}")
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)
        else:
            await ctx.send("my pic ??|| OR some adult stuff goto nsfw channels coz ||i am not shairing mine !")

    @commands.command(pass_context=True , aliases = ["booties","asss","asses","booty","asswes"])
    async def ass(self,ctx):
        if ctx.channel.is_nsfw():
            memes_submissions = memes_submissions = reddit.subreddit('ass').hot()
            post_to_pick = random.randint(1, 100)
            for i in range(0, post_to_pick):
                submission = next(x for x in memes_submissions if not x.stickied)

            embed = discord.Embed(title="Hot ass",
                                description=f"...",
                                color=random.choice(self.color_codes) ) 
            embed.set_thumbnail(
                url="https://i.pinimg.com/564x/e7/3b/ec/e73bec09a9ed141144bc5696d27dabca.jpg"
            )
            embed.set_image(
                url=submission.url
            )
            embed.set_footer(text=f"{ctx.guild}", icon_url=f"{ctx.guild.icon_url}")
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)
        else:
            await ctx.send("Get your ass moved to nsfw channels if ya want to see some ass.")

    @commands.command(pass_context=True , aliases = ["puss","pussies","pus"])
    async def pussy(self,ctx):
        if ctx.channel.is_nsfw():
            memes_submissions = memes_submissions = reddit.subreddit('GodPussy').hot()
            post_to_pick = random.randint(1, 100)
            for i in range(0, post_to_pick):
                submission = next(x for x in memes_submissions if not x.stickied)

            embed = discord.Embed(title="Pussies",
                                description=f"What again .......",
                                color=random.choice(self.color_codes) ) 
            embed.set_thumbnail(
                url="https://i.pinimg.com/736x/3e/28/fc/3e28fcb799f3c36737f189fa379f77b2.jpg"
            )
            embed.set_image(
                url=submission.url
            )
            embed.set_footer(text=f"{ctx.guild}", icon_url=f"{ctx.guild.icon_url}")
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)
        else:
            await ctx.send("No cats here!")

    @commands.command(pass_context=True , aliases = ["sluts"])
    async def slut(self,ctx):
        if ctx.channel.is_nsfw():
            memes_submissions = memes_submissions = reddit.subreddit('Slut').hot()
            post_to_pick = random.randint(1, 100)
            for i in range(0, post_to_pick):
                submission = next(x for x in memes_submissions if not x.stickied)

            embed = discord.Embed(title="slt pics",
                                description=f"sluts seriously ?",
                                color=random.choice(self.color_codes) ) 
            embed.set_thumbnail(
                url="https://i.pinimg.com/736x/3e/28/fc/3e28fcb799f3c36737f189fa379f77b2.jpg"
            )
            embed.set_image(
                url=submission.url
            )
            embed.set_footer(text=f"{ctx.guild}", icon_url=f"{ctx.guild.icon_url}")
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)
        else:
            await ctx.send("I know no slut.")

    @commands.command(pass_context=True , aliases = ["porns"])
    async def porn(self,ctx):
        if ctx.channel.is_nsfw():
            memes_submissions = memes_submissions = reddit.subreddit('porn').hot()
            post_to_pick = random.randint(1, 100)
            for i in range(0, post_to_pick):
                submission = next(x for x in memes_submissions if not x.stickied)
                ur=submission.url
            await ctx.send(ur)
        else:
            await ctx.send("NSFW pls!")