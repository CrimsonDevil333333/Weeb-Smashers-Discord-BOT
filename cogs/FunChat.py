##############################  AIML CHAT  ##########################################

import aiml
import discord
from discord.ext import commands
import os
import random
import datetime

bot_name = ["Crimanu#5184","weeb#5184","smasher#5184","smashers#5184"]
bot_private = ["bot-spam"]

k = aiml.Kernel()
BRAIN_FILE="dump/brain.dump"
if os.path.exists(BRAIN_FILE):
    print("Loading from brain file: " + BRAIN_FILE)
    k.loadBrain(BRAIN_FILE)
else:
    print("Parsing aiml files")
    k.bootstrap(learnFiles="std-startup.aiml", commands="load aiml b")
    print("Saving brain file: " + BRAIN_FILE)
    k.saveBrain(BRAIN_FILE)

class AIMLS(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.color_codes = [0x00FFDA,0x0DFF00,0xFFEB00,0x00FFD7,0x004CFF,0xC600FF,0xFF00AA,0xFF0004,0xCF9292]

    @commands.command(pass_context=True, aliases=['bud','bro','bot'])
    async def brb(self,ctx, *, reason=None):
        if reason == None:
            await ctx.send("What ? ask me any Questions don't just brb or bro me !")
        else:
            if str(ctx.author) in bot_name:
                pass
            else:
                if str(ctx.channel) in bot_private:
                    krp = k.respond(reason)
                    s ="> **" + str(ctx.author) + "**  --> " + reason + "\n" + krp

                    embed = discord.Embed(title="Bot logs !",
                                        description=f'{str(ctx.author.name)} --> {reason}\n{krp}',
                                        color=random.choice(self.color_codes)) 
                    embed.set_thumbnail(
                        url=ctx.author.avatar_url
                    )
            
    
                    embed.set_footer(text=f"{ctx.guild}", icon_url=f"{ctx.guild.icon_url}")
                    embed.timestamp = datetime.datetime.utcnow()
                    await ctx.channel.send(s)