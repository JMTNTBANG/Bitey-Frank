import bot
import discord
import os


def import_command():

    # Create Command Group
    frank_jpeg_commands = discord.app_commands.Group(
        name='frankjpeg',
        description='Choose a specific Frank jpeg'
    )

    # Add Command Group to Tree
    bot.tree.add_command(frank_jpeg_commands)

    # Number Command
    @frank_jpeg_commands.command(
        name="num",
        description="Choose a Frank jpeg by number"
    )
    async def send_frank_jpeg_num(interaction: discord.Interaction, option: int):
        await interaction.response.send_message(file = discord.File(bot.assets[option]))

    # Name Command
    @frank_jpeg_commands.command(
        name="name",
        description="Choose a Frank jpeg by name, including the file extension"
    )
    async def send_frank_jpeg_name(interaction: discord.Interaction, option: str):
        # Get just the file names
        jpegNames = [os.path.basename(asset).casefold() for asset in bot.assets]
        jpegIndex = jpegNames.index(option.casefold())
        await interaction.response.send_message(file = discord.File(bot.assets[jpegIndex]))

    # List Sub-Command
    @frank_jpeg_commands.command(
        name='list',
        description='List Frank jpegs'
    )
    async def list_frank_jpegs(interaction: discord.Interaction):
        message = 'Frank jpegs:'
        for asset_id, jpegName in enumerate(bot.assets):
            message += f'\n*{asset_id}*: **{os.path.basename(jpegName)}**'
        await interaction.response.send_message(message)
