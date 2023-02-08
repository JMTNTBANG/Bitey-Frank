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
        open('messageResponses.txt', 'a').write(f't:{trigger} r:{response} u:{Interaction.user}\n')
        await Interaction.response.send_message(f'Frank will now respond to `{trigger}` with `{response}`', ephemeral=True)
    
    @setfrankresponseCommands.command(
        name='snarklist',
        description='List frank snarks'
    )
    async def self2(Interaction:discord.Interaction):
        embed=discord.Embed(
            title='Snarks',
            description=''
        )
        f = open('messageResponses.txt', 'r')
        for x in f:
            trigger = x[x.find('t:')+2:x.find('r:')-1]
            response = x[x.find('r:')+2:x.find('u:')-1]
            creator = x[x.find('u:')+2:-1]
            embed.add_field(name=trigger,value=f'{response} (Set by: {creator})',inline=False)

        await Interaction.response.send_message(embed=embed)