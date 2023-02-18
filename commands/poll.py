import bot
import discord
from threading import Timer
import time


def import_command():

    class pollModal(discord.ui.Modal, title='Create a Poll'):
        question = discord.ui.TextInput(
            label = 'What question are you asking?',
            style = discord.TextStyle.short,
            placeholder = 'If given the chance would you help Frank rule the world?',
            required = True
        )
        async def on_submit(self,Interaction:discord.Interaction):
            modal = pollModal2(self.question)
            global question
            question = self.question
            async def callback(button):
                await button.response.send_modal(modal)
            view = discord.ui.View(timeout=15)
            button = discord.ui.Button(
                label='Click here for Part 2'
            )
            button.callback = callback
            view.add_item(button)
            await Interaction.response.send_message(content='Step 1 Completed', view=view, ephemeral = True)

    class pollModal2(discord.ui.Modal, title='Create a Poll'): 
        def __init__(self,question):
            super().__init__()
            self.question = question
        option1 = discord.ui.TextInput(
            label = 'Option 1',
            style = discord.TextStyle.short,
            placeholder = 'Yes',
            required = True
        )
        option2 = discord.ui.TextInput(
            label = 'Option 2',
            style = discord.TextStyle.short,
            placeholder = 'Yes',
            required = True
        )
        option3 = discord.ui.TextInput(
            label = 'Option 3',
            style = discord.TextStyle.short,
            placeholder = 'Yes',
            required = False
        )
        option4 = discord.ui.TextInput(
            label = 'Option 4',
            style = discord.TextStyle.short,
            placeholder = 'Yes',
            required = False
        )
        option5 = discord.ui.TextInput(
            label = 'Option 5',
            style = discord.TextStyle.short,
            placeholder = 'Yes',
            required = False
        )

        async def on_submit(self, Interaction: discord.Interaction):
            modal = pollModal3(self.question,self.option1,self.option2,self.option3,self.option4,self.option5)
            async def callback(button):
                await button.response.send_modal(modal)
            view = discord.ui.View(timeout=15)
            button = discord.ui.Button(
                label='Click here for Part 3'
            )
            button.callback = callback
            view.add_item(button)
            await Interaction.response.send_message(content='Step 2 Completed', view=view, ephemeral=True)
                    

    class pollModal3(discord.ui.Modal, title='Create a Poll'):
        def __init__(self,question,option1,option2,option3,option4,option5):
            super().__init__()
            self.question = question
            self.option1 = option1
            self.option2 = option2
            self.option3 = option3
            self.option4 = option4
            self.option5 = option5
        option6 = discord.ui.TextInput(
            label = 'Option 6',
            style = discord.TextStyle.short,
            placeholder = 'Yes',
            required = False
        )
        option7 = discord.ui.TextInput(
            label = 'Option 7',
            style = discord.TextStyle.short,
            placeholder = 'Yes',
            required = False
        )
        option8 = discord.ui.TextInput(
            label = 'Option 8',
            style = discord.TextStyle.short,
            placeholder = 'Yes',
            required = False
        )
        option9 = discord.ui.TextInput(
            label = 'Option 9',
            style = discord.TextStyle.short,
            placeholder = 'Yes',
            required = False
        )
        option10 = discord.ui.TextInput(
            label = 'Option 10',
            style = discord.TextStyle.short,
            placeholder = 'say no and i come after you and your family',
            required = False
        )
        async def on_submit(self, Interaction: discord.Interaction):
            await Interaction.response.send_message('Creating Poll',ephemeral=True)
            embed=discord.Embed(
                    title=f'Poll: {question}',
                    description='',
                    color=discord.Color.green()
                    ).set_author(
                        name=Interaction.user.name,
                        icon_url=Interaction.user.avatar
                    )
            embed.add_field(name='1️⃣', value=self.option1, inline=False)
            embed.add_field(name='2️⃣', value=self.option2, inline=False)
            if self.option3.value != '':
                embed.add_field(name='3️⃣', value=self.option3, inline=False)
            if self.option4.value != '':
                embed.add_field(name='4️⃣', value=self.option4, inline=False)
            if self.option5.value != '':
                embed.add_field(name='5️⃣', value=self.option5, inline=False)
            if self.option6.value != '':
                embed.add_field(name='6️⃣', value=self.option6, inline=False)
            if self.option7.value != '':
                embed.add_field(name='7️⃣', value=self.option7, inline=False)
            if self.option8.value != '':
                embed.add_field(name='8️⃣', value=self.option8, inline=False)
            if self.option9.value != '':
                embed.add_field(name='9️⃣', value=self.option9, inline=False)
            if self.option10.value != '':
                embed.add_field(name='🔟', value=self.option10, inline=False)
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
                if self.option3.value != '':
                    await poll.add_reaction('3️⃣')
                if self.option4.value != '':
                    await poll.add_reaction('4️⃣')
                if self.option5.value != '':
                    await poll.add_reaction('5️⃣')
                if self.option6.value != '':
                    await poll.add_reaction('6️⃣')
                if self.option7.value != '':
                    await poll.add_reaction('7️⃣')
                if self.option8.value != '':
                    await poll.add_reaction('8️⃣')
                if self.option9.value != '':
                    await poll.add_reaction('9️⃣')
                if self.option10.value != '':
                    await poll.add_reaction('🔟')
        

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
    async def self(Interaction:discord.Interaction):
        modal = pollModal()
        await Interaction.response.send_modal(modal)

    @pollCommands.command(
        name='total',
        description='Get a tally of the most recent Untimed Poll'
    )
    async def self2(Interaction:discord.Interaction, messageid:str='', donottouch:bool=False):
        await total(Interaction,messageid,donottouch)