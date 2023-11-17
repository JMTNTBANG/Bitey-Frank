import bot
import discord
import json
import datetime


def import_command():

    birthday_commands = discord.app_commands.Group(
        name='birthday',
        description='Get birthday celebrations from Frank'
    )

    # Add Command group to tree
    bot.tree.add_command(birthday_commands)

    # Command Info
    @birthday_commands.command(
        name="set",
        description='Get birthday celebrations from Frank'
    )
    # Code to Run Here
    async def self(interaction: discord.Interaction, mm: int, dd: int, yyyy: int = 1):
        timestamp = datetime.datetime(yyyy, mm, dd).timestamp()
        birthdays = json.loads(open("birthdays.json", "r").read())
        birthdays[interaction.user.id] = timestamp
        with open("birthdays.json", "w") as update:
            update.write(json.dumps(birthdays, indent=3))
        await interaction.response.send_message("Done!")

    # Command Info
    @birthday_commands.command(
        name="remove",
        description='No longer get birthday celebrations from Frank'
    )
    # Code to Run Here
    async def self(interaction: discord.Interaction):
        birthdays = json.loads(open("birthdays.json", "r").read())
        birthdays.pop(interaction.user.id)
        with open("birthdays.json", "w") as update:
            update.write(json.dumps(birthdays, indent=3))
        await interaction.response.send_message("Done!")

    @birthday_commands.command(
        name="list",
        description='List birthdays'
    )
    # Code to Run Here
    async def self(interaction: discord.Interaction):
        birthdays = json.loads(open("birthdays.json", "r").read())
        embed = discord.Embed(
            title="Birthdays"
        )
        for birthday in birthdays:
            user = interaction.guild.get_member(int(birthday))
            birthday = datetime.datetime.fromtimestamp(birthdays[birthday])
            if birthday.year > 1:
                embed.add_field(name=user.display_name, value=birthday.strftime("%m/%d/%Y"))
            else:
                embed.add_field(name=user.display_name, value=birthday.strftime("%m/%d"))
        await interaction.response.send_message(embed=embed)
