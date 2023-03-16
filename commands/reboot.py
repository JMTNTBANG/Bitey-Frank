import bot
import discord
import sys


def import_command():
    # Command Info
    @bot.tree.command(
        name="reboot",
        description="Reboot the Bot"
    )
    # Code to Run Here
    async def kill(interaction: discord.Interaction):
        await interaction.response.send_message('Rebooting...')
        sys.exit()
    