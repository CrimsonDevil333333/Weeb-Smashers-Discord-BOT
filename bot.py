############################################   weeb smashers   ##########################################
from cogs.music_player import Music
from cogs.meme import Meme
from cogs.adult import Adult
from cogs.MFF.ctp import CTPS
from cogs.MFF.uru import URUS
from cogs.FunChat import AIMLS
from cogs.info import INFO
from cogs.covid.reddit import Reddit

import datetime
import wikipedia
import discord
from discord.ext import commands
import datetime
import random
from discord.utils import get
from random import randrange
import asyncio
import os
import shutil
import requests 
import config
import logging

from discord.utils import find
from discord.ext import commands
from discord.ext.commands import when_mentioned_or
from datetime import datetime






rust_ctrl = ["rust-language"]
anime_reco = ["animes",'anime','weeb-smash','weebs','weeb']



wlcm = 630341659099398144
anouncement = 630333673584984064  #were want to anounce
newvideo = 630513815855038496     #were want to upload new video
admin_ctrl = 638263332863737868
wike = ["wikipedia"]

suggest_vid = 637272528393338880

#valid users
valid_users = ["Crimson Devil#7759"]

list1 = []
list2 = []
################################################################## AIML ###########################


###################################################################################################
def read_token():
    with open("token.txt","r") as f:
        lines =f.readlines()
        return lines[0].strip()
token = read_token()
def read_prefex():
    with open("prefex.txt","r") as f:
        lines = f.readlines()
        return lines[0].strip()
prefex = read_prefex()
bot = commands.Bot(command_prefix=prefex , case_insensitive=True)
bot.remove_command("help")


#######################       start         ###########################







    
# *************************************************************************** AIML ABOVE ! #######

