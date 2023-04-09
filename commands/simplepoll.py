import bot
import discord


def import_command():
    # Command Info
    @bot.tree.command(
        name="simplepoll",
        description="Makes a simple poll"
    )
    # Code to Run Here
    async def self(interaction: discord.Interaction, title: str, description: str):
        await interaction.response.send_message('Creating...', ephemeral=True)
        embed = discord.Embed(title=title, description=description)
        await interaction.channel.send(embed=embed)
