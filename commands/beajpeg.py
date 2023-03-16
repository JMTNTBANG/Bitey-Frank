import bot
import discord
from random import choice


def import_command():
    @bot.tree.command(
        name="beajpeg",
        description="Send a Random Image of Frank"
    )
    async def be_a_jpeg(interaction: discord.Interaction):
        await interaction.response.send_message(file=discord.File(choice(bot.assets)))
