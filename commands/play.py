import bot
import discord
import pytube
import asyncio
import os


def import_command():
    # Command Info
    @bot.tree.command(
        name="play",
        description="Play a song in your current vc"
    )
    # Code to Run Here
    async def self(interaction: discord.Interaction, url: str):
        if interaction.user.voice is not None:
            await interaction.response.send_message("Working...")
            video = pytube.YouTube(url)
            video_loc = video.streams.get_audio_only().download()
            vc: discord.VoiceClient = await interaction.user.voice.channel.connect()
            await interaction.edit_original_response(content=f"Done! Playing `{video.title}` in {interaction.user.voice.channel.mention}")
            vc.play(discord.FFmpegPCMAudio(video_loc, executable="./ffmpeg/ffmpeg"))
            await asyncio.sleep(video.length+5)
            await vc.disconnect()
            os.remove(video_loc)
        else:
            await interaction.response.send_message("Please Enter a Voice Channel First")
