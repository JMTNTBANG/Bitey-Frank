import bot
import discord


def import_command():
    frankJpegCommands = discord.app_commands.Group(
        name='frankjpeg',
        description='Choose a specific Frank Jpeg'
    )
    bot.tree.add_command(frankJpegCommands)
    # Command Info
    @frankJpegCommands.command(
        name="-",
        description="Choose a specific Frank Jpeg"
    )
    # Code to Run Here
    async def self(Interaction:discord.Interaction, option: int):
        await Interaction.response.send_message(file=discord.File(bot.assets[option]))

    @frankJpegCommands.command(
        name='list',
        description='List applicable Jpegs to send'
    )
    async def self(Interaction:discord.Interaction):
        message='Frank jpegs:'
        id=0
        for jpegName in bot.assets:
            message+=f'\n*{str(id)}*: **__{jpegName[7:]}__**'
            id+=1
        await Interaction.response.send_message(message)
