import bot
import discord


def import_command():

    # Create Command Group
    frankJpegCommands = discord.app_commands.Group(
        name='frankjpeg',
        description='Choose a specific Frank Jpeg'
    )

    # Add Command Group to Tree
    bot.tree.add_command(frankJpegCommands)

    # Main Command
    @frankJpegCommands.command(
        name="-",
        description="Choose a specific Frank Jpeg"
    )
    async def self(Interaction:discord.Interaction, option: int):
        await Interaction.response.send_message(file=discord.File(bot.assets[option]))

    # List Sub-Command
    @frankJpegCommands.command(
        name='list',
        description='List applicable Jpegs to send'
    )
    async def self2(Interaction:discord.Interaction):
        message='Frank jpegs:'
        id=0
        for jpegName in bot.assets:
            message+=f'\n*{str(id)}*: **__{jpegName[7:]}__**'
            id+=1
        await Interaction.response.send_message(message)
