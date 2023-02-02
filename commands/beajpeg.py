import bot
import discord
from random import choice as randItem


def import_command():
    @bot.tree.command(
        name="beajpeg",
        description="Send a Random Image of Frank"
    )
    async def self(interaction:discord.Interaction):
        await interaction.response.send_message(file=discord.File(randItem(bot.assets)))