@bot.command(pass_context=True, aliases=['rec','recommend','recomend','reco','nerd'])
async def weeb(ctx, * , reason =None):
    if str(ctx.channel) in anime_reco:
        if reason == None:
            await ctx.send("You little weeb at least tell me your fav genre for animes.")
        elif reason == 'romance' or reason == "Romance" or reason =="romanse" or reason == 'R' or reason == 'r':
            embed = discord.Embed(title="Animes Recommendation's",
                              description=f'So {ctx.message.author} is into romance animes for you here is my recommendation.\nHope you gonna like it.',
                              color=0xF400FF) 
            embed.set_thumbnail(
                url="https://cdn141.picsart.com/255950841011212.png?r1024x1024"
            )
            rom = ("https://images-na.ssl-images-amazon.com/images/I/517dSLp8UvL.jpg","https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTEg-F7fec_urFZz11A1CNcsIKpOpU7pbTDdYzzfako7p7YiIh5","https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSBgaJ6KjlQOKgmVeR3Lhd2hzWmZEh2YZ_U-CYcn7kinUf3j-6z","https://cdn.myanimelist.net/r/334x484/images/anime/3/25518.webp?s=694d4250eb82913d141d4b78b4b83daf","https://cdn.myanimelist.net/r/334x484/images/anime/11/75563.webp?s=23cad69be03ca315417d186d1003d645","https://i.ytimg.com/vi/HG_xsxSvTn4/maxresdefault.jpg","https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSS_ocq6l9EEnwRwcbfMjADUEWcDqeuj02IPs7kdmCWztNB-JuQ","https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRHuaxn5PrE56ueidW4wbKZOkdQyxm3TDmRG2H3sf3E8eTsMqdm","https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSfoquuMaeGloMV5xPgqaNY67tA5rcv-1QJ08a7Tk19QIoLQ42o","https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSd3JtA7vzhMSjckEWOQovpiPNQw8VHNZvGyNCVTiIsLVgntIMv","https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTmuE0k42Xi8Ek3ANOXUADcNvtUGkfunVf-YO43acG0a_Ap5wjx","https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRYNGBRGmhr7M5kMjf7yYEv82Va5b99HNz9um77R-8WKl_QMy6c","https://cdn.myanimelist.net/r/334x484/images/anime/5/76034.webp?s=78a8982dc1afd0fd8dfdbf57f356ba76","https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSAEuSOMVKzZItP3epBzjIkawqPpqRv91VgPBVrbN_t_m3jLlrP","https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQAGxSxffAF3deI7pHVTrq-racg73GCktzf9QKuShvWH4zB7nyO","https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQTRIOHrN9JL5K3DPccKh3rOXzHumpb51PxPnO_kE-KvZ_GKxU6","https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSaYFklOsG5qLkLuYmva9LUoS-fPpiug4ZQpwY05IsKhWTLM0z-","https://images-na.ssl-images-amazon.com/images/I/71MYAESZpEL._SL1000_.jpg","https://images-na.ssl-images-amazon.com/images/I/71b3MahBcnL._SY445_.jpg","https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQRJg_xaTbwoKV4Bz7X7NVxBBpSeTOUlBCtH13gfVwuRRftzsQg","https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTKPYLgoNo51ejA5H5YnvtuJNyWkIR3HEKOm4mlSL1FIdJ7In-s","https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTZWcoTOGB9dRvy3PSutPr4lReEOwBuyck1TbqNt7fS5JRPIOty","https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcT3Zq9YwVGOfxVyE0YpmYM6hpGzXk2fbh1d66je_61uqjo00DEr","https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQDoY40nslHHtbVFf5BR6L_i-QREsT5XmTJfoR6Es4Jw9NxvXxI","https://cdn.myanimelist.net/r/334x484/images/anime/2/73700.webp?s=9f4e72ab1dcea2326135a6ce48a2981c","https://cdn.myanimelist.net/r/334x484/images/anime/8/64813.webp?s=e1d99eb7fd70972cf70cde629256d9bf","https://cdn.myanimelist.net/r/334x484/images/anime/8/86373.webp?s=974377f43e5725dc6b365f20cbf39abd","https://www.planetdp.org//covers/big/dp49889.jpg","https://m.media-amazon.com/images/M/MV5BMjA4NzYzOWItYzA2MC00ZDQwLWExODYtMWYzNjNlNTc2N2M0XkEyXkFqcGdeQXVyMTA3OTEyODI1._V1_UX182_CR0,0,182,268_AL_.jpg","https://ib4.hulu.com/user/v3/artwork/e4c45f43-dc4b-44ce-a9b8-14139ac1af69?base_image_bucket_name=image_manager&base_image=2f93472d-4fd0-461c-b553-9eea092d1903&size=400x600&format=jpeg","https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSEc7EPZZBGiJ0nWWwi3gLKox4ol5_3ScsvR9KhAj8uJtiwwws2","https://i.pinimg.com/originals/60/87/39/608739f14a259700c18bb80bd7e9ed22.jpg","https://i0.wp.com/www.overpoweredentertainment.com/wp-content/uploads/2018/02/1394307_Japanese_ShowDetailHeroPhone_c9598761-7c81-e911-8175-020165574d09.jpg?fit=1080%2C1080&ssl=1","https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcR_KrOJV-xY3QYFOu_Z-9Ncj0hFzVAZSWaGh3kiaPJx1BSMIghP","https://upload.wikimedia.org/wikipedia/en/thumb/7/71/Gekkan_Sh%C5%8Djo_Nozaki-kun.jpg/220px-Gekkan_Sh%C5%8Djo_Nozaki-kun.jpg","https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTJVpuoM20cP5z2F-fLq3hI0z-GszUeXDkAr93C62XVkgf6oKnD","https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSPEk9ahpvC6Ku-R-bx1sSBObSY0zUMN6LQ6tcfdOUK-2F-e83N","https://img.reelgood.com/content/show/aea56a02-21e3-4415-ad93-790a48b5b65b/poster-780.jpg","https://cdn.shoplightspeed.com/shops/608693/files/9915597/aniplex-of-america-inc-irregular-at-magic-high-sch.jpg","https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRHOX6Hmko2hdVwrUkXCZoYpdsgmfNueQWxvF4Ao8u1S0b6Vhdd","https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQvwVd0jqsaosMEvt0z1zCSAPcXi-m_eyBRyLIGBOLlCUNjobRO","https://images-na.ssl-images-amazon.com/images/I/81b2OtyVHpL._SY445_.jpg","https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTr2yNJqdr0BFUC7zIqqVCscnbpGDsjZB7Q-AbOOJHk54DrGCqm","https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSvT3rh3wbGu4cJUz8ComK_PDO5haEd0vCGDvEpVQWUuuN-Sg7j","https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/i/99b0b4b2-1ec2-42db-8d72-689653733407/danin3f-73b4101b-bed7-402e-af3e-4346596d8520.png","https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTgFwmNmWjfhEOAMuIeBnWHn1TSkQaYGqIpFPWO7ZF4cP4EWSNh","https://cdn.myanimelist.net/r/334x484/images/anime/8/38155.webp?s=f19598de1939c18a48eb770b8b3e38ae","https://cdn.myanimelist.net/r/334x484/images/anime/3/82149.webp?s=405fe22c769fb6ebe070dc42cc8f119f","https://cdn.myanimelist.net/r/334x484/images/anime/13/44844.webp?s=7e25ba9174343b0d2c62fdd1f09d3f86","https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTCFvCiFvi16e9O25HrXOna0R-McZb_Md2MWmGgtr8cFRX16m7i","https://cdn.myanimelist.net/r/334x484/images/anime/13/22128.webp?s=88f15c4f285c474f1e69b59034ba8550","https://cdn.myanimelist.net/r/334x484/images/anime/11/39717.webp?s=e696c09db680ad3e06b37866f0021eaa","https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcR4jJqVNFlMKNNmuq2JNJRmSVE_-CQeGOrq7-DU2E_9X8D09ksf","https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcT9_u3fGcwbIGwOmZr-ZDTi3K4cI62tiaREOKqG444W0e8xhiHf","https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQH2vz6zt5l7z_AkNygsCdRqCj27AOUfRJX_GJEfvOondTU7JDv","https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQ7IOp8Dk7SPaNeOZLHWWZ3lRzUhDom3HzkaLOk_Bs_thhJSLE1","https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRbQSRjQsgDMpC9H6wJUanCRqv6TllbsL0KL6aJQQJgGodtAgNm","https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSpTRPfNnOqy9fROd6C9RqZ4gvbMf3pW5tB0iCjOJRMVizrMcSF","https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQfR6PJI6PZ__dpF_GCKyQ9MFv20dwjT3znD3dh1HkCfUeahY5t","https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRsPWIQei5cZnOJJ3PC_mldPkWDkXKaDX-0W0g8mPdajBPsmZXB","https://upload.wikimedia.org/wikipedia/en/thumb/e/ed/SchoolDays.png/220px-SchoolDays.png","https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSdnifWTQAGqHq81pKZRX1kfQTBPWtRQEB_zaj-NmiXJkXFuF4Y","https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcToazhVyUMqwYhYY8fFJH9DCimOQ0rO2dGIRn3FKdMXr4642SIt","https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTGoJE_4nkjG-wnzd1Rschk1ONdTDTlus0d6JLfbEkuz9cB3Pym","https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQsORDtUnIUgT6JJIobEyQfQR5FyYZ7kWVJ4Zfl8cBmG97pz0L4","https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQdEZOmwn3ymgwSe-wlAu1-Cyc0YNFoTrvVd59JqUem-9a--OeQ","https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTrk9OYu1QihiUraMWrq2D_yp7gBac3WiGHLJdt-hyWBa_nw0Jx","https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRnXNToeYrpNhlb5gZHw2AE_DbLVx56HmXKYEnxbpACwxsCN1K6","https://images-na.ssl-images-amazon.com/images/I/71Oxv-X-4JL._SY445_.jpg","https://m.media-amazon.com/images/M/MV5BMjUxMzE4ZDctODNjMS00MzIwLThjNDktODkwYjc5YWU0MDc0XkEyXkFqcGdeQXVyNjc3OTE4Nzk@._V1_QL50_.jpg","https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTEhSEzOfKNttdVKATohyZDhyaWpPQl8fct_e0PUx_RTtDV_DCT","https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcS_IdUCXN0MCn4nA5TL1VW5si2BvJyr66MFrIznFZcORZv9An7Y","https://upload.wikimedia.org/wikipedia/en/e/e5/Plastic_Memories_DVD_Vol_1.jpg","https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQz6KIXdfjU8sdbu6MV58unaTLn1TrM1LJztGl9wGBbOj0JCZm0","https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQEK6PMNjVxC3Ch_n_XFPBwnMGosOvPMisJmMrqsh2CHG40LD1F","http://i.imgur.com/nSSdKns.jpg")
            imgs=random.choice(rom)
            
            embed.set_image(
                url=imgs
            )
            embed.set_footer(text=f"{ctx.guild}", icon_url=f"{ctx.guild.icon_url}")
          
            await ctx.send(embed=embed)
            if imgs == "https://i.ytimg.com/vi/HG_xsxSvTn4/maxresdefault.jpg":
                await ctx.send("Shinmai Maou no Testament")
        else :
            await ctx.send("Sorry i am a weeb myself but i dont know anything about that genre yet sorry bud.(only romance i know so far)")
