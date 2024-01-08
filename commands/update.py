import bot
import discord
import sys


def import_command():
    # Command Info
    @bot.tree.command(
        name="update",
        description="Update the Bot to latest commits"
    )
    # Code to Run Here
    async def kill(interaction: discord.Interaction):
        await interaction.response.send_message('Updating...')
        sys.exit()
    