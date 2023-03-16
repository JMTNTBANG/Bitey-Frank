import bot
import discord


def import_command():
    # Command Info
    @bot.tree.command(
        name="Command Name (No Spaces/Caps/Special Characters)",
        description="Description here"
    )
    # Code to Run Here
    async def self(interaction: discord.Interaction):
        pass  # delete this before you start coding
