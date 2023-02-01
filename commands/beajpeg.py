import bot
import discord
from random import choice as randItem


def import_command():
    # Command Info
    @bot.tree.command(
        name="beajpeg",
        description="Send a Random Image of Frank"
    )
    # Code to Run Here
    async def self(interaction:discord.Interaction):
        await interaction.response.send_message(file=randItem(bot.assets))