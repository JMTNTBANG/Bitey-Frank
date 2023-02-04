import bot
import discord
from threading import Timer
import time


def import_command():

    async def total(Interaction:discord.Interaction, messageid:str='', donottouch:bool=False):
        if donottouch == False:
            await Interaction.response.send_message('Calculating...')
        global poll
        poll = discord.Message
        if isinstance(Interaction.channel, discord.TextChannel):
            if messageid == '':
                async for message in Interaction.channel.history():
                    for embed in message.embeds:
                        if 'Poll:' in str(embed.title):
                            if 'Results' not in str(embed.title):
                                poll = message
                                pollEmbed = embed
                                break
                    if poll != discord.Message: break
            else:
                for guild in bot.client.guilds:
                    for channel in guild.text_channels:
                        async for message in channel.history():
                            if message.id == int(messageid):
                                for embed in message.embeds:
                                    if 'Poll:' in str(embed.title):
                                        if 'Results' not in str(embed.title):
                                            poll = message
                                            pollEmbed = embed
                                            break
                            if poll != discord.Message: break
                        if poll != discord.Message: break
                    if poll != discord.Message: break
            
            global oneReactors
            global twoReactors
            global threeReactors
            global fourReactors
            global fiveReactors
            global sixReactors
            global sevenReactors
            global eightReactors
            global nineReactors
            global tenReactors
            oneReactors=[]
            twoReactors=[]
            threeReactors=[]
            fourReactors=[]
            fiveReactors=[]
            sixReactors=[]
            sevenReactors=[]
            eightReactors=[]
            nineReactors=[]
            tenReactors=[]

            for reaction in message.reactions:
                if reaction.emoji == '1️⃣':
                    async for user in reaction.users():
                        if str(bot.client.user) not in str(user):
                            oneReactors.append(user)
                    
                elif reaction.emoji == '2️⃣':
                    async for user in reaction.users():
                        if str(bot.client.user) not in str(user):
                            twoReactors.append(user)
                    
                elif reaction.emoji == '3️⃣':
                    async for user in reaction.users():
                        if str(bot.client.user) not in str(user):
                            threeReactors.append(user)
                    
                elif reaction.emoji == '4️⃣':
                    async for user in reaction.users():
                        if str(bot.client.user) not in str(user):
                            fourReactors.append(user)
                    
                elif reaction.emoji == '5️⃣':
                    async for user in reaction.users():
                        if str(bot.client.user) not in str(user):
                            fiveReactors.append(user)
                    
                elif reaction.emoji == '6️⃣':
                    async for user in reaction.users():
                        if str(bot.client.user) not in str(user):
                            sixReactors.append(user)
                    
                elif reaction.emoji == '7️⃣':
                    async for user in reaction.users():
                        if str(bot.client.user) not in str(user):
                            sevenReactors.append(user)
                    
                elif reaction.emoji == '8️⃣':
                    async for user in reaction.users():
                        if str(bot.client.user) not in str(user):
                            eightReactors.append(user)
                    
                elif reaction.emoji == '9️⃣':
                    async for user in reaction.users():
                        if str(bot.client.user) not in str(user):
                            nineReactors.append(user)
                    
                elif reaction.emoji == '🔟':
                    async for user in reaction.users():
                        if str(bot.client.user) not in str(user):
                            tenReactors.append(user)
                    

            totalReactors=0
            if oneReactors: totalReactors+=len(oneReactors)
            if twoReactors: totalReactors+=len(twoReactors)
            if threeReactors: totalReactors+=len(threeReactors)
            if fourReactors: totalReactors+=len(fourReactors)
            if fiveReactors: totalReactors+=len(fiveReactors)
            if sixReactors: totalReactors+=len(sixReactors)
            if sevenReactors: totalReactors+=len(sevenReactors)
            if eightReactors: totalReactors+=len(eightReactors)
            if nineReactors: totalReactors+=len(nineReactors)
            if tenReactors: totalReactors+=len(tenReactors)

            embed=discord.Embed(
                title=f'Results for {pollEmbed.title}',
                description=f'{totalReactors} Total Participant(s)',
                color=discord.Color.green()
                ).set_author(
                    name=Interaction.user.name,
                    icon_url=Interaction.user.avatar
                )

            async def generateField(reactors, number):
                if len(oneReactors) != 0:
                    embed.add_field(
                        name=number,
                        value=f'{field["value"]} -- **{round(len(reactors)/totalReactors*100)}%** ***{len(reactors)} User(s)***',
                        inline=False
                        )
                else:
                    embed.add_field(
                        name=number,
                        value=f'{field["value"]} -- **0%** ***0 User(s)***',
                        inline=False
                        )

            for field in pollEmbed.to_dict().get('fields'):
                if field['name'] == '1️⃣':
                    await generateField(oneReactors,'1️⃣')
                elif field['name'] == '2️⃣':
                    await generateField(twoReactors,'2️⃣')
                elif field['name'] == '3️⃣':
                    await generateField(threeReactors,'3️⃣')
                elif field['name'] == '4️⃣':
                    await generateField(fourReactors,'4️⃣')
                elif field['name'] == '5️⃣':
                    await generateField(fiveReactors,'5️⃣')
                elif field['name'] == '6️⃣':
                    await generateField(sixReactors,'6️⃣')
                elif field['name'] == '7️⃣':
                    await generateField(sevenReactors,'7️⃣')
                elif field['name'] == '8️⃣':
                    await generateField(eightReactors,'8️⃣')
                elif field['name'] == '9️⃣':
                    await generateField(nineReactors,'9️⃣')
                elif field['name'] == '🔟':
                    await generateField(tenReactors,'🔟')
    
            await poll.channel.send(embed=embed)

    # Create Command Group
    pollCommands = discord.app_commands.Group(
        name='poll',
        description='Make a Poll'
    )

    # Add Command Group to Tree
    bot.tree.add_command(pollCommands)

    # Main Command
    @pollCommands.command(
        name="-",
        description="Make a Poll"
    )
    async def self(Interaction:discord.Interaction,
        question:str,
        option1:str,
        option2:str,
        # timer:float=0.0,
        option3:str='',
        option4:str='',
        option5:str='',
        option6:str='',
        option7:str='',
        option8:str='',
        option9:str='',
        option10:str=''
    ):
        await Interaction.response.send_message('Creating Poll',ephemeral=True)
        embed=discord.Embed(
                    title=f'Poll: {question}',
                    description='',
                    color=discord.Color.green()
                    ).set_author(
                        name=Interaction.user.name,
                        icon_url=Interaction.user.avatar
                    )
        embed.add_field(name='1️⃣', value=option1, inline=False)
        embed.add_field(name='2️⃣', value=option2, inline=False)
        if option3 != '':
            embed.add_field(name='3️⃣', value=option3, inline=False)
        if option4 != '':
            embed.add_field(name='4️⃣', value=option4, inline=False)
        if option5 != '':
            embed.add_field(name='5️⃣', value=option5, inline=False)
        if option6 != '':
            embed.add_field(name='6️⃣', value=option6, inline=False)
        if option7 != '':
            embed.add_field(name='7️⃣', value=option7, inline=False)
        if option8 != '':
            embed.add_field(name='8️⃣', value=option8, inline=False)
        if option9 != '':
            embed.add_field(name='9️⃣', value=option9, inline=False)
        if option10 != '':
            embed.add_field(name='🔟', value=option10, inline=False)
        if isinstance(Interaction.channel, discord.TextChannel):
        #     if timer != 0:
        #         embed.description = f'Poll Ends <t:{round(time.time()+int(timer*60))}:R>'
            poll= await Interaction.channel.send(
                embed=embed)
            # if timer != 0:
            #     def timerend(Interaction:discord.Interaction, messageid, donottouch):
            #         async def timerend2(Interaction:discord.Interaction, messageid, donottouch):
            #             await total(Interaction, messageid, donottouch)
            #         await timerend2(Interaction,messageid,donottouch)
            #     pollTimer=Timer(timer, total, (Interaction,poll.id,True))
            #     await pollTimer.start()
            await poll.add_reaction('1️⃣')
            await poll.add_reaction('2️⃣')
            if option3 != '':
                await poll.add_reaction('3️⃣')
            if option4 != '':
                await poll.add_reaction('4️⃣')
            if option5 != '':
                await poll.add_reaction('5️⃣')
            if option6 != '':
                await poll.add_reaction('6️⃣')
            if option7 != '':
                await poll.add_reaction('7️⃣')
            if option8 != '':
                await poll.add_reaction('8️⃣')
            if option9 != '':
                await poll.add_reaction('9️⃣')
            if option10 != '':
                await poll.add_reaction('🔟')

    @pollCommands.command(
        name='total',
        description='Get a tally of the most recent Untimed Poll'
    )
    async def self2(Interaction:discord.Interaction, messageid:str='', donottouch:bool=False):
        await total(Interaction,messageid,donottouch)