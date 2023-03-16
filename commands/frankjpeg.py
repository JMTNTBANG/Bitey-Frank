import bot
import discord


def import_command():

    # Create Command Group
    frank_jpeg_commands = discord.app_commands.Group(
        name='frankjpeg',
        description='Choose a specific Frank Jpeg'
    )

    # Add Command Group to Tree
    bot.tree.add_command(frank_jpeg_commands)

    # Main Command
    @frank_jpeg_commands.command(
        name="-",
        description="Choose a specific Frank Jpeg"
    )
    async def send_frank_jpeg(interaction: discord.Interaction,
                              option: int):
        await interaction.response.send_message(file=discord.File(bot.assets[option]))

    # List Sub-Command
    @frank_jpeg_commands.command(
        name='list',
        description='List applicable Jpegs to send'
    )
    async def list_frank_jpegs(interaction: discord.Interaction):
        message = 'Frank jpegs:'
        asset_id = 0
        for jpegName in bot.assets:
            message += f'\n*{asset_id}*: **__{jpegName[7:]}__**'
            asset_id += 1
        await interaction.response.send_message(message)
