import bot
import discord
from random import choice


def import_command():

    die = {
        1: bot.emojis[':die1:'],
        2: bot.emojis[':die2:'],
        3: bot.emojis[':die3:'],
        4: bot.emojis[':die4:'],
        5: bot.emojis[':die5:'],
        6: bot.emojis[':die6:']
    }

    # Command Info
    @bot.tree.command(
        name="rolladie",
        description="Roll a die"
    )
    # Code to Run Here
    async def roll_a_die(interaction: discord.Interaction):
        await interaction.response.send_message(choice(die))
