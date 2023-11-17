import bot
import discord
import json
import datetime


def import_command():

    birthday_commands = discord.app_commands.Group(
        name='birthday',
        description='Get birthday celebrations from frank'
    )

    # Add Command group to tree
    bot.tree.add_command(birthday_commands)

    # Command Info
    @birthday_commands.command(
        name="set"
    )
    # Code to Run Here
    async def self(interaction: discord.Interaction, b_month, b_day, b_year):
        pass

    # Command Info
    @birthday_commands.command(
        name="remove"
    )
    # Code to Run Here
    async def self(interaction: discord.Interaction):
        pass  # delete this before you start coding
