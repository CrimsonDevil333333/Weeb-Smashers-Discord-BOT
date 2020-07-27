import discord
from discord.ext import commands
import random
import datetime

uru_guide = ["uru-guide"]

class URUS(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.obls = ("https://images-ext-1.discordapp.net/external/rftLnTiKRQaEv8n7EpjYRiUaaLazZTHYJo5YgQ4BFvI/https/i.imgur.com/BMX35oF.png","https://images-ext-1.discordapp.net/external/DTk4v33eebxa_UvurZOVhiiOqN4opNNY0xrUM6rrroE/https/i.imgur.com/olMSmjU.png","https://images-ext-2.discordapp.net/external/oIB1oEBRNF7TBmztBfUmUg4anvwe-8mNUo5pVTbzh6M/https/i.imgur.com/guEBSUZ.png","https://images-ext-2.discordapp.net/external/m1oY46EYDLzf5K5li-CPOETimO4EFO1w63CL9lTYncE/https/i.imgur.com/Ac55FKz.png","https://images-ext-1.discordapp.net/external/wxPm_FugxmQqHg5PgPQuovHIbPV07ej-6rqGYSHrMFI/https/i.imgur.com/AvfAndU.png","https://images-ext-1.discordapp.net/external/F9j6ogbv8BkGKNwdHIX0DhZBu_ROpwEsPdBIcXvGlZI/https/i.imgur.com/RdmjEHu.png","https://images-ext-2.discordapp.net/external/n_2uoklwZ_ees5vwf4Nka5uitEwvwJulTNyoeEQoqwg/https/i.imgur.com/AnSkI2b.png","https://images-ext-2.discordapp.net/external/dMH754PlNksZjR8-mocx7CFUi29zUaKDn2yCOwK2tCg/https/i.imgur.com/ToBzt8L.png","https://images-ext-1.discordapp.net/external/Of3cTVPaMnOflf1BSQLNM4WXeM4FYYMTARdfK6KZCzU/https/i.imgur.com/iSeRqtY.png","https://images-ext-1.discordapp.net/external/aHzsK--MNelFbpmuwoKk0LjrPtKxVisebiAS8YofAOM/https/i.imgur.com/Id0Obuy.png","https://images-ext-2.discordapp.net/external/SDk3NC4i6J_GyU-OFlereLo-CeuJFQ0bwkxmXfFCwwM/https/i.imgur.com/j9PlUnW.png","https://images-ext-1.discordapp.net/external/Grh28vgW8w48zr2g3zNKPsKaL7hJ6yR4mXyzMAOs3q0/https/i.imgur.com/wSG299Z.png")


    @commands.command(pass_context=True,aliases=['names'])
    async def name(self,ctx):
        if str(ctx.channel) in uru_guide:
            embed = discord.Embed(title="Following are the names of available Odin's Blessings",
                                description='• Amplify\n• Heal\n• Magic\n• Resist\n• Balance\n• focus\n• Insight\n• Will\n• Fortitude\n• Steel\n• Strike\n• Toughness',
                                color=0xFF00C5) 
            embed.set_thumbnail(
                url="https://i.ibb.co/J5c5T8W/odin.png"
            )
            embed.set_footer(text=f"{ctx.guild}", icon_url=f"{ctx.guild.icon_url}")
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)


    @commands.command(pass_context=True, aliases=['bless','blessing','blessings','odin'])
    async def odinbless(self,ctx):
        if str(ctx.channel) in uru_guide:
            embed = discord.Embed(title="You opened a Odin's Blessing chest wow!",
                                description='Congratulations you got....',
                                color=0x00EAFF)        
            imgs=random.choice(self.obls)
            embed.set_thumbnail(
                url="https://i.ibb.co/J5c5T8W/odin.png"
            )
            embed.set_image(
                url=imgs
            )
            embed.set_footer(text=f"{ctx.guild}", icon_url=f"{ctx.guild.icon_url}")
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)

    @commands.command(pass_context=True, aliases=['u', 'ob'])
    async def uru(self,ctx, * , reason =None):
        if str(ctx.channel) in uru_guide:
            if reason == 'heal':
                embed = discord.Embed(title="Odin's Blessing: Heal",
                                    description="• HP - 348/+464\n• HP - 348/+464",
                                    color=0x091DD1)
                embed.set_thumbnail(
                    url="https://images-ext-1.discordapp.net/external/Grh28vgW8w48zr2g3zNKPsKaL7hJ6yR4mXyzMAOs3q0/https/i.imgur.com/wSG299Z.png")
                embed.set_footer(text=f"{ctx.guild}", icon_url=f"{ctx.guild.icon_url}")
                embed.timestamp = datetime.datetime.utcnow()
                await ctx.send(embed=embed)
            elif reason == 'amplify' or reason == 'amlify':
                embed = discord.Embed(title="Odin's Blessing: Amplify",
                                    description="• Energy Attack - 99/+132\n• Critical Dammage - 222/+296",
                                    color=0x091DD1)
                embed.set_thumbnail(
                    url="https://images-ext-2.discordapp.net/external/SDk3NC4i6J_GyU-OFlereLo-CeuJFQ0bwkxmXfFCwwM/https/i.imgur.com/j9PlUnW.png")
                embed.set_footer(text=f"{ctx.guild}", icon_url=f"{ctx.guild.icon_url}")
                embed.timestamp = datetime.datetime.utcnow()
                await ctx.send(embed=embed)
            elif reason == 'magik' or reason == 'magic':
                embed = discord.Embed(title="Odin's Blessing: Magic",
                                    description="• Energy Attack - 99/+132\n• Energy Attack - 99/+132",
                                    color=0x091DD1)
                embed.set_thumbnail(
                    url="https://images-ext-1.discordapp.net/external/aHzsK--MNelFbpmuwoKk0LjrPtKxVisebiAS8YofAOM/https/i.imgur.com/Id0Obuy.png")
                embed.set_footer(text=f"{ctx.guild}", icon_url=f"{ctx.guild.icon_url}")
                embed.timestamp = datetime.datetime.utcnow()
                await ctx.send(embed=embed)
            elif reason == 'resist' or reason == 'ressist':
                embed = discord.Embed(title="Odin's Blessing: Resist",
                                    description="• Energy Attack - 99/+132\n• Ignore Defense - 222/+296",
                                    color=0x091DD1)
                embed.set_thumbnail(
                    url="https://images-ext-1.discordapp.net/external/Of3cTVPaMnOflf1BSQLNM4WXeM4FYYMTARdfK6KZCzU/https/i.imgur.com/iSeRqtY.png")
                embed.set_footer(text=f"{ctx.guild}", icon_url=f"{ctx.guild.icon_url}")
                embed.timestamp = datetime.datetime.utcnow()
                await ctx.send(embed=embed)
            elif reason == 'balanse' or reason == 'balance':
                embed = discord.Embed(title="Odin's Blessing: Balance",
                                    description="• Physical Attack - 99/+132\n• Energy Attack - 99/+132",
                                    color=0x09A92D)
                embed.set_thumbnail(
                    url="https://images-ext-2.discordapp.net/external/dMH754PlNksZjR8-mocx7CFUi29zUaKDn2yCOwK2tCg/https/i.imgur.com/ToBzt8L.png")
                embed.set_footer(text=f"{ctx.guild}", icon_url=f"{ctx.guild.icon_url}")
                embed.timestamp = datetime.datetime.utcnow()
                await ctx.send(embed=embed)
            elif reason == 'focus' or reason == 'foc':
                embed = discord.Embed(title="Odin's Blessing: Focus",
                                    description="• Energy Attack - 99/+132\n• Critical Rate - 222/+296",
                                    color=0x09A92D)
                embed.set_thumbnail(
                    url="https://images-ext-2.discordapp.net/external/n_2uoklwZ_ees5vwf4Nka5uitEwvwJulTNyoeEQoqwg/https/i.imgur.com/AnSkI2b.png")
                embed.set_footer(text=f"{ctx.guild}", icon_url=f"{ctx.guild.icon_url}")
                embed.timestamp = datetime.datetime.utcnow()
                await ctx.send(embed=embed)
            elif reason == 'insight' or reason == 'sight':
                embed = discord.Embed(title="Odin's Blessing: Insight",
                                    description="• Energy Attack - 99/+132\n• Skill Cooldown - 222/+296",
                                    color=0x09A92D)
                embed.set_thumbnail(
                    url="https://images-ext-1.discordapp.net/external/F9j6ogbv8BkGKNwdHIX0DhZBu_ROpwEsPdBIcXvGlZI/https/i.imgur.com/RdmjEHu.png")
                embed.set_footer(text=f"{ctx.guild}", icon_url=f"{ctx.guild.icon_url}")
                embed.timestamp = datetime.datetime.utcnow()
                await ctx.send(embed=embed)
            elif reason == 'wil' or reason == 'wiil' or reason == 'will':
                embed = discord.Embed(title="Odin's Blessing: Will",
                                    description="• Physical Attack - 99/+132\n• Skill Cooldown - 222/+296",
                                    color=0x09A92D)
                embed.set_thumbnail(
                    url="https://images-ext-1.discordapp.net/external/wxPm_FugxmQqHg5PgPQuovHIbPV07ej-6rqGYSHrMFI/https/i.imgur.com/AvfAndU.png")
                embed.set_footer(text=f"{ctx.guild}", icon_url=f"{ctx.guild.icon_url}")
                embed.timestamp = datetime.datetime.utcnow()
                await ctx.send(embed=embed)


            elif reason == 'fortitude' or reason == 'fortude' or reason == 'forti':
                embed = discord.Embed(title="Odin's Blessing: Fortitude",
                                    description="• Physical Attack - 99/+132\n• Ignore defense - 222/+296",
                                    color=0xDB200C)
                embed.set_thumbnail(
                    url="https://images-ext-2.discordapp.net/external/m1oY46EYDLzf5K5li-CPOETimO4EFO1w63CL9lTYncE/https/i.imgur.com/Ac55FKz.png")
                embed.set_footer(text=f"{ctx.guild}", icon_url=f"{ctx.guild.icon_url}")
                embed.timestamp = datetime.datetime.utcnow()
                await ctx.send(embed=embed)
            elif reason == 'steel' or reason == 'steal' or reason == 'stel':
                embed = discord.Embed(title="Odin's Blessing: Steel",
                                    description="• Physical Attack - 99/+132\n• Critical Damage - 222/+296",
                                    color=0xDB200C)
                embed.set_thumbnail(
                    url="https://images-ext-2.discordapp.net/external/oIB1oEBRNF7TBmztBfUmUg4anvwe-8mNUo5pVTbzh6M/https/i.imgur.com/guEBSUZ.png")
                embed.set_footer(text=f"{ctx.guild}", icon_url=f"{ctx.guild.icon_url}")
                embed.timestamp = datetime.datetime.utcnow()
                await ctx.send(embed=embed)
            elif reason == 'strike' or reason == 'streke' or reason == 'str':
                embed = discord.Embed(title="Odin's Blessing: Strike",
                                    description="• Physical Attack - 99/+132\n• Physical Attack - 99/+132",
                                    color=0xDB200C)
                embed.set_thumbnail(
                    url="https://images-ext-1.discordapp.net/external/DTk4v33eebxa_UvurZOVhiiOqN4opNNY0xrUM6rrroE/https/i.imgur.com/olMSmjU.png")
                embed.set_footer(text=f"{ctx.guild}", icon_url=f"{ctx.guild.icon_url}")
                embed.timestamp = datetime.datetime.utcnow()
                await ctx.send(embed=embed)
            elif reason == 'toughness' or reason == 'tough' or reason == 'toughnes':
                embed = discord.Embed(title="Odin's Blessing: Toughness",
                                    description="• Physical Attack - 99/+132\n• Critical Rate - 222/+296",
                                    color=0xDB200C)
                embed.set_thumbnail(
                    url="https://images-ext-1.discordapp.net/external/rftLnTiKRQaEv8n7EpjYRiUaaLazZTHYJo5YgQ4BFvI/https/i.imgur.com/BMX35oF.png")
                embed.set_footer(text=f"{ctx.guild}", icon_url=f"{ctx.guild.icon_url}")
                embed.timestamp = datetime.datetime.utcnow()
                await ctx.send(embed=embed)
            elif reason == None:
                await ctx.send(f"{ctx.message.author.mention} please at least enter Odin's Blessing name you want to search.")
            else:
                await ctx.send("please use Correct Keywords")