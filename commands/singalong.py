import bot
import discord
from lyricsgenius import Genius
from dotenv import load_dotenv
from os import getenv
from datetime import datetime


def strip_non_alpha(str):
    mod_string = ""
    for elem in str:
        if elem.isalnum() or elem == ' ' or elem == '\n':
            mod_string += elem
    return mod_string


load_dotenv()
token = getenv('GENIUS')
if token is None:
    raise ValueError('Please Paste your Access Token in the .env file')
try:
    GeniusAPI: Genius = Genius(token, remove_section_headers=True, verbose=True)
except TypeError:
    raise ValueError('Please try a new Access Token as this one did not work...')


def import_command():
    # Command Info
    @bot.tree.command(
        name="singalong",
        description="Have Frank sing along to a song with you")
    # Code to Run Here
    async def self(interaction: discord.Interaction, song_title: str, artist: str):
        await interaction.response.send_message("One Moment...", ephemeral=True)
        for guild in bot.client.guilds:
            if guild == interaction.guild:
                for channel in guild.text_channels:
                    if channel.topic is not None:
                        if "Current Song:" in channel.topic:
                            if interaction.channel == channel:
                                song = GeniusAPI.search_song(song_title, artist)
                                lyric_file = open("../lyrics.txt", "w")
                                if song is None:
                                    await interaction.edit_original_response(content="Could not find that song, Please try again.")
                                else:
                                    should_continue = False
                                    lyric_file.write(song.lyrics)
                                    lyric_file.close()
                                    channel_topic = f"Current Song: \"{song.title}\" by \"{song.artist}\"\n\n"
                                    prev_timestamp = int(channel.topic[channel.topic.find("TIMESTAMP: ") + 11:channel.topic.find("USES: ") - 1])
                                    prev_uses = int(channel.topic[channel.topic.find("USES: ") + 6:])
                                    if round(datetime.now().timestamp(), 0) - prev_timestamp > 600:
                                        channel_topic += f'TIMESTAMP: {round(datetime.now().timestamp())}\nUSES: 1'
                                        should_continue = True
                                    elif int(channel.topic[channel.topic.find("USES: ") + 6]) < 2:
                                        channel_topic += f'TIMESTAMP: {prev_timestamp}\nUSES: {prev_uses + 1}'
                                        should_continue = True
                                    if should_continue:
                                        await channel.edit(topic=channel_topic)
                                        await interaction.edit_original_response(content=f"All Set! Start singing `{song.title}` by `{song.artist}` and ill join along!")
                                        await channel.send(f'```\n'
                                                           f'Song Change: \"{song.title}\" by \"{song.artist}\"\n'
                                                           f'Changed by: {interaction.user.display_name}\n'
                                                           f'```',
                                                           file=discord.File("../lyrics.txt"))
                                    else:
                                        await interaction.edit_original_response(content=f'Apologies, but this feature is on cooldown and will be ready <t:{prev_timestamp + 600}:R>\n'
                                                                                         f'Please try again then')
