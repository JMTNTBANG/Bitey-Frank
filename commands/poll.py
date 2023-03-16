import bot
import discord

found_poll: None
found_poll_embed: None
poll_question: discord.ui.TextInput
poll_option_1: discord.ui.TextInput
poll_option_2: discord.ui.TextInput
poll_option_3: discord.ui.TextInput
poll_option_4: discord.ui.TextInput
poll_option_5: discord.ui.TextInput


def import_command():
    class PollModal(discord.ui.Modal,
                    title='Create a Poll'):
        question = discord.ui.TextInput(
            label='What question are you asking?',
            placeholder='If given the chance would you help Frank rule the world?'
        )

        async def on_submit(self,
                            interaction: discord.Interaction):
            modal = PollModalStep2()
            global poll_question

            async def callback(next_step_button):
                await next_step_button.response.send_modal(modal)

            view = discord.ui.View(timeout=15)
            button = discord.ui.Button(
                label='Click here for Part 2'
            )
            button.callback = callback
            view.add_item(button)
            await interaction.response.send_message(content='Step 1 Completed',
                                                    view=view,
                                                    ephemeral=True)

    class PollModalStep2(discord.ui.Modal, title='Create a Poll'):
        option1 = discord.ui.TextInput(
            label='Option 1',
            placeholder='Yes',
        )
        option2 = discord.ui.TextInput(
            label='Option 2',
            placeholder='Yes',
        )
        option3 = discord.ui.TextInput(
            label='Option 3',
            placeholder='Yes',
            required=False
        )
        option4 = discord.ui.TextInput(
            label='Option 4',
            placeholder='Yes',
            required=False
        )
        option5 = discord.ui.TextInput(
            label='Option 5',
            placeholder='Yes',
            required=False
        )

        async def on_submit(self, interaction: discord.Interaction):
            modal = PollModalStep3()
            global poll_option_1
            global poll_option_2
            global poll_option_3
            global poll_option_4
            global poll_option_5
            poll_option_1 = self.option1
            poll_option_2 = self.option2
            poll_option_3 = self.option3
            poll_option_4 = self.option4
            poll_option_5 = self.option5

            async def callback(next_step_button):
                await next_step_button.response.send_modal(modal)

            view = discord.ui.View(timeout=15)
            button = discord.ui.Button(
                label='Click here for Part 3'
            )
            button.callback = callback
            view.add_item(button)
            await interaction.response.send_message(content='Step 2 Completed',
                                                    view=view,
                                                    ephemeral=True)

    class PollModalStep3(discord.ui.Modal,
                         title='Create a Poll'):
        option6 = discord.ui.TextInput(
            label='Option 6',
            placeholder='Yes',
            required=False
        )
        option7 = discord.ui.TextInput(
            label='Option 7',
            placeholder='Yes',
            required=False
        )
        option8 = discord.ui.TextInput(
            label='Option 8',
            placeholder='Yes',
            required=False
        )
        option9 = discord.ui.TextInput(
            label='Option 9',
            placeholder='Yes',
            required=False
        )
        option10 = discord.ui.TextInput(
            label='Option 10',
            placeholder='say no and i come after you and your family',
            required=False
        )

        async def on_submit(self,
                            interaction: discord.Interaction):
            await interaction.response.send_message('Creating Poll',
                                                    ephemeral=True)
            embed = discord.Embed(
                title=f'Poll: {poll_question}',
                description='',
                color=discord.Color.green()
            ).set_author(
                name=interaction.user.name,
                icon_url=interaction.user.avatar
            )
            embed.add_field(name='1️⃣', value=poll_option_1, inline=False)
            embed.add_field(name='2️⃣', value=poll_option_2, inline=False)
            if poll_option_3.value != '':
                embed.add_field(name='3️⃣', value=poll_option_3, inline=False)
            if poll_option_4.value != '':
                embed.add_field(name='4️⃣', value=poll_option_4, inline=False)
            if poll_option_5.value != '':
                embed.add_field(name='5️⃣', value=poll_option_5, inline=False)
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
            if isinstance(interaction.channel, discord.TextChannel):
                #  if timer != 0:
                #      embed.description = f'Poll Ends <t:{round(time.time()+int(timer*60))}:R>'
                poll = await interaction.channel.send(embed=embed)
                #  if timer != 0:
                #      def timerend(Interaction:discord.Interaction, messageid, donottouch):
                #          async def timerend2(Interaction:discord.Interaction, messageid, donottouch):
                #              await total(Interaction, messageid, donottouch)
                #          await timerend2(Interaction,messageid,donottouch)
                #      pollTimer=Timer(timer, total, (Interaction,poll.id,True))
                #      await pollTimer.start()
                await poll.add_reaction('1️⃣')
                await poll.add_reaction('2️⃣')
                if poll_option_3.value != '':
                    await poll.add_reaction('3️⃣')
                if poll_option_4.value != '':
                    await poll.add_reaction('4️⃣')
                if poll_option_5.value != '':
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

    async def total(interaction: discord.Interaction,
                    message_id: str = '',
                    do_not_touch: bool = False):
        if not do_not_touch:
            await interaction.response.send_message('Calculating...')
        global found_poll
        global found_poll_embed
        if isinstance(interaction.channel,
                      discord.TextChannel):
            if message_id == '':
                async for message in interaction.channel.history():
                    for embed in message.embeds:
                        if 'Poll:' in str(embed.title):
                            if 'Results' not in str(embed.title):
                                found_poll = message
                                found_poll_embed = embed
                                break
                    if found_poll != discord.Message:
                        break
            else:
                for guild in bot.client.guilds:
                    for channel in guild.text_channels:
                        async for message in channel.history():
                            if message.id == int(message_id):
                                for embed in message.embeds:
                                    if 'Poll:' in str(embed.title):
                                        if 'Results' not in str(embed.title):
                                            found_poll = message
                                            found_poll_embed = embed
                                            break
                            if found_poll != discord.Message:
                                break
                        if found_poll != discord.Message:
                            break
                    if found_poll != discord.Message:
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

            for reaction in found_poll.reactions:
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

            total_reactors = 0
            if one_reactors:
                total_reactors += len(one_reactors)
            if two_reactors:
                total_reactors += len(two_reactors)
            if three_reactors:
                total_reactors += len(three_reactors)
            if four_reactors:
                total_reactors += len(four_reactors)
            if five_reactors:
                total_reactors += len(five_reactors)
            if six_reactors:
                total_reactors += len(six_reactors)
            if seven_reactors:
                total_reactors += len(seven_reactors)
            if eight_reactors:
                total_reactors += len(eight_reactors)
            if nine_reactors:
                total_reactors += len(nine_reactors)
            if ten_reactors:
                total_reactors += len(ten_reactors)

            embed = discord.Embed(
                title=f'Results for {found_poll_embed.title}',
                description=f'{total_reactors} Total Participant(s)',
                color=discord.Color.green()
            ).set_author(
                name=interaction.user.name,
                icon_url=interaction.user.avatar
            )

            async def generate_field(reactors, number):
                if len(one_reactors) != 0:
                    embed.add_field(
                        name=number,
                        value=f'{field["value"]} -- **{round(len(reactors) / total_reactors * 100)}%** ***{len(reactors)} User(s)***',
                        inline=False
                    )
                else:
                    embed.add_field(
                        name=number,
                        value=f'{field["value"]} -- **0%** ***0 User(s)***',
                        inline=False
                    )

            for field in found_poll_embed.to_dict().get('fields'):
                if field['name'] == '1️⃣':
                    await generate_field(one_reactors, '1️⃣')
                elif field['name'] == '2️⃣':
                    await generate_field(two_reactors, '2️⃣')
                elif field['name'] == '3️⃣':
                    await generate_field(three_reactors, '3️⃣')
                elif field['name'] == '4️⃣':
                    await generate_field(four_reactors, '4️⃣')
                elif field['name'] == '5️⃣':
                    await generate_field(five_reactors, '5️⃣')
                elif field['name'] == '6️⃣':
                    await generate_field(six_reactors, '6️⃣')
                elif field['name'] == '7️⃣':
                    await generate_field(seven_reactors, '7️⃣')
                elif field['name'] == '8️⃣':
                    await generate_field(eight_reactors, '8️⃣')
                elif field['name'] == '9️⃣':
                    await generate_field(nine_reactors, '9️⃣')
                elif field['name'] == '🔟':
                    await generate_field(ten_reactors, '🔟')

            await found_poll.channel.send(embed=embed)

    # Create Command Group
    poll_commands = discord.app_commands.Group(
        name='poll',
        description='Make a Poll'
    )

    # Add Command Group to Tree
    bot.tree.add_command(poll_commands)

    # Main Command
    @poll_commands.command(
        name="-",
        description="Make a Poll"
    )
    async def gen_poll(interaction: discord.Interaction):
        modal = PollModal()
        await interaction.response.send_modal(modal)

    @poll_commands.command(
        name='total',
        description='Get a tally of the most recent Untimed Poll'
    )
    async def tally_poll(interaction: discord.Interaction,
                         message_id: str = '',
                         do_not_touch: bool = False):
        await total(interaction,
                    message_id,
                    do_not_touch)