"""
### dISCONTINUED !

@bot.command(pass_context=True, aliases=['prog','code'])
async def rust(ctx, * , reason =None):
    if str(ctx.channel) in rust_ctrl:
        if reason == None:
            await ctx.send("```rs\n1.Basic print! statement\n2.How to declare variables(i32 example)\n3.How to declare functions\n4.How to pass arguments in functions\n5.How to return values from functions\n6.If-Else in rust( if , else )\n7.Loop\n8.while loop ```")
        if reason == "hello" or reason == 'Hello' or reason =='1' or reason == '1.':
            await ctx.send("```rs\nfn main(){\n\tprintln!('hello_world'); \n}```");
        if reason == '2.' or reason == '2':
            await ctx.send("```rs\nfn main(){\n\tlet n = 10;\n\tlet p:i32 = 20;\n\tprintln!(' n = {} and p = {}',n,p);\n}```")
        if reason == '3.' or reason == '3':
            await ctx.send("```rs\nfn main(){\n\tdisp();\n}\nfn disp(){\n\tprintln!(' Disp function called');\n}```")
        if reason== '4.' or reason == '4':
            await ctx.send("```rs\nfn main(){\n\tsum(5,10);\n}\nfn sum( x:i32 , y:i32 ){\n\tprintln!(' Sum of {} and {} is {} ',x,y,x+y);\n}```")
        if reason == '5' or reason == '5.':
            await ctx.send("```rs\nfn main(){\n\tlet n:i32 = sum(5,10);\n\tprintln!(' sum = {}',n);\n}\nfn sum( x:i32 , y:i32 ) -> i32 { x+y }```")
        if reason == '6' or reason == '6.':
            await ctx.send("```rs\nfn main(){\n\tlet n = 1; \n\t if n==1{\n\tprint!(' if');\n\t\t}\n\telse{\n\tprint!(' else');\n\t\t}\n}```")
        if reason == '7' or reason == '7.':
            await ctx.send("```rs\nfn main(){\n\tlet mut n = 1;\n\tloop {\n\t\tn = n+1;\n\t\tprint!( ' Hi');\n\t\tif n==5 { break; }  \n}```")
        if reason == '8' or reason == '8.':
            await ctx.send("```rs\nfn main(){\n\tlet mut n = 1;\n\tn = n+1;\n\twhile n==5 {\n\t\t print!(' Hi ');\n\t} \n}```")
"""     




