import discord
from discord.ext import commands
import random
import datetime

ctp = ["ctp-guide"]

class CTPS(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def CTP(self,ctx):
        if str(ctx.channel) in ctp:
            embed = discord.Embed(title="You opened ctp chest",
                                description='Congratulations you got....',
                                color=0x541212)
            img=("https://images-ext-2.discordapp.net/external/YfVV20vl6Mj_Q4XLOmJm1nCrAWF8eFoqj4leIsURCYE/https/i.imgur.com/etw0hUL.png","https://images-ext-1.discordapp.net/external/YklWbDTPoe6AeXiArE7a0p4Lh93r0Fy5f6ghRlSdyZA/https/i.imgur.com/eVtYF8p.png","https://images-ext-2.discordapp.net/external/_5DOwPLfHgA2DvDWveGwe7i8sUkmcvsIEyf4hBBNnjc/https/i.imgur.com/75XVqes.png","https://images-ext-1.discordapp.net/external/_68_kCWy02q6RnGwVsMfMegZP8Qag2egsjqbxf5sBH4/https/i.imgur.com/J7dVhbw.png","https://images-ext-1.discordapp.net/external/VAwn2iQV-Gf9jCB2CqCbDA5G50kvJ1UWjR0GJq0L17s/https/i.imgur.com/IBIsuaE.png","https://images-ext-2.discordapp.net/external/Kn9aMzYw6CqpNshTkL__QLX_fJAFS-42ufMM-y1gWgA/https/i.imgur.com/TRsLAIl.png","https://images-ext-2.discordapp.net/external/Qj2h-IAyrHx7fbFyeVM397nyyu-VlmVrhgs6TrmOj4g/https/i.imgur.com/7K0Xz07.png","https://images-ext-2.discordapp.net/external/l13EMZL0jlp4vqI-dIdK0PlDV1_Z7XFXXQEg_lLGuQg/https/i.imgur.com/jYiGknu.png","https://images-ext-2.discordapp.net/external/uIcnLNGQHL_PUM99p83tca-ijFLjBdk3X1pg_mlNx6M/https/i.imgur.com/ylLLge9.png","https://images-ext-1.discordapp.net/external/xFgl3XSvluPfW-DezQ4Lwx--Pu5FIEnoIw04Ew54DI8/https/i.imgur.com/T6ryvUs.png","https://images-ext-1.discordapp.net/external/C8-VixGH4g8lfBwq9KUvFeJki44o-F2-qgW8tVZbF2E/https/i.imgur.com/Wp5xlsy.png")
            embed.set_thumbnail(
                url="https://i.ibb.co/BVS2CGM/ctp.png"
            )
            imgs=random.choice(img)
            embed.set_image(
                url=imgs
            )
            embed.set_footer(text=f"{ctx.guild}", icon_url=f"{ctx.guild.icon_url}")
            embed.timestamp = datetime.datetime.utcnow()

            await ctx.send(embed=embed)

            #ctp of greed
    @commands.command(pass_context=True, aliases=['g'])
    async def Greed(self,ctx):
        if str(ctx.channel) in ctp:
            embed = discord.Embed(title="CTP of Greed",
                                description="This is a good pve ctp. This ctp is good for characters like (thanos,jean..) as this ctp works good in both pvp and sometimes as well as pve content.",
                                color=0x55B80B)
            embed.set_thumbnail(url="https://images-ext-2.discordapp.net/external/l13EMZL0jlp4vqI-dIdK0PlDV1_Z7XFXXQEg_lLGuQg/https/i.imgur.com/jYiGknu.png")
            embed.add_field(name="Location", value='Custom Gear Chest, Selector: CTP (Advanced/New)', inline = False)
            embed.add_field(name='Stats at Maximum Roll', value ='• Applies to: Self\nGuard Break Immunity \n• Ignore Dodge +45%\n• Applies to: Self % chance when attacking \nApplies to: Self \n10% recovery of Max HP.\n150% increase to damage against COMBAT, BLAST-type characters. (5 sec.)\n150% increase to damage against SPEED, UNIVERSAL-type characters. (5 sec.)\n(Activates Damage increase effect in turn.)\nCooldown Time 12 seconds', inline=False)
            embed.set_footer(text=f"{ctx.guild}", icon_url=f"{ctx.guild.icon_url}")
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)

    @commands.command(pass_context=True, aliases=['j','judge','judgemen'])
    async def Judgement(self,ctx):
        if str(ctx.channel) in ctp:
            embed = discord.Embed(title="CTP of Judgement",
                                description="An extremely powerful CTP for Pve characters with all attack and chain hit for characters  whose damage is based on elemental attacks (i.e. cyclops,luna snow etc) Lacks the ignore boss defence like rage so might be bad for characters like namor for in abx/wbu boosts the damage for 5sec on any skill with element better than energy atk but not better than rage for elemental characters",
                                color=0x010846)
            embed.set_thumbnail(url="https://images-ext-2.discordapp.net/external/uIcnLNGQHL_PUM99p83tca-ijFLjBdk3X1pg_mlNx6M/https/i.imgur.com/ylLLge9.png")
            embed.add_field(name="Location", value='Custom Gear Chest, Selector: CTP (Advanced/New)', inline = False)
            embed.add_field(name='Stats at Maximum Roll', value ='• Applies to: Self\n• All Attacks +32% \n• Chain Hit Damage Dealt +20%\n• Activation Rate: 10% chance when attacking\nApplies to: Enemies \nDecreases All Resistance by 30%. (5 sec.)\nApplies to: Self\nIncreased damage to all element damage by +200%. (5 sec.)\nCooldown Time 7 seconds', inline=False)
            embed.set_footer(text=f"{ctx.guild}", icon_url=f"{ctx.guild.icon_url}")
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)

    @commands.command(pass_context=True, aliases=['i','in','sight'])
    async def insight(self,ctx):
        if str(ctx.channel) in ctp:
            embed = discord.Embed(title="CTP of Insight",
                                description="Could be useful in pve game modes where you can add damage by having this obelisk on a support character or even a character with a good leadership Against world boss or Shadowland,  ABX\nThere maybe some usefulness maybe in PVP as well Except the fact that it doesn't have itgb",
                                color=0x5D0B6D)
            embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/xFgl3XSvluPfW-DezQ4Lwx--Pu5FIEnoIw04Ew54DI8/https/i.imgur.com/T6ryvUs.png")
            embed.add_field(name="Location", value='Custom Gear Chest, Selector: CTP (Advanced/New)', inline = False)
            embed.add_field(name='Stats at Maximum Roll', value ='• Max HP +34%\n• All Defense +39%\n• Activation Rate: 10% chance when attacking\n• Applies to: All Allies \nIncreases damage dealt to SUPER HERO-type characters by 20%. (5 sec.)\nIncreases damage dealt to SUPER VILLAIN-type characters by 20%. (5 sec.)\n(The effect that applies to all team members cannot be applied in duplicate.)\nCooldown Time 7 seconds', inline=False)
            embed.set_footer(text=f"{ctx.guild}", icon_url=f"{ctx.guild.icon_url}")
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)

    #ctp of energy
    @commands.command(pass_context=True, aliases=['e'])
    async def Energy(self,ctx):
        if str(ctx.channel) in ctp:
            embed = discord.Embed(title="CTP of Energy",
                                description="Good for any kind of character especially those who can cancel their skill without make the animation stopped. The Ignore Dodge stat is very good to help character fight against bosses with high Dodge rate such as Frost Beast in ABX Speed Villain/Hero or Corvus Glaive WBU",
                                color=0xff0000)
            embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/C8-VixGH4g8lfBwq9KUvFeJki44o-F2-qgW8tVZbF2E/https/i.imgur.com/Wp5xlsy.png")
            embed.add_field(name="Location", value='Cinematic Battle Reward(Mythic Hela, Killmonger), Story Mission 13 - 8 First Clear Reward, Custom Gear Chest', inline = False)
            embed.add_field(name='Stats at Maximum Roll', value ='• Ignore Dodge + 45 % \n• Critical Damage ↑ +45 % \n• Activation Rate: 10 % chance when attacking \nApplies to: Self Increases Chain Hit damage by 30 % when attacking.(5 sec.) Increases damage by 200 % for 1 attack(s).(5 sec.) Cooldown Time 7 seconds', inline=False)
            embed.set_footer(text=f"{ctx.guild}", icon_url=f"{ctx.guild.icon_url}")
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)

    #ctp of rage
    @commands.command(pass_context=True, aliases=['r'])
    async def Rage(self,ctx):
        if str(ctx.channel) in ctp:
            embed = discord.Embed(title="CTP of Rage",
                                description="This CTP has special damage proc buff that allow your character to receive Increases"
                                            " Damage buff for any skill when proc is activated. Therefore this CTP will be very great "
                                            "for character who can deal decent damage from all of their skill. Obviously CTP of Rage is not "
                                            "suitable for character who focusing their damage to one skill only (i.e Sharon Rogers, Gambit)",
                                color=0xee00ff)
            embed.set_thumbnail(url="https://images-ext-2.discordapp.net/external/Qj2h-IAyrHx7fbFyeVM397nyyu-VlmVrhgs6TrmOj4g/https/i.imgur.com/7K0Xz07.png")
            embed.add_field(name="Location", value='custom Gear Chest, Legendary battle - Thanos type 6', inline = False)
            embed.add_field(name="Stats at Maximum Roll", value ="• Critical Rate ↑ +32%\n• Dodge ↑ +32%\n• Activation Rate: 20% chance when dealing critical attack \nApplies to: Self Ignores Boss's Damage Decrease by 60% (5 sec.) Increases 0.9% damage per 1% of Dodge Rate and Critical Rate, regardless of Guaranteed Dodge Rate and Guaranteed Critical Rate (5 sec.) Cooldown Time 7 seconds'", inline=False)
            embed.set_footer(text=f"{ctx.guild}", icon_url=f"{ctx.guild.icon_url}")
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)

    #ctp of regenration
    @commands.command(pass_context=True, aliases=['reg', 'regen'])
    async def Regenration(self,ctx):
        if str(ctx.channel) in ctp:
            embed = discord.Embed(title="CTP of Regenration",
                                description="Made for PvP character due to its defensive stat. It is best to give this CTP to character "
                                            "who has healing ability either as passive or active skill.",
                                color=0x15a80b)
            embed.set_thumbnail(
                url="https://images-ext-2.discordapp.net/external/Kn9aMzYw6CqpNshTkL__QLX_fJAFS-42ufMM-y1gWgA/https/i.imgur.com/TRsLAIl.png")
            embed.add_field(name="Location", value='custom Gear Chest, Carol type 6', inline=False)
            embed.add_field(name="Stats at Maximum Roll",
                            value="• Max HP ↑ +34% \n• Guard Break Immunity, Increase HP Regen by 90% \n• Activation Rate: when HP is below 50% \nGenerates a Shield that is 35% of Max HP and ignores Cancel and Pierce effects (5 sec.) Recover 10% of Max HP Cooldown Time 10 seconds",
                            inline=False)
            embed.set_footer(text=f"{ctx.guild}", icon_url=f"{ctx.guild.icon_url}")
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)

    #ctp of authority
    @commands.command(pass_context=True, aliases=['a', 'auth'])
    async def authority(self,ctx):
        if str(ctx.channel) in ctp:
            embed = discord.Embed(title="CTP of Authority",
                                description="A defensive version of CTP of Destruction, but without buff to pierce through defensive skill. "
                                            "Which makes this CTP only works for character who already has an ability to pierce. The offensive stat"
                                            " given might help character with low damage to kill enemy faster.",
                                color=0xf9dd24)
            embed.set_thumbnail(
                url="https://images-ext-1.discordapp.net/external/VAwn2iQV-Gf9jCB2CqCbDA5G50kvJ1UWjR0GJq0L17s/https/i.imgur.com/IBIsuaE.png")
            embed.add_field(name="Location", value='custom Gear Chest', inline=False)
            embed.add_field(name="Stats at Maximum Roll",
                            value="• Applies to: Self Guard Break Immunity \n• Critical Damage ↑ +45% \n• Activation Rate: when HP is below 50%: \nApplies to: Self Accumulates 100% of True Damage regardless of Defense and Dodge stats. The total true damage accumulated cannot exceed 10% of HP. (7 sec.) Increases Attack by +5% for each 1% of damage taken. (7 sec.) Invincible (5 sec.) Cooldown Time 10 seconds",
                            inline=False)
            embed.set_footer(text=f"{ctx.guild}", icon_url=f"{ctx.guild.icon_url}")
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)

    #ctp of destruction
    @commands.command(pass_context=True, aliases=['des', 'd'])
    async def destruction(self,ctx):
        if str(ctx.channel) in ctp:
            embed = discord.Embed(title="CTP of Destruction",
                                description="A hybrid CTP, providing stat for both PvP and PvE mode. Extremely good for character with high "
                                            "survivability but lacking ability to pierce through defensive buff. The Increase Damage buff will "
                                            "help character to compete in PvE mode as well.",
                                color=0xe01aa1)
            embed.set_thumbnail(
                url="https://images-ext-1.discordapp.net/external/_68_kCWy02q6RnGwVsMfMegZP8Qag2egsjqbxf5sBH4/https/i.imgur.com/J7dVhbw.png")
            embed.add_field(name="Location", value='custom Gear Chest', inline=False)
            embed.add_field(name="Stats at Maximum Roll",
                            value="• Critical Damage ↑ +45% \n• Applies to: Self \nGuard Break Immunity \n• Activation Rate: 10% chance when attacking \nApplies to: Self 30% chance to penetrate with SUPER ARMOR, BARRIER, ALL DAMAGE IMMUNE, INVINCIBLE effect. (5 sec.) Increases damage by 200% for 1 attack(s). (5 sec.) Cooldown Time 7 seconds ",
                            inline=False)
            embed.set_footer(text=f"{ctx.guild}", icon_url=f"{ctx.guild.icon_url}")
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)



    #ctp of refinement
    @commands.command(pass_context=True, aliases=['ref', 'refine'])
    async def refinement(self,ctx):
        if str(ctx.channel) in ctp:
            embed = discord.Embed(title="CTP of Refinement",
                                description="With the Max HP stat and Recovery ability provided, this CTP is good for character who has high defense against"
                                        " certain attack but lack of ability to heal. But due to the absence of Immunity to Guard Break, this CTP is not suitable for PvP metas",
                                color=0xb5215c)
            embed.set_thumbnail(
                url="https://images-ext-2.discordapp.net/external/_5DOwPLfHgA2DvDWveGwe7i8sUkmcvsIEyf4hBBNnjc/https/i.imgur.com/75XVqes.png")
            embed.add_field(name="Location", value='Cinematic Battle Reward (Mythic Hulk, Shuri), Custom Gear Chest', inline=False)
            embed.add_field(name="Stats at Maximum Roll",
                            value="• Max HP ↑ +34% \n• Recovery Rate ↑ +90% \n• Activation Rate: when HP is below 50% \nApplies to: Self\nGuard against 6 hits (6 sec.) 20% Recovery of MAX HP.Cooldown Time 15 seconds",
                            inline=False)
            embed.set_footer(text=f"{ctx.guild}", icon_url=f"{ctx.guild.icon_url}")
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)


    #ctp of veteran
    @commands.command(pass_context=True, aliases=['vet', 'v'])
    async def veteran(self,ctx):
        if str(ctx.channel) in ctp:
            embed = discord.Embed(title="CTP of Veteran",
                                description="Hard to find but domination of all. It make a character god tier",
                                color=0xe4b91b)
            embed.set_thumbnail(
                url="https://images-ext-1.discordapp.net/external/-iTWZP55z2MjhN9c0V83cwiD90QIsqNHzySDuX2IaYs/https/i.imgur.com/CcJgA5g.png")
            embed.add_field(name="Location", value="Collector's Vault Event", inline=False)
            embed.add_field(name="Stats at Maximum Roll",
                            value="• Guard Break Immunity, Ignore Dodge, Critical Damage Increase +32% \n• Increases All Attacks and Defense +28% \n• Activation Rate: 15% chance when attacking\nApplies to: Self\nIncreases Chain Hit Damage by 40% when attacking. (5 sec.)Creates a Shield that is 30% of Max HP and ignores Cancel and Pierce effects. (3 sec.)Increases damage by 150% for 1 attack(s). (5 sec.)Cooldown Time 7 seconds",
                            inline=False)
            embed.set_footer(text=f"{ctx.guild}", icon_url=f"{ctx.guild.icon_url}")
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)



    #ctp of transcendence
    @commands.command(pass_context=True, aliases=['t', 'trans'])
    async def transcendence(self,ctx):
        if str(ctx.channel) in ctp:
            embed = discord.Embed(title="CTP of Transcendence",
                                description="With the All Attack stat provided, this CTP is good for character who uses summon/clone as main damage dealer."
                                        " But due to the absence of Immunity to Guard Break, this CTP is not suitable for PvP metas.",
                                color=0x1394f6)
            embed.set_thumbnail(
                url="https://images-ext-1.discordapp.net/external/YklWbDTPoe6AeXiArE7a0p4Lh93r0Fy5f6ghRlSdyZA/https/i.imgur.com/eVtYF8p.png")
            embed.add_field(name="Location", value="Hidden Route Reward", inline=False)
            embed.add_field(name="Stats at Maximum Roll",
                            value="• All Attack ↑ +40%\n• Ignore Dodge +45%\n• Activation Rate: when HP is below 50%\nApplies to: Self\nDecreases the effect of Reflect by 50% Reflects effect(s): PHYSICAL REFLECT, ENERGY REFLECT (5 sec.) Invincible (5 sec.) Cooldown Time 10 seconds",
                            inline=False)
            embed.set_footer(text=f"{ctx.guild}", icon_url=f"{ctx.guild.icon_url}")
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)


    #ctp of Patience
    @commands.command(pass_context=True, aliases=['p','pai'])
    async def Patience(self,ctx):
        if str(ctx.channel) in ctp:
            embed = discord.Embed(title="CTP of Patience",
                                description="With the All Attack stat provided, this CTP is good for character who uses summon/clone as main damage dealer."
                                        " But due to the absence of Immunity to Guard Break, this CTP is not suitable for PvP metas.",
                                color=0x39f613)
            embed.set_thumbnail(
                url="https://images-ext-2.discordapp.net/external/YfVV20vl6Mj_Q4XLOmJm1nCrAWF8eFoqj4leIsURCYE/https/i.imgur.com/etw0hUL.png")
            embed.add_field(name="Location", value="Boost Point Stage 2 Reward", inline=False)
            embed.add_field(name="Stats at Maximum Roll",
                            value="• All Attack ↑ +40%\n• Dodge ↑ +40%\n• Activation Rate: when HP is below 50%\nApplies to: Self\nDecreases the effect of Reflect by 50% Reflects effect(s): PHYSICAL REFLECT, ENERGY REFLECT (5 sec.) Invincible (5 sec.) Cooldown Time 10 seconds",
                            inline=False)
            embed.set_footer(text=f"{ctx.guild}", icon_url=f"{ctx.guild.icon_url}")
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)

    
    @commands.command(pass_context=True, aliases=['l', 'loc'])
    async def location(self,ctx):
        if str(ctx.channel) in ctp:
            file = discord.File("cogs/MFF/ctp.jpg", filename="ctp.jpg")
            await ctx.channel.send("You can find ctp's at......",file=file)