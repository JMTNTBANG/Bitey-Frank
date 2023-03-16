import bot
import discord


def import_command():
    # Create Command Group
    setfrankresponse_commands = discord.app_commands.Group(
        name='setfrankresponse',
        description='Add a trigger that frank will respond to with the response chosen'
    )

    # Add Command Group to Tree
    bot.tree.add_command(setfrankresponse_commands)

    # Command Info
    @setfrankresponse_commands.command(
        name="-",
        description="Add a trigger that frank will respond to with the response chosen"
    )
    # Code to Run Here
    async def add_response(interaction: discord.Interaction, trigger: str, response: str):
        open('snarks.txt', 'a').write(f't:{trigger} r:{response} u:{interaction.user}\n')
        await interaction.response.send_message(f'Frank will now respond to `{trigger}` with `{response}`',
                                                ephemeral=True)
    
    @setfrankresponse_commands.command(
        name='snarklist',
        description='List frank snarks'
    )
    async def list_responses(interaction: discord.Interaction):
        embed_page_1 = discord.Embed(
            title='Snarks',
            description='Page 1'
        )
        view_page_1 = discord.ui.View(timeout=0)
        embed_page_2 = discord.Embed(
            title='Snarks',
            description='Page 2'
        )
        view_page_2 = discord.ui.View(timeout=0)
        embed_page_3 = discord.Embed(
            title='Snarks',
            description='Page 3'
        )
        view_page_3 = discord.ui.View(timeout=0)
        embed_page_4 = discord.Embed(
            title='Snarks',
            description='Page 4'
        )
        view_page_4 = discord.ui.View(timeout=0)
        embed_page_5 = discord.Embed(
            title='Snarks',
            description='Page 5'
        )
        view_page_5 = discord.ui.View(timeout=0)
        f = open('snarks.txt', 'r')
        for x in f:
            trigger = x[x.find('t:')+2:x.find('r:')-1]
            response = x[x.find('r:')+2:x.find('u:')-1]
            creator = x[x.find('u:')+2:-1]
            if len(embed_page_1.fields) == 25:
                if len(embed_page_2.fields) == 25:
                    if len(embed_page_3.fields) == 25:
                        if len(embed_page_4.fields) == 25:
                            if len(embed_page_5.fields) == 25:
                                raise Exception('Overflow Maxed Out')
                            else:
                                embed_page_5.add_field(name=trigger,
                                                       value=f'{response} (Set by: {creator})',
                                                       inline=False)
                        else:
                            embed_page_4.add_field(name=trigger,
                                                   value=f'{response} (Set by: {creator})',
                                                   inline=False)
                    else:
                        embed_page_3.add_field(name=trigger,
                                               value=f'{response} (Set by: {creator})',
                                               inline=False)
                else:
                    embed_page_2.add_field(name=trigger,
                                           value=f'{response} (Set by: {creator})',
                                           inline=False)
            else:
                embed_page_1.add_field(name=trigger,
                                       value=f'{response} (Set by: {creator})',
                                       inline=False)

        if len(embed_page_2.fields) > 0:
            async def goto_page_2(button_press):
                if interaction.user == button_press.user:
                    await interaction.edit_original_response(embed=embed_page_2, view=view_page_2)
                else:
                    await button_press.response.send_message('YOU DID NOT USE THIS COMMAND', ephemeral=True)

            async def goto_page_1(button_press):
                if interaction.user == button_press.user:
                    await interaction.edit_original_response(embed=embed_page_1, view=view_page_1)
                else:
                    await button_press.response.send_message('YOU DID NOT USE THIS COMMAND', ephemeral=True)

            async def goto_page_3(button_press):
                if interaction.user == button_press.user:
                    await interaction.edit_original_response(embed=embed_page_3, view=view_page_3)
                else:
                    await button_press.response.send_message('YOU DID NOT USE THIS COMMAND', ephemeral=True)
            back = discord.ui.Button(style=discord.ButtonStyle.gray,
                                     emoji='◀️',
                                     disabled=True)
            forward = discord.ui.Button(style=discord.ButtonStyle.gray,
                                        emoji='▶️')
            forward.callback = goto_page_2
            view_page_1.add_item(back)
            view_page_1.add_item(forward)
            next_back = discord.ui.Button(style=discord.ButtonStyle.gray,
                                          emoji='◀️')
            if len(embed_page_3.fields) > 0:
                next_forward = discord.ui.Button(style=discord.ButtonStyle.gray,
                                                 emoji='▶️')
            else:
                next_forward = discord.ui.Button(style=discord.ButtonStyle.gray,
                                                 emoji='▶️', disabled=True)
            next_back.callback = goto_page_1
            next_forward.callback = goto_page_3
            view_page_2.add_item(next_back)
            view_page_2.add_item(next_forward)
            await interaction.response.send_message(embed=embed_page_1, view=view_page_1)
            if len(embed_page_3.fields) > 0:
                async def goto_page_2(button_press):
                    if interaction.user == button_press.user:
                        await interaction.edit_original_response(embed=embed_page_2, view=view_page_2)
                    else:
                        await button_press.response.send_message('YOU DID NOT USE THIS COMMAND', ephemeral=True)

                async def goto_page_4(button_press):
                    if interaction.user == button_press.user:
                        await interaction.edit_original_response(embed=embed_page_4, view=view_page_4)
                    else:
                        await button_press.response.send_message('YOU DID NOT USE THIS COMMAND', ephemeral=True)
                back = discord.ui.Button(style=discord.ButtonStyle.gray,
                                         emoji='◀️')
                if len(embed_page_4.fields) > 0:
                    forward = discord.ui.Button(style=discord.ButtonStyle.gray,
                                                emoji='▶️')
                else:
                    forward = discord.ui.Button(style=discord.ButtonStyle.gray,
                                                emoji='▶️', disabled=True)
                back.callback = goto_page_2
                forward.callback = goto_page_4
                view_page_3.add_item(back)
                view_page_3.add_item(forward)
                if len(embed_page_4.fields) > 0:
                    async def goto_page_3(button_press):
                        if interaction.user == button_press.user:
                            await interaction.edit_original_response(embed=embed_page_3, view=view_page_3)
                        else:
                            await button_press.response.send_message('YOU DID NOT USE THIS COMMAND', ephemeral=True)

                    async def goto_page_5(button_press):
                        if interaction.user == button_press.user:
                            await interaction.edit_original_response(embed=embed_page_5, view=view_page_5)
                        else:
                            await button_press.response.send_message('YOU DID NOT USE THIS COMMAND', ephemeral=True)
                    back = discord.ui.Button(style=discord.ButtonStyle.gray,
                                             emoji='◀️')
                    if len(embed_page_5.fields) > 0:
                        forward = discord.ui.Button(style=discord.ButtonStyle.gray,
                                                    emoji='▶️')
                    else:
                        forward = discord.ui.Button(style=discord.ButtonStyle.gray,
                                                    emoji='▶️', disabled=True)
                    back.callback = goto_page_3
                    forward.callback = goto_page_5
                    view_page_4.add_item(back)
                    view_page_4.add_item(forward)
                    if len(embed_page_5.fields) > 0:
                        async def goto_page_4(button_press):
                            if interaction.user == button_press.user:
                                await interaction.edit_original_response(embed=embed_page_4, view=view_page_4)
                            else:
                                await button_press.response.send_message('YOU DID NOT USE THIS COMMAND', ephemeral=True)
                        back = discord.ui.Button(style=discord.ButtonStyle.gray,
                                                 emoji='◀️')
                        forward = discord.ui.Button(style=discord.ButtonStyle.gray,
                                                    emoji='▶️', disabled=True)
                        back.callback = goto_page_4
                        view_page_5.add_item(back)
                        view_page_5.add_item(forward)
        else:
            back = discord.ui.Button(style=discord.ButtonStyle.gray,
                                     emoji='◀️', disabled=True)
            forward = discord.ui.Button(style=discord.ButtonStyle.gray,
                                        emoji='▶️', disabled=True)
            view_page_1.add_item(back)
            view_page_1.add_item(forward)
            await interaction.response.send_message(embed=embed_page_1, view=view_page_1)
