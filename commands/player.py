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
            bot.music_queue.append((url, interaction.user.id))
            await interaction.edit_original_response(
                content=f"Done! Added `{pytube.YouTube(url).title}` to the Queue")
            if len(bot.music_queue) == 1:
                await bot.start_playback(interaction.user.voice.channel)
        else:
            await interaction.response.send_message("Please Enter a Voice Channel First")

    @player.command(
        name="search",
        description="Find Some Music to Commit in a Voice Channel Near you"
    )
    async def self(interaction: discord.Interaction, query: str):
        def callback(url):
            async def callback_function(interaction: discord.Interaction):
                if interaction.user.voice is not None:
                    await interaction.response.send_message("Working...")
                    bot.music_queue.append((url, interaction.user.id))
                    await interaction.edit_original_response(
                        content=f"Done! Added `{pytube.YouTube(url).title}` to the Queue")
                    if len(bot.music_queue) == 1:
                        await bot.start_playback(interaction.user.voice.channel)
                else:
                    await interaction.response.send_message("Please Enter a Voice Channel First")
            return callback_function

        await interaction.response.send_message("Searching...")
        embed = discord.Embed(
            title=f"Results for {query}"
        )
        view = discord.ui.View(timeout=60)
        search = pytube.Search(query)
        i = 0
        for result in search.results:
            if i < 10:
                i += 1
                embed.add_field(name=f'{i}. \"{result.title}\" by {result.author}', value=result.watch_url,
                                inline=False)
                button = discord.ui.Button(label=str(i))
                button.callback = callback(result.watch_url)
                view.add_item(button)
        await interaction.edit_original_response(content="Done!", embed=embed, view=view)

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
            video = pytube.YouTube(song[0])
            embed.add_field(name=f"{number}. \"{video.title}\" by \"{video.author}\"", value=f"{song[0]}\nAdded By: {interaction.guild.get_member(song[1]).mention}", inline=False)
        await interaction.response.send_message(embed=embed)

    @player.command(
        name="toggle-pause",
        description="Play/Pause Current Playback (Instigator Only)"
    )
    async def self(interaction: discord.Interaction):
        if bot.music_queue:
            if interaction.user.voice is not None:
                if bot.music_queue[0][1] == interaction.user.id or interaction.user.guild_permissions.manage_guild:
                    vc: discord.VoiceClient = interaction.guild.voice_client
                    if vc.is_playing():
                        vc.pause()
                        await interaction.response.send_message(content="Paused...")
                    elif vc.is_paused():
                        vc.resume()
                        await interaction.response.send_message(content="Resuming...")
                else:
                    await interaction.response.send_message(content="You did not add this song, please ask the instigator or admin to pause.")
            else:
                await interaction.response.send_message(content="You are not in a voice channel, please join one and try again.")
        else:
            await interaction.response.send_message(content="Nothing is playing right now.")

    @player.command(
        name="skip",
        description="Skip the current song (Instigator Only)"
    )
    async def self(interaction: discord.Interaction):
        if bot.music_queue:
            if interaction.user.voice is not None:
                if bot.music_queue[0][1] == interaction.user.id or interaction.user.guild_permissions.manage_guild:
                    vc: discord.VoiceClient = interaction.guild.voice_client
                    vc.stop()
                    await interaction.response.send_message(content="Skipping...")
                else:
                    await interaction.response.send_message(content="You did not add this song, please ask the instigator or admin to skip.")
            else:
                await interaction.response.send_message(content="You are not in a voice channel, please join one and try again.")
        else:
            await interaction.response.send_message(content="Nothing is playing right now.")

    @player.command(
        name="remove",
        description="Remove a song from the queue (Instigator Only)"
    )
    async def self(interaction: discord.Interaction, number: int):
        if bot.music_queue:
            if interaction.user.voice is not None:
                if len(bot.music_queue) >= number > 1:
                    if bot.music_queue[number-1][1] == interaction.user.id or interaction.user.guild_permissions.manage_guild:
                        bot.music_queue.remove(bot.music_queue[number-1])
                        await interaction.response.send_message(content="Removed.")
                    else:
                        await interaction.response.send_message(content="You did not add this song, please ask the instigator or admin to remove.")
                else:
                    await interaction.response.send_message(content="Please choose a valid song in the Queue (use </player queue:1179688433350873129> for guidance)")
            else:
                await interaction.response.send_message(content="You are not in a voice channel, please join one and try again.")
        else:
            await interaction.response.send_message(content="Queue is currently empty")