@bot.event
async def on_ready():
    print("Logged in as: " + bot.user.name + "\n")
    return await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching , name=f"Prefix is '{prefex}'"))
    
    

#welcome event
@bot.event
async def on_member_join(member):
    embed = discord.Embed(title="",
                        description= f"Welcome to Weeb Smasher's official Discord server \nWOW! now we have {len(list(member.guild.members))} member in our Weeb's family!!!\nIf you need any help ask our moderators" ,
                        color=0xe01aa1)
    embed.set_thumbnail(url= f"{member.avatar_url}")
    embed.set_author(name=f"{member.name}", icon_url=f"{member.avatar_url}")
    embed.set_footer(text=f"{member.guild}", icon_url=f"{member.guild.icon_url}")
    

    channel = bot.get_channel(id=wlcm)

    await channel.send(embed=embed)

@bot.event
async def on_member_remove(member):
    embed = discord.Embed(title="",
                        description= f"{member.name} Left us \nnow we have {len(list(member.guild.members))} member left in our Crimanu family!!!\nHope he came back soon" ,
                        color=0xe01aa1)
    embed.set_thumbnail(url= f"{member.avatar_url}")
    embed.set_author(name=f"{member.name}", icon_url=f"{member.avatar_url}")
    embed.set_footer(text=f"{member.guild}", icon_url=f"{member.guild.icon_url}")
    

    channel = bot.get_channel(id=wlcm)

    await channel.send(embed=embed)

