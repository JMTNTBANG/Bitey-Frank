import bot
import discord
import csv
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
        with open("../birthdays.csv") as file:
            birthdays = csv.reader(file, delimiter=',')
            writer = csv.writer(file, delimiter=',')
            unadded = False
            for birthday in birthdays:
                if not birthday[0] == 'UserID' and not birthday[1] == 'BirthdayUNIX':
                    user = birthday[0]
                    if user == interaction.user.id:
                        writer.writerow()





                    # pulled_bday = datetime.datetime.fromtimestamp(float(birthday_unix))





    # Command Info
    @birthday_commands.command(
        name="remove"
    )
    # Code to Run Here
    async def self(interaction: discord.Interaction):
        pass  # delete this before you start coding
