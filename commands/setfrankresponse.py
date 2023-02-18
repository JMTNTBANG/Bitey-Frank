import bot
import discord

def import_command():

    # Create Command Group
    setfrankresponseCommands = discord.app_commands.Group(
        name='setfrankresponse',
        description='Add a trigger that frank will respond to with the response chosen'
    )

    # Add Command Group to Tree
    bot.tree.add_command(setfrankresponseCommands)

    # Command Info
    @setfrankresponseCommands.command(
        name="-",
        description="Add a trigger that frank will respond to with the response chosen"
    )
    # Code to Run Here
    async def self(Interaction:discord.Interaction, trigger:str, response:str):
        open('snarks.txt', 'a').write(f't:{trigger} r:{response} u:{Interaction.user}\n')
        await Interaction.response.send_message(f'Frank will now respond to `{trigger}` with `{response}`', ephemeral=True)
    
    @setfrankresponseCommands.command(
        name='snarklist',
        description='List frank snarks'
    )
    async def self2(Interaction:discord.Interaction):
        embed=discord.Embed(
            title='Snarks',
            description='Page 1'
        )
        view=discord.ui.View(timeout=0)
        embed2=discord.Embed(
            title='Snarks',
            description='Page 2'
        )
        view2=discord.ui.View(timeout=0)
        embed3=discord.Embed(
            title='Snarks',
            description='Page 3'
        )
        view3=discord.ui.View(timeout=0)
        embed4=discord.Embed(
            title='Snarks',
            description='Page 4'
        )
        view4=discord.ui.View(timeout=0)
        embed5=discord.Embed(
            title='Snarks',
            description='Page 5'
        )
        view5=discord.ui.View(timeout=0)
        f = open('snarks.txt', 'r')
        for x in f:
            trigger = x[x.find('t:')+2:x.find('r:')-1]
            response = x[x.find('r:')+2:x.find('u:')-1]
            creator = x[x.find('u:')+2:-1]
            if len(embed.fields) == 25:
                if len(embed2.fields) == 25:
                    if len(embed3.fields) == 25:
                        if len(embed4.fields) == 25:
                            if len(embed5.fields) == 25:
                                raise Exception('Overflow Maxed Out')
                            else:
                                embed5.add_field(name=trigger,value=f'{response} (Set by: {creator})',inline=False)
                        else:
                            embed4.add_field(name=trigger,value=f'{response} (Set by: {creator})',inline=False)
                    else:
                        embed3.add_field(name=trigger,value=f'{response} (Set by: {creator})',inline=False)
                else:
                    embed2.add_field(name=trigger,value=f'{response} (Set by: {creator})',inline=False)
            else:
                embed.add_field(name=trigger,value=f'{response} (Set by: {creator})',inline=False)

        

        if len(embed2.fields) > 0:
            async def callback(button):
                if Interaction.user == button.user:
                    await Interaction.edit_original_response(embed=embed2, view=view2)
                else:
                    await button.response.send_message('YOU DID NOT USE THIS COMMAND', ephemeral=True)
            async def callback2(button):
                if Interaction.user == button.user:
                    await Interaction.edit_original_response(embed=embed, view=view)
                else:
                    await button.response.send_message('YOU DID NOT USE THIS COMMAND', ephemeral=True)
            async def callback3(button):
                if Interaction.user == button.user:
                    await Interaction.edit_original_response(embed=embed3, view=view3)
                else:
                    await button.response.send_message('YOU DID NOT USE THIS COMMAND', ephemeral=True)
            button = discord.ui.Button(style=discord.ButtonStyle.gray,emoji='◀️', disabled=True)
            button2 = discord.ui.Button(style=discord.ButtonStyle.gray,emoji='▶️')
            button2.callback=callback
            view.add_item(button)
            view.add_item(button2)
            button3 = discord.ui.Button(style=discord.ButtonStyle.gray,emoji='◀️')
            if len(embed3.fields) > 0:
                button4 = discord.ui.Button(style=discord.ButtonStyle.gray,emoji='▶️')
            else:
                button4 = discord.ui.Button(style=discord.ButtonStyle.gray,emoji='▶️', disabled=True)
            button3.callback=callback2
            button4.callback=callback3
            view2.add_item(button3)
            view2.add_item(button4)
            await Interaction.response.send_message(embed=embed, view=view)
            if len(embed3.fields) > 0:
                async def callback(button):
                    if Interaction.user == button.user:
                        await Interaction.edit_original_response(embed=embed2, view=view2)
                    else:
                        await button.response.send_message('YOU DID NOT USE THIS COMMAND', ephemeral=True)
                async def callback2(button):
                    if Interaction.user == button.user:
                        await Interaction.edit_original_response(embed=embed4, view=view4)
                    else:
                        await button.response.send_message('YOU DID NOT USE THIS COMMAND', ephemeral=True)
                button = discord.ui.Button(style=discord.ButtonStyle.gray,emoji='◀️')
                if len(embed4.fields) > 0:
                    button2 = discord.ui.Button(style=discord.ButtonStyle.gray,emoji='▶️')
                else:
                    button2 = discord.ui.Button(style=discord.ButtonStyle.gray,emoji='▶️', disabled=True)
                button.callback=callback
                button2.callback=callback2
                view3.add_item(button)
                view3.add_item(button2)
                if len(embed4.fields) > 0:
                    async def callback(button):
                        if Interaction.user == button.user:
                            await Interaction.edit_original_response(embed=embed3, view=view3)
                        else:
                            await button.response.send_message('YOU DID NOT USE THIS COMMAND', ephemeral=True)
                    async def callback2(button):
                        if Interaction.user == button.user:
                            await Interaction.edit_original_response(embed=embed5, view=view5)
                        else:
                            await button.response.send_message('YOU DID NOT USE THIS COMMAND', ephemeral=True)
                    button = discord.ui.Button(style=discord.ButtonStyle.gray,emoji='◀️')
                    if len(embed5.fields) > 0:
                        button2 = discord.ui.Button(style=discord.ButtonStyle.gray,emoji='▶️')
                    else:
                        button2 = discord.ui.Button(style=discord.ButtonStyle.gray,emoji='▶️', disabled=True)
                    button.callback=callback
                    button2.callback=callback2
                    view4.add_item(button)
                    view4.add_item(button2)
                    if len(embed5.fields) > 0: 
                        async def callback(button):
                            if Interaction.user == button.user:
                                await Interaction.edit_original_response(embed=embed4, view=view4)
                            else:
                                await button.response.send_message('YOU DID NOT USE THIS COMMAND', ephemeral=True)
                        button = discord.ui.Button(style=discord.ButtonStyle.gray,emoji='◀️')
                        button2 = discord.ui.Button(style=discord.ButtonStyle.gray,emoji='▶️', disabled=True)
                        button.callback=callback
                        view5.add_item(button)
                        view5.add_item(button2)
        else:
            button = discord.ui.Button(style=discord.ButtonStyle.gray,emoji='◀️', disabled=True)
            button2 = discord.ui.Button(style=discord.ButtonStyle.gray,emoji='▶️', disabled=True)
            view.add_item(button)
            view.add_item(button2)
            await Interaction.response.send_message(embed=embed, view=view)
