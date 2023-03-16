import bot
import discord
magic_poll: discord.Message
double_poll: discord.Message
magic_poll_embed: discord.Embed
double_poll_embed: discord.Embed


def import_command():
    # Command Info
    @bot.tree.command(
        name="whowon",
        description="Who Won?"
    )
    # Code to Run Here
    async def who_won(interaction: discord.Interaction,
                      magic_poll_id: str,
                      double_poll_id: str,
                      magic_winner: int,
                      double_winner: int):
        await interaction.response.send_message('Calculating...')
        for guild in bot.client.guilds:
            for channel in guild.channels:
                if isinstance(channel, discord.TextChannel):
                    if channel.permissions_for(guild.get_member(bot.client.user.id)).read_message_history:
                        async for message in channel.history():
                            if message.id == int(magic_poll_id):
                                global magic_poll
                                magic_poll = message
                            if message.id == int(double_poll_id):
                                global double_poll
                                double_poll = message

        for embed in magic_poll.embeds:
            if 'Poll:' in str(embed.title):
                if 'Results' not in str(embed.title):
                    global magic_poll_embed
                    magic_poll_embed = embed
                    break
        
        for embed in double_poll.embeds:
            if 'Poll:' in str(embed.title):
                if 'Results' not in str(embed.title):
                    global double_poll_embed
                    double_poll_embed = embed
                    break

        one_reactors = []
        two_reactors = []
        three_reactors = []
        four_reactors = []
        five_reactors = []
        six_reactors = []
        seven_reactors = []
        eight_reactors = []
        nine_reactors = []
        ten_reactors = []

        async def get_users(source_message):
            for reaction in source_message.reactions:
                if reaction.emoji == '1️⃣':
                    async for user in reaction.users():
                        if str(bot.client.user) not in str(user):
                            one_reactors.append(user)
                    
                elif reaction.emoji == '2️⃣':
                    async for user in reaction.users():
                        if str(bot.client.user) not in str(user):
                            two_reactors.append(user)
                    
                elif reaction.emoji == '3️⃣':
                    async for user in reaction.users():
                        if str(bot.client.user) not in str(user):
                            three_reactors.append(user)
                    
                elif reaction.emoji == '4️⃣':
                    async for user in reaction.users():
                        if str(bot.client.user) not in str(user):
                            four_reactors.append(user)
                    
                elif reaction.emoji == '5️⃣':
                    async for user in reaction.users():
                        if str(bot.client.user) not in str(user):
                            five_reactors.append(user)
                    
                elif reaction.emoji == '6️⃣':
                    async for user in reaction.users():
                        if str(bot.client.user) not in str(user):
                            six_reactors.append(user)
                    
                elif reaction.emoji == '7️⃣':
                    async for user in reaction.users():
                        if str(bot.client.user) not in str(user):
                            seven_reactors.append(user)
                    
                elif reaction.emoji == '8️⃣':
                    async for user in reaction.users():
                        if str(bot.client.user) not in str(user):
                            eight_reactors.append(user)
                    
                elif reaction.emoji == '9️⃣':
                    async for user in reaction.users():
                        if str(bot.client.user) not in str(user):
                            nine_reactors.append(user)
                    
                elif reaction.emoji == '🔟':
                    async for user in reaction.users():
                        if str(bot.client.user) not in str(user):
                            ten_reactors.append(user)

        embed = discord.Embed(
            title='Winners!',
            description='',
            color=discord.Color.green()
                ).set_author(
                    name=interaction.user.name,
                    icon_url=interaction.user.avatar
                )

        async def generate_field(reactors, number, is_double: bool = False):
            if not is_double:
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

        await get_users(magic_poll)

        if magic_winner != 0:
            for field in magic_poll_embed.to_dict().get('fields'):
                if field['name'] == '1️⃣':
                    if magic_winner == 1:
                        await generate_field(one_reactors, '1️⃣')
                elif field['name'] == '2️⃣':
                    if magic_winner == 2:
                        await generate_field(two_reactors, '2️⃣')
                elif field['name'] == '3️⃣':
                    if magic_winner == 3:
                        await generate_field(three_reactors, '3️⃣')
                elif field['name'] == '4️⃣':
                    if magic_winner == 4:
                        await generate_field(four_reactors, '4️⃣')
                elif field['name'] == '5️⃣':
                    if magic_winner == 5:
                        await generate_field(five_reactors, '5️⃣')
                elif field['name'] == '6️⃣':
                    if magic_winner == 6:
                        await generate_field(six_reactors, '6️⃣')
                elif field['name'] == '7️⃣':
                    if magic_winner == 7:
                        await generate_field(seven_reactors, '7️⃣')
                elif field['name'] == '8️⃣':
                    if magic_winner == 8:
                        await generate_field(eight_reactors, '8️⃣')
                elif field['name'] == '9️⃣':
                    if magic_winner == 9:
                        await generate_field(nine_reactors, '9️⃣')
                elif field['name'] == '🔟':
                    if magic_winner == 10:
                        await generate_field(ten_reactors, '🔟')

        await get_users(double_poll)

        if double_winner != 0:
            for field in double_poll_embed.to_dict().get('fields'):
                if field['name'] == '1️⃣':
                    if double_winner == 1:
                        await generate_field(one_reactors, '1️⃣', True)
                elif field['name'] == '2️⃣':
                    if double_winner == 2:
                        await generate_field(two_reactors, '2️⃣', True)
                elif field['name'] == '3️⃣':
                    if double_winner == 3:
                        await generate_field(three_reactors, '3️⃣', True)
                elif field['name'] == '4️⃣':
                    if double_winner == 4:
                        await generate_field(four_reactors, '4️⃣', True)
                elif field['name'] == '5️⃣':
                    if double_winner == 5:
                        await generate_field(five_reactors, '5️⃣', True)
                elif field['name'] == '6️⃣':
                    if double_winner == 6:
                        await generate_field(six_reactors, '6️⃣', True)
                elif field['name'] == '7️⃣':
                    if double_winner == 7:
                        await generate_field(seven_reactors, '7️⃣', True)
                elif field['name'] == '8️⃣':
                    if double_winner == 8:
                        await generate_field(eight_reactors, '8️⃣', True)
                elif field['name'] == '9️⃣':
                    if double_winner == 9:
                        await generate_field(nine_reactors, '9️⃣', True)
                elif field['name'] == '🔟':
                    if double_winner == 10:
                        await generate_field(ten_reactors, '🔟', True)

        await interaction.channel.send(embed=embed)