#help giveaway
@bot.command(pass_context = True, aliases = ["help-giveaway","giveaway-help","give-away"])
async def giveaway(ctx):
    await ctx.send("```Here are some commands for give away bot.....\ninitiate - use to initiate giveaway.\npart - to take part in giveaways.\napplied - to check who applied till now.\nremove - to remove spammers\nwinners - to declare winners obviously\n***All results are random***```")


#give away bot
@bot.command()
async def part(ctx, * , reason =None):
    if reason == None:
        await ctx.send(f"```Pls enter your user name.......```")
    elif list1.count(reason)>=1 or list2.count(ctx.message.author.mention)>=1:
        await ctx.send(f"```your name is allready here in list.......```")
    else:
        list1.append(reason)
        list2.append(ctx.message.author.mention)
        await ctx.send(f"{ctx.message.author.mention}```Congratulations {reason} now you are part of giveaway\nWOW! Now there {len(list1)} ppls are part of this giveaway.```")
#give away aplicants
@bot.command()
async def applied(ctx):
    if ctx.message.author.guild_permissions.kick_members:
        await ctx.send(f"```Given names --- {list1}```\nDiscord names --- {list2}")
    else:
        await ctx.send(f"```Sorry!... You won't seems to have permission to see this```")
#give away delete names
@bot.command()
async def remove(ctx, * , reason=None):
    if reason == None:
        await ctx.send("Remove whome from giveaway!")
    elif ctx.message.author.guild_permissions.kick_members:
        list1.remove(reason)
        await ctx.send(f"{ctx.message.author.mention} removed {reason}\nNow {reason} is not a part of giveaway anymore.....")
    else:
        await ctx.send("Sorry you can't do this")
@bot.command()
async def initiate(ctx, * , reason =None):
    if ctx.message.author.guild_permissions.kick_members:
        await ctx.send(f"@everyone a giveaway has been started by {ctx.message.author.mention} don't miss it")
        list1.clear()
        list2.clear()
    else:
        await ctx.send("You cant initiate giveaways sorry.....")
@bot.command(pass_context = True, aliases = ["winer","winners"])
async def winner(ctx , * , number:int=None ):
    if ctx.message.author.guild_permissions.kick_members:
        if number is None :
            await ctx.send("At least gimme the no of winners you want")
        else:
            down = 0
            down = number
            while(down != 0):
                down = down - 1
                num = len(list1)
                ran=random.choice(list1)
                list1.remove(ran)
                await ctx.send(f"```congratulations '{ran}' you won```")
    else:
        await ctx.send("You cant decide winners 'LMAO'")

#hello
@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello")


#new video brod
@bot.command(pass_context=True, aliases=['sugg'])
async def suggest(ctx, * , reason =None):
    channel = bot.get_channel(id= suggest_vid)
    await channel.send(f"{ctx.message.author.mention}```has give his suggestions   \nHe suggested.....\n\n{reason}```")



#flip
@bot.command(pass_context=True, aliases=['toss'])
async def flip(ctx):
    coin = ('Head','Tail')
    toss = random.choice(coin)
    if toss == 'Tail':
            embed = discord.Embed(title="Coin toss",
                                description=f'Lemme roll a coin for: \n{ctx.message.author}',
                                color=0xFFF700) 
            embed.set_thumbnail(
                url="https://cdn0.iconfinder.com/data/icons/football-34/64/coin-risky-money-flip-512.png"
            )
            embed.set_image(
                url='https://randomster.com/img/tail.png'
            )
            embed.set_footer(text=f"{ctx.guild}", icon_url=f"{ctx.guild.icon_url}")
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)
    elif toss == 'Head':
            embed = discord.Embed(title="Coin toss",
                                description=f'Lemme roll a coin for: \n{ctx.message.author}\nCongratulations you got',
                                color=0xFFF700) 
            embed.set_thumbnail(
                url="https://cdn0.iconfinder.com/data/icons/football-34/64/coin-risky-money-flip-512.png"
            )
            embed.set_image(
                url='https://randomster.com/img/head.png'
            )
            embed.set_footer(text=f"{ctx.guild}", icon_url=f"{ctx.guild.icon_url}")
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)


#dice
@bot.command(pass_context=True, aliases=['roll'])
async def dice(ctx):
    coin = ('1','2','3','4','5','6')
    toss = random.choice(coin)

    embed = discord.Embed(title="Rollong dice.....",
                              description=f'You got....',
                              color=0xF91CD4) 
    embed.set_thumbnail(
        url="https://i.ibb.co/cJbxM3V/dice-fire.png"
    )
    if toss == '1':
        embed.set_image(
            url="https://i.ibb.co/gvdzcf1/dice-six-faces-one.png"
        )
    elif toss == '2':
        embed.set_image(
            url="https://i.ibb.co/Mpz5W1Q/dice-six-faces-two.png"
        )
    elif toss == '3':
        embed.set_image(
            url="https://i.ibb.co/3TmXq5b/dice-six-faces-three.png"
        )
    elif toss == '4':
        embed.set_image(
            url="https://i.ibb.co/rGzgFsT/dice-six-faces-four.png"
        )
    elif toss == '5':
        embed.set_image(
            url="https://i.ibb.co/T8rXWdS/dice-six-faces-five.png"
        )
    elif toss == '6':
        embed.set_image(
            url="https://i.ibb.co/c67dhRH/dice-six-faces-six.png"
        )
    embed.set_footer(text=f"{ctx.guild}", icon_url=f"{ctx.guild.icon_url}")
    embed.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=embed)

    

#hi
@bot.command()
async def hi(ctx):
    await ctx.send(f"hi")

#Help command
@bot.command(pass_context=True, aliases=['h'])
async def Help(ctx):
    if str(ctx.channel) in ctp:
        clr=(0x00b3ff,0xff1f1f,0xff1ff8,0x141cff,0x14ffb1,0x67ff14,0xffe014,0xff1814)
        clrs=random.choice(clr)
        embed = discord.Embed(title="This is CTP guide bot",
                              description='The prefix for Bot is " . " ',
                              color=clrs)
        embed.set_thumbnail(
            url="https://pngimage.net/wp-content/uploads/2018/06/guide-png-4.png"
        )
        embed.add_field(name='C.T.P.', value="There are 12 different type of CTP's \nIf you want to know about any particular ctp just type its name using prefex",inline=False)
        embed.add_field(name="Names of CTP ",value="Judgement - '.j' , '.judgement'\nGreed - '.g' , '.greed'\nInsight - '.i' , '.insight'\nRage - '.rage' , '.r',.r\nEnergy - '.energy' , '.e'\nRegenration - '.regenration' , '.regen'\nAuthority - '.authority' , '.a'\n"
                                                   "Destruction - '.destruction' , '.d'\nRefinement - '.refinement' , '.ref'\nTranscendence - '.transcendence' , '.trans'\n"
                                                   "Patience - '.patience' , '.p'\nVeteran - '.veteran' , '.v'\nLocation of ctp - '.location' , '.l'", inline=False)
        embed.add_field(name='CTP Chest',value="You can try your luck by rolling one of those ctp chest keep in mind No ctp of veteren is there in it \nUse '.ctp'",inline=False)
        await ctx.send(embed=embed)
    elif str(ctx.channel) in memes_ctrl:
        await ctx.send(f"```Hello this is meme command center here are some of commands that you can use\n\nmeme - will show a hot meme of day\nanime - Hot anime memes"
                       f"\nmarvel - ofcz marvel memes```")
    elif str(ctx.channel) in wike:
        await ctx.send(f"```Hello this is wikipedia here you can ask or search in wikipedia\nExample- wanna know about marvel \nType '.wiki animes'```")
    elif str(ctx.channel) in uru_guide:
        await ctx.send(f"```Hello this is odin's blessing help book.....\nPefix = '{prefex}'\nodin - to open odin box\nuru/ob blessing_name - to know about particular blessing\n(example - to know about heal '.uru heal')\nname - to know names of odin blessings if you dont know```")
    else :
        await ctx.send(f"```Hello everyone this is help command\nuse prefix as '{prefex}' and try commands\n\n'For memes goto #memes\n'for ctp guide goto #ctp-guide'\n\nFor giveaway help type 'giveaway'\n@men = @mentions\nres = reasion for that task\n\n"
                       f"slap @men- the bot will slap for you\nslap @men res-to give reason\npunch @men- bot will punch min for you\npunch @men res-to give reasion "
                       f"\nkill @men- no words\nkill @men res- reason for kil####\nslam @men-bot will slam\n\n'want to give us suggestions why not'\nsuggest/sugg <your suggestion> - this will record your suggestion\n\n'You can throw things too'\nthrow res @men- bot will throw res @men\nflip/toss - will flip a coin"
                       f"\ndice/roll - will roll a dice for you"
                       f"\n\nThere are some more commands like\n[users, hello, hi, say, call ] \n\ncast- broadcast/announcments \nnew- new video ```")

#repeat command
@bot.command()
async def wiki(ctx, * , reason =None):
    if str(ctx.channel) in wike:
        q = wikipedia.summary(reason, sentences=3)

        embed = discord.Embed(title=f"{reason}",
                              description=f"{ctx.message.author} i searched about '{reason}' and here are the results of my search....\n\n{q}",
                              color=0xAFB6FF) 
        embed.set_thumbnail(
            url="https://i.ibb.co/bLRMh37/kisspng-wikipedia-logo-online-encyclopedia-wikimedia-found-que-5ada2ad0a3a446-7771588615242472486703.png"
        )

        embed.set_footer(text=f"{ctx.guild}", icon_url=f"{ctx.guild.icon_url}")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)

#new video brod
@bot.command()
async def new(ctx, * , reason =None):
    channel = bot.get_channel(id=newvideo)
    if str(ctx.author) in valid_users:
        await channel.send(f"```Wow a new video has come \nLet's watch together......```\n{reason}")

#new announcement
@bot.command()
async def cast(ctx, * , reason =None):
    channel = bot.get_channel(id=anouncement)
    if str(ctx.author) in valid_users:
        embed = discord.Embed(title="Important Announcement ",
                              description=f"{reason}",
                              color=0xe01aa1)
        embed.timestamp = datetime.datetime.utcnow()
        await channel.send(embed=embed)

