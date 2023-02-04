import bot
import discord


def import_command():
    # Command Info
    @bot.tree.command(
        name="whowon",
        description="Who Won?"
    )
    # Code to Run Here
    async def self(Interaction:discord.Interaction, magicpollid:str, doublepollid:str, magicwinner:int, doublewinner:int):
        await Interaction.response.send_message('Calculating...')
        for guild in bot.client.guilds:
            for channel in guild.channels:
                if isinstance(channel, discord.TextChannel):
                    if channel.permissions_for(guild.get_member(bot.client.user.id)).read_message_history == True:
                        async for message in channel.history():
                            if message.id == int(magicpollid):
                                global magicPoll
                                magicPoll = message
                            if message.id == int(doublepollid):
                                global doublePoll
                                doublePoll = message

        for embed in magicPoll.embeds:
            if 'Poll:' in str(embed.title):
                if 'Results' not in str(embed.title):
                    global magicPollEmbed
                    magicPollEmbed = embed
                    break
        
        for embed in doublePoll.embeds:
            if 'Poll:' in str(embed.title):
                if 'Results' not in str(embed.title):
                    global doublePollEmbed
                    doublePollEmbed = embed
                    break

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

        async def getUsers(message):
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

        embed=discord.Embed(
            title='Winners!',
            description='',
            color=discord.Color.green()
                ).set_author(
                    name=Interaction.user.name,
                    icon_url=Interaction.user.avatar
                )

        async def generateField(reactors, number, bool:bool=False):
            if bool == False:
                value = ''
                for user in reactors:
                    value += f'{user}\n'
                embed.add_field(
                    name=f'**Magical Die Winners!** (Number: {number})',
                    value=value,
                    inline=False
                    )
            else:
                value = ''
                for user in reactors:
                    value += f'{user}\n'
                embed.add_field(
                    name=f'**Double Die Winners!** (Number: {number})',
                    value=value,
                    inline=False
                    )

        await getUsers(magicPoll)

        if magicwinner != 0:
            for field in magicPollEmbed.to_dict().get('fields'):
                if field['name'] == '1️⃣':
                    if magicwinner == 1:
                        await generateField(oneReactors,'1️⃣')
                elif field['name'] == '2️⃣':
                    if magicwinner == 2:
                        await generateField(twoReactors,'2️⃣')
                elif field['name'] == '3️⃣':
                    if magicwinner == 3:
                        await generateField(threeReactors,'3️⃣')
                elif field['name'] == '4️⃣':
                    if magicwinner == 4:
                        await generateField(fourReactors,'4️⃣')
                elif field['name'] == '5️⃣':
                    if magicwinner == 5:
                        await generateField(fiveReactors,'5️⃣')
                elif field['name'] == '6️⃣':
                    if magicwinner == 6:
                        await generateField(sixReactors,'6️⃣')
                elif field['name'] == '7️⃣':
                    if magicwinner == 7:
                        await generateField(sevenReactors,'7️⃣')
                elif field['name'] == '8️⃣':
                    if magicwinner == 8:
                        await generateField(eightReactors,'8️⃣')
                elif field['name'] == '9️⃣':
                    if magicwinner == 9:
                        await generateField(nineReactors,'9️⃣')
                elif field['name'] == '🔟':
                    if magicwinner == 10:
                        await generateField(tenReactors,'🔟')

        await getUsers(doublePoll)

        if doublewinner != 0:
            for field in doublePollEmbed.to_dict().get('fields'):
                if field['name'] == '1️⃣':
                    if doublewinner == 1:
                        await generateField(oneReactors,'1️⃣',True)
                elif field['name'] == '2️⃣':
                    if doublewinner == 2:
                        await generateField(twoReactors,'2️⃣',True)
                elif field['name'] == '3️⃣':
                    if doublewinner == 3:
                        await generateField(threeReactors,'3️⃣',True)
                elif field['name'] == '4️⃣':
                    if doublewinner == 4:
                        await generateField(fourReactors,'4️⃣',True)
                elif field['name'] == '5️⃣':
                    if doublewinner == 5:
                        await generateField(fiveReactors,'5️⃣',True)
                elif field['name'] == '6️⃣':
                    if doublewinner == 6:
                        await generateField(sixReactors,'6️⃣',True)
                elif field['name'] == '7️⃣':
                    if doublewinner == 7:
                        await generateField(sevenReactors,'7️⃣',True)
                elif field['name'] == '8️⃣':
                    if doublewinner == 8:
                        await generateField(eightReactors,'8️⃣',True)
                elif field['name'] == '9️⃣':
                    if doublewinner == 9:
                        await generateField(nineReactors,'9️⃣',True)
                elif field['name'] == '🔟':
                    if doublewinner == 10:
                        await generateField(tenReactors,'🔟',True)

        poll = await Interaction.channel.send(embed=embed)