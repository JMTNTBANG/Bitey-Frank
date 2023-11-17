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
    async def self(interaction: discord.Interaction, b_month: int, b_day: int, b_year: int):
        timestamp = datetime.datetime(b_year, b_month, b_day).timestamp()
        birthdays = json.loads(open("birthdays.json", "r").read())
        birthdays[interaction.user.display_name] = timestamp
        update = open("birthdays.json", "w")
        update.write(json.dumps(birthdays, indent=3))
        update.close()
        await interaction.response.send_message("Done!")

    # Command Info
    @birthday_commands.command(
        name="remove"
    )
    # Code to Run Here
    async def self(interaction: discord.Interaction):
        pass  # delete this before you start coding