#delete message command
@bot.command(pass_context=True, aliases=['clear'])
async def delete(ctx , * , number:int=None ):
    if ctx.message.author.guild_permissions.manage_messages:
        try:
            if number is None:
                await ctx.send("You must input a number")
            else:
                delete = await ctx.message.channel.purge(limit=number+1)
                await ctx.send(f"{number} Messages deleted by {ctx.message.author}")
        except:
            await ctx.send("I can't delete messages here")
    else:
        await ctx.send("You don't have permission for this.")

#kick user command
@bot.command()
async def kick(ctx , user: discord.Member, * , reason =None ):
    try:
        if user.guild_permissions.manage_messages:
            await ctx.send("I can't kick admins or moderators")
        elif ctx.message.author.guild_permissions.kick_members:
            if reason is None:
                await ctx.guild.kick(user=user , reason='None')
                await ctx.send(f"{user} has been kicked.")
            else:
                await ctx.guild.kick(user=user, reason=reason)
                await ctx.send(f"{user} has been kicked {reason}.")
        else:
            await ctx.send("You don't have permissions for this.")
    except:
        await ctx.send("Enter the name of person you want to kick.")

#slap command
@bot.command()
async  def slap(ctx,user:discord.Member,*,reason =None):
    if reason is None:
        await ctx.send(f"{ctx.message.author.mention} slapped {user} for no reason")
    else:
        await ctx.send(f"{ctx.message.author.mention} slapped {user} {reason}")

#punch command
@bot.command()
async  def punch(ctx,user:discord.Member,*,reason =None):
    if reason is None:
        await ctx.send(f"{ctx.message.author.mention} punched {user} for no reason")
    else:
        await ctx.send(f"{ctx.message.author.mention} punched {user} {reason}")

@bot.command()
async  def call(ctx,user:discord.Member,*,reason =None):
    if reason is None:
        await ctx.send(f"```{user} Get your ass here punk.```")
    else:
        await ctx.send(f"```{user} Get your ass here punk {reason}.```")

#kill command
@bot.command()
async  def kill(ctx,user:discord.Member,*,reason =None):
    if reason is None:
        await ctx.send(f"{ctx.message.author.mention} is trying to kill {user} for no reason")
    else:
        await ctx.send(f"{ctx.message.author.mention} is trying to kill {user} {reason}")

#slam command
@bot.command()
async  def slam(ctx,user:discord.Member,*,reason =None):
    if reason is None:
        await ctx.send(f"{ctx.message.author.mention} slammed {user} for no reason")
    else:
        await ctx.send(f"{ctx.message.author.mention} slammed {user} {reason}")

#throw command
@bot.command()
async  def throw(ctx,reason =None,*,user:discord.Member):
    if reason is None:
        await ctx.send(f"{ctx.message.author.mention} is throwing nothing at {user} ")
    else:
        await ctx.send(f"{ctx.message.author.mention} is throwing  {reason} at {user} ")

#ban user command
@bot.command()
async def ban(ctx , user: discord.Member, * , reason =None ):
    try:
        if user.guild_permissions.manage_messages:
            await ctx.send("I can't ban admins or moderators")
        elif ctx.message.author.guild_permissions.ban_members:
            if reason is None:
                await ctx.guild.ban(user=user , reason='None')
                await ctx.send(f"{user} has been baned.")
            else:
                await ctx.guild.ban(user=user, reason=reason)
                await ctx.send(f"{user} has been baned {reason}.")
        else:
            await ctx.send("You don't have permissions for this.")
    except:
        await ctx.send("Enter the name of person you want to ban.")



bot.add_cog(AIMLS(bot))
bot.add_cog(Reddit(bot))
bot.add_cog(INFO(bot))
bot.add_cog(URUS(bot))
bot.add_cog(CTPS(bot))
bot.add_cog(Adult(bot))
bot.add_cog(Meme(bot))
bot.add_cog(Music(bot))
bot.run(token)

