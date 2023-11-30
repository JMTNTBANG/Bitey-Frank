import bot
import discord
import pytube
import asyncio
import os


def import_command():
    # Create Command Group
    player = discord.app_commands.Group(
        name='player',
        description='Commit Some Music in a Voice Channel Near you'
    )

    # Add Command Group to Tree
    bot.tree.add_command(player)

    # Command Info
    @player.command(
        name="play",
        description="Commit Some Music in a Voice Channel Near you"
    )
    # Code to Run Here
    async def self(interaction: discord.Interaction, url: str):
        if interaction.user.voice is not None:
            await interaction.response.send_message("Working...")
            bot.music_queue.append(url)
            await interaction.edit_original_response(
                content=f"Done! Added `{pytube.YouTube(url).title}` to the Queue")
            if len(bot.music_queue) == 1:
                await bot.start_playback(interaction.user.voice.channel)
        else:
            await interaction.response.send_message("Please Enter a Voice Channel First")

    @player.command(
        name="queue",
        description="Show Song Queue"
    )
    async def self(interaction: discord.Interaction):
        embed = discord.Embed(
            title="Song Queue"
        )
        number = 0
        for song in bot.music_queue:
            number += 1
            video = pytube.YouTube(song)
            embed.add_field(name=f"{number}. \"{video.title}\" by \"{video.author}\"", value=song, inline=False)
        await interaction.response.send_message(embed=embed)
