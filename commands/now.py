import bot
import discord
import time


def import_command():
    # Command Info
    @bot.tree.command(
        name="now",
        description="Get The Time"
    )
    # Code to Run Here
    async def self(Interaction:discord.Interaction):
        embed = discord.Embed(title='Current time', description=int(time.time()))
        embed.add_field(name='', value=f'<t:{int(time.time())}:t>', inline=False)
        embed.add_field(name='', value=f'<t:{int(time.time())}:T>', inline=False)
        embed.add_field(name='', value=f'<t:{int(time.time())}:d>', inline=False)
        embed.add_field(name='', value=f'<t:{int(time.time())}:D>', inline=False)
        embed.add_field(name='', value=f'<t:{int(time.time())}:f>', inline=False)
        embed.add_field(name='', value=f'<t:{int(time.time())}:F>', inline=False)
        embed.add_field(name='', value=f'<t:{int(time.time())}:R>', inline=False)
        await Interaction.response.send_message(embed=embed)