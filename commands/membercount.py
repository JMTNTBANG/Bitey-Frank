import bot
import discord


def import_command():
    # Command Info
    @bot.tree.command(
        name="membercount",
        description="Pull the amount of people in the server"
    )
    # Code to Run Here
    async def print_member_count(interaction: discord.Interaction):
        members = 0
        people = 0
        bots = 0
        for user in interaction.guild.members:
            if user.bot:
                bots += 1
            else:
                people += 1
            members += 1
        
        embed = discord.Embed(title='Member Count')
        embed.add_field(name='Total Members:', value=members, inline=False)
        embed.add_field(name='People', value=people)
        embed.add_field(name='Bots', value=bots)
        await interaction.response.send_message(embed=embed)